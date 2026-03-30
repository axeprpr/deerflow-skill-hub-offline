#!/usr/bin/env python3
import base64
import json
import os
import re
import time
import urllib.error
import urllib.request
from collections import deque, defaultdict
from pathlib import Path

ROOT = Path('/root/deerflow-skill-hub-offline')
SRC = ROOT / 'data' / 'enterprise_offline_top60.json'
OUT_JSON = ROOT / 'data' / 'index_recursive_analysis.json'
OUT_MD = ROOT / 'reports' / 'index-recursive-analysis.md'

TOKEN = os.environ.get('GITHUB_TOKEN', '')
HEADERS = {
    'Accept': 'application/vnd.github+json',
    'User-Agent': 'deerflow-index-recursive-miner/1.0',
}
if TOKEN:
    HEADERS['Authorization'] = f'Bearer {TOKEN}'

INDEX_HINTS = [
    'awesome', 'curated', 'directory', 'marketplace', 'list of', 'collection', 'resources', 'toolkit'
]

GITHUB_REPO_PAT = re.compile(r'https://github[.]com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)')


def api_json(url: str):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode('utf-8', errors='replace'))


def repo_meta(repo: str):
    try:
        data = api_json(f'https://api.github.com/repos/{repo}')
        text = ' '.join([
            str(data.get('name', '')),
            str(data.get('description') or ''),
            ' '.join(data.get('topics') or []),
        ]).lower()
        is_index = any(h in text for h in INDEX_HINTS)
        return {
            'full_name': repo,
            'url': data.get('html_url', f'https://github.com/{repo}'),
            'stars': data.get('stargazers_count', 0),
            'updated_at': data.get('updated_at'),
            'license': (data.get('license') or {}).get('spdx_id', ''),
            'description': data.get('description') or '',
            'topics': data.get('topics') or [],
            'is_index_like': bool(is_index),
            'archived': bool(data.get('archived', False)),
            'default_branch': data.get('default_branch', 'main'),
        }
    except Exception:
        return {
            'full_name': repo,
            'url': f'https://github.com/{repo}',
            'stars': 0,
            'updated_at': None,
            'license': '',
            'description': '',
            'topics': [],
            'is_index_like': False,
            'archived': False,
            'default_branch': 'main',
        }


def readme_text(repo: str):
    # Try canonical README endpoint first
    try:
        data = api_json(f'https://api.github.com/repos/{repo}/readme')
        if data.get('encoding') == 'base64' and data.get('content'):
            raw = base64.b64decode(data['content']).decode('utf-8', errors='replace')
            return raw
    except Exception:
        # fallback: explicit path endpoint
        try:
            data = api_json(f'https://api.github.com/repos/{repo}/contents/README.md')
            if data.get('encoding') == 'base64' and data.get('content'):
                raw = base64.b64decode(data['content']).decode('utf-8', errors='replace')
                return raw
        except Exception:
            pass
    return ''


def is_index_like_name(repo: str) -> bool:
    text = repo.lower()
    return any(k in text for k in ['awesome', 'list', 'directory', 'marketplace', 'resources', 'toolkit', 'skills'])


def extract_repo_links(text: str):
    out = set()
    for m in GITHUB_REPO_PAT.findall(text or ''):
        repo = m.rstrip('/').rstrip('.git')
        if repo.count('/') == 1:
            owner, name = repo.split('/')
            if owner.lower() != 'topics' and name.lower() not in {'pull', 'issues', 'actions'}:
                out.add(f'{owner}/{name}')
    return sorted(out)


