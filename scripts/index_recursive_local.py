#!/usr/bin/env python3
import base64
import json
import os
import re
import subprocess
import urllib.request
from pathlib import Path

ROOT = Path('/root/deerflow-skill-hub-offline')
INDEX_ROOTS_DIR = Path('/root/github-repos/index-roots')
SRC = ROOT / 'data' / 'enterprise_offline_top60.json'
OUT_JSON = ROOT / 'data' / 'index_recursive_local.json'
OUT_MD = ROOT / 'reports' / 'index-recursive-analysis.md'

TOKEN = os.environ.get('GITHUB_TOKEN', '')
HEADERS = {
    'Accept': 'application/vnd.github+json',
    'User-Agent': 'deerflow-index-recursive-local/1.0',
}
if TOKEN:
    HEADERS['Authorization'] = f'Bearer {TOKEN}'

REPO_PAT = re.compile(r'https://github[.]com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)')


def is_index_like(repo: str) -> bool:
    s = repo.lower()
    return any(k in s for k in ['awesome', 'list', 'directory', 'marketplace', 'resources', 'toolkit'])


def extract_links(text: str):
    out = set()
    for m in REPO_PAT.findall(text or ''):
        repo = m.rstrip('/').rstrip('.git')
        if repo.count('/') == 1:
            owner, name = repo.split('/')
            if owner.lower() != 'topics' and name.lower() not in {'pull', 'issues', 'actions'}:
                out.add(repo)
    return sorted(out)


def local_readme(repo: str) -> str:
    d = INDEX_ROOTS_DIR / repo.replace('/', '__')
    for cand in ['README.md', 'readme.md', 'README.MD']:
        p = d / cand
        if p.exists():
            return p.read_text(encoding='utf-8', errors='replace')
    return ''


def remote_readme(repo: str) -> str:
    try:
        req = urllib.request.Request(f'https://api.github.com/repos/{repo}/readme', headers=HEADERS)
        with urllib.request.urlopen(req, timeout=12) as r:
            data = json.loads(r.read().decode('utf-8', errors='replace'))
        if data.get('encoding') == 'base64' and data.get('content'):
            return base64.b64decode(data['content']).decode('utf-8', errors='replace')
    except Exception:
        return ''
    return ''


def gh_stars(repo: str) -> int:
    try:
        req = urllib.request.Request(f'https://api.github.com/repos/{repo}', headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode('utf-8', errors='replace'))
        return int(data.get('stargazers_count') or 0)
    except Exception:
        return 0


def main():
    roots = [x['full_name'] for x in json.loads(SRC.read_text(encoding='utf-8')) if x.get('type') == 'index']

    results = []
    for root in roots:
        t = local_readme(root)
        direct = extract_links(t)
        direct = [r for r in direct if r != root]

        direct_meta = []
        for r in direct:
            direct_meta.append({
                'repo': r,
                'stars': gh_stars(r),
                'is_index_like': is_index_like(r),
            })
        direct_meta.sort(key=lambda x: x['stars'], reverse=True)

        index_children = [x['repo'] for x in direct_meta if x['is_index_like']][:20]

        second = []
        for child in index_children:
            rt = remote_readme(child)
            child_links = extract_links(rt)
            child_links = [x for x in child_links if x != child]
            second.append({
                'repo': child,
                'stars': gh_stars(child),
                'second_level_link_count': len(child_links),
                'second_level_index_like_count': len([x for x in child_links if is_index_like(x)]),
                'second_level_top': child_links[:30],
            })

        results.append({
            'root': root,
            'direct_link_count': len(direct),
            'direct_index_like_count': len(index_children),
            'direct_top': direct_meta[:30],
            'index_children_second_level': second,
        })

    OUT_JSON.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')

    lines = []
    lines.append('# Top60 索引仓库递归分析（本地+二级递归）')
    lines.append('')
    lines.append('说明：先解析根仓库本地 README 外链，再对索引型子仓库读取远端 README 做二级递归。')
    lines.append('')

    for r in results:
        lines.append(f"## {r['root']}")
        lines.append(f"- 直接外链仓库数: {r['direct_link_count']}")
        lines.append(f"- 直接外链中索引型: {r['direct_index_like_count']}")
        lines.append('- 直接外链 Top:')
        for x in r['direct_top'][:20]:
            lines.append(f"  - {x['repo']} | stars={x['stars']} | index_like={x['is_index_like']}")
        if r['index_children_second_level']:
            lines.append('- 二级递归（索引子仓库）:')
            for c in r['index_children_second_level'][:12]:
                lines.append(f"  - {c['repo']} | second_links={c['second_level_link_count']} | second_index={c['second_level_index_like_count']}")
        lines.append('')

    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')

    print('roots', len(results))
    print('json', OUT_JSON)
    print('md', OUT_MD)


if __name__ == '__main__':
    main()
