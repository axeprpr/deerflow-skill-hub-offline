#!/usr/bin/env python3
import base64
import json
import os
import re
import time
import urllib.request
from pathlib import Path

ROOT = Path('/root/deerflow-skill-hub-offline')
SRC = ROOT / 'data' / 'enterprise_offline_top60.json'
OUT = ROOT / 'data' / 'enterprise_offline_top60_enriched.json'
TOKEN = os.environ.get('GITHUB_TOKEN','')

headers = {
    'Accept': 'application/vnd.github+json',
    'User-Agent': 'deerflow-skill-hub-enricher/1.0',
}
if TOKEN:
    headers['Authorization'] = f'Bearer {TOKEN}'

def get_json(url: str):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read().decode('utf-8', errors='replace'))

def clean_md(md: str) -> str:
    md = re.sub(r'```[\s\S]*?```', ' ', md)
    md = re.sub(r'`[^`]*`', ' ', md)
    md = re.sub(r'!\[[^\]]*\]\([^)]*\)', ' ', md)
    md = re.sub(r'\[[^\]]*\]\([^)]*\)', ' ', md)
    md = re.sub(r'^#+\s*', '', md, flags=re.M)
    md = re.sub(r'\s+', ' ', md)
    return md.strip()

def readme_snippet(repo_full: str) -> str:
    try:
        data = get_json(f'https://api.github.com/repos/{repo_full}/readme')
        content = data.get('content','')
        if data.get('encoding') == 'base64' and content:
            raw = base64.b64decode(content).decode('utf-8', errors='replace')
            c = clean_md(raw)
            return c[:900]
    except Exception:
        return ''
    return ''

def main():
    items = json.loads(SRC.read_text(encoding='utf-8'))
    out = []
    for i, it in enumerate(items, start=1):
        full = it['full_name']
        try:
            repo = get_json(f'https://api.github.com/repos/{full}')
        except Exception:
            repo = {}
        snippet = readme_snippet(full)
        out.append({
            **it,
            'repo_full': full,
            'forks': repo.get('forks_count'),
            'watchers': repo.get('subscribers_count'),
            'open_issues': repo.get('open_issues_count'),
            'size_kb': repo.get('size'),
            'homepage': repo.get('homepage') or '',
            'default_branch': repo.get('default_branch') or 'main',
            'topics_detail': repo.get('topics') or [],
            'readme_snippet': snippet,
        })
        if i % 10 == 0:
            print(f'enriched {i}/60')
        time.sleep(0.15)

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    print('written', OUT)

if __name__ == '__main__':
    main()