def analyze_root(root_repo: str, depth_limit: int = 2, max_nodes: int = 220):
    q = deque([(root_repo, 0)])
    seen = set()
    nodes = {}
    edges = defaultdict(list)

    while q and len(seen) < max_nodes:
        repo, d = q.popleft()
        if repo in seen:
            continue
        seen.add(repo)

        meta = repo_meta(repo)
        text = readme_text(repo)
        links = extract_repo_links(text)

        nodes[repo] = {
            **meta,
            'depth': d,
            'readme_link_count': len(links),
        }

        # outbound edges (all repos)
        for child in links:
            edges[repo].append(child)

        # recurse when current node is likely index-like and depth not exceeded
        if d < depth_limit and (meta['is_index_like'] or is_index_like_name(repo)):
            for child in links:
                if child not in seen:
                    q.append((child, d + 1))

        time.sleep(0.12)

    # enrich children nodes summary for edges already discovered but not visited
    for parent, chs in list(edges.items()):
        for c in chs:
            if c not in nodes:
                nodes[c] = {
                    'full_name': c,
                    'url': f'https://github.com/{c}',
                    'stars': 0,
                    'updated_at': None,
                    'license': '',
                    'description': '',
                    'topics': [],
                    'is_index_like': False,
                    'archived': False,
                    'default_branch': 'main',
                    'depth': nodes[parent]['depth'] + 1,
                    'readme_link_count': 0,
                }

    # root direct children stats
    direct = edges.get(root_repo, [])
    direct_ranked = sorted(direct, key=lambda r: nodes.get(r, {}).get('stars', 0), reverse=True)

    index_like_children = [r for r in direct if nodes.get(r, {}).get('is_index_like')]

    return {
        'root': root_repo,
        'depth_limit': depth_limit,
        'visited_node_count': len([k for k,v in nodes.items() if v.get('readme_link_count') or k == root_repo]),
        'discovered_node_count': len(nodes),
        'direct_child_count': len(direct),
        'direct_index_like_count': len(index_like_children),
        'direct_children_top_by_stars': direct_ranked[:40],
        'direct_index_like_children': sorted(index_like_children),
        'nodes': nodes,
        'edges': {k: v for k, v in edges.items()},
    }


def to_md(results):
    lines = []
    lines.append('# Top60 索引仓库递归分析')
    lines.append('')
    lines.append('分析对象: Top60 中标记为 `index` 的仓库')
    lines.append('递归策略: 读取 README 链接，若节点为索引类则继续下钻（默认深度 2）')
    lines.append('')

    for r in results:
        root = r['root']
        nodes = r['nodes']
        root_meta = nodes.get(root, {})
        lines.append(f'## {root}')
        lines.append(f"- stars: {root_meta.get('stars', 0)}")
        lines.append(f"- 直接外链仓库数: {r['direct_child_count']}")
        lines.append(f"- 直接外链中索引类: {r['direct_index_like_count']}")
        lines.append(f"- 递归访问节点数: {r['visited_node_count']}")
        lines.append(f"- 递归发现节点总数: {r['discovered_node_count']}")
        lines.append('')
        lines.append('### 作用判断')
        desc = root_meta.get('description') or ''
        lines.append(f'- 描述: {desc}')
        lines.append('- 判断: 该仓库属于“索引中枢”，应先做白名单筛选再导入，不建议整仓直接启用。')
        lines.append('')
        lines.append('### 直接外链（Top by stars）')
        for child in r['direct_children_top_by_stars'][:20]:
            m = nodes.get(child, {})
            lines.append(f"- {child} | stars={m.get('stars',0)} | index_like={m.get('is_index_like',False)} | license={m.get('license','') or 'Unknown'}")
        lines.append('')
        if r['direct_index_like_children']:
            lines.append('### 递归下钻候选（直接子节点中的索引类）')
            for child in r['direct_index_like_children'][:30]:
                m = nodes.get(child, {})
                lines.append(f"- {child} | stars={m.get('stars',0)}")
            lines.append('')

    return '\n'.join(lines) + '\n'


def main():
    data = json.loads(SRC.read_text(encoding='utf-8'))
    roots = [x['full_name'] for x in data if x.get('type') == 'index']

    results = []
    for i, root in enumerate(roots, start=1):
        print(f'[{i}/{len(roots)}] analyze {root}')
        results.append(analyze_root(root, depth_limit=2, max_nodes=220))

    OUT_JSON.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text(to_md(results), encoding='utf-8')

    print(f'roots={len(roots)}')
    print(f'json={OUT_JSON}')
    print(f'md={OUT_MD}')


if __name__ == '__main__':
    main()
