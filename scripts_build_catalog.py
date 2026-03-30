#!/usr/bin/env python3
import csv
import json
import re
from pathlib import Path

ROOT = Path('/root/deerflow-skill-hub-offline')
RAW_DIR = ROOT / 'data' / 'raw'
OUT_DIR = ROOT / 'data'
OUT_DIR.mkdir(parents=True, exist_ok=True)

SKILL_HINTS = [
    'skill', 'skills', 'claude code', 'codex', 'agent', 'subagent', 'cursor rules', 'windsurf', 'prompt'
]
HIGH_COMPAT_HINTS = [
    'claude code skill', 'codex skill', 'agent skills', 'skill library', 'skillset', 'skill pack', 'skills for'
]
LOW_OFFLINE_HINTS = ['saas', 'hosted', 'cloud', 'managed service']


def infer_env(language: str, text: str) -> str:
    lang = (language or '').lower()
    text = text.lower()
    env = []
    if lang in {'javascript', 'typescript'} or any(k in text for k in ['npm', 'node', 'pnpm']):
        env.append('Node.js')
    if lang == 'python' or 'python' in text or 'pip' in text:
        env.append('Python')
    if lang == 'go' or 'golang' in text:
        env.append('Go')
    if lang == 'rust' or 'cargo' in text:
        env.append('Rust')
    if not env:
        return 'None (Markdown/Config-only or unknown)'
    return ', '.join(sorted(set(env)))


def classify(name: str, desc: str, topics: list[str]):
    text = ' '.join([name or '', desc or '', ' '.join(topics or [])]).lower()

    deerflow = 'low'
    if any(h in text for h in HIGH_COMPAT_HINTS):
        deerflow = 'high'
    elif any(h in text for h in ['claude code', 'codex', 'agent', 'skills']):
        deerflow = 'medium'

    offline = 'medium'
    if any(h in text for h in LOW_OFFLINE_HINTS):
        offline = 'low'
    elif any(h in text for h in ['markdown', 'prompt', 'rules', 'local-first', 'offline', 'config']):
        offline = 'high'

    rtype = 'collection'
    if any(h in text for h in ['awesome', 'directory', 'marketplace']):
        rtype = 'index'
    if any(h in text for h in ['plugin', 'mcp', 'server', 'desktop app']):
        rtype = 'tooling'

    return deerflow, offline, rtype


def main():
    repos = {}
    for p in sorted(RAW_DIR.glob('*.json')):
        data = json.loads(p.read_text(encoding='utf-8'))
        for item in data.get('items', []):
            full_name = item.get('full_name')
            if not full_name:
                continue
            text = f"{item.get('name','')} {item.get('description') or ''}".lower()
            if not any(k in text for k in SKILL_HINTS):
                continue
            old = repos.get(full_name)
            if old is None or item.get('stargazers_count', 0) > old.get('stargazers_count', 0):
                repos[full_name] = item

    ranked = sorted(repos.values(), key=lambda x: x.get('stargazers_count', 0), reverse=True)
    ranked = [r for r in ranked if not r.get('archived', False)]
    ranked = ranked[:180]

    out = []
    for idx, r in enumerate(ranked, start=1):
        name = r.get('name') or ''
        desc = r.get('description') or ''
        topics = r.get('topics') or []
        language = r.get('language') or ''
        deerflow, offline, rtype = classify(name, desc, topics)
        env_summary = infer_env(language, f"{desc} {' '.join(topics)}")

        out.append({
            'rank': idx,
            'full_name': r.get('full_name'),
            'url': r.get('html_url'),
            'stars': int(r.get('stargazers_count') or 0),
            'updated_at': r.get('updated_at'),
            'language': language,
            'license': ((r.get('license') or {}).get('spdx_id') or ''),
            'topics': topics,
            'description': desc,
            'deerflow_compat': deerflow,
            'offline_readiness': offline,
            'type': rtype,
            'environment_dependencies': env_summary,
        })

    out.sort(key=lambda x: x['stars'], reverse=True)
    for i, row in enumerate(out, start=1):
        row['rank'] = i

    (OUT_DIR / 'catalog.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')

    with (OUT_DIR / 'catalog.csv').open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow([
            'rank', 'full_name', 'stars', 'url', 'updated_at', 'language', 'license',
            'deerflow_compat', 'offline_readiness', 'type', 'environment_dependencies', 'description'
        ])
        for r in out:
            w.writerow([
                r['rank'], r['full_name'], r['stars'], r['url'], r['updated_at'], r['language'], r['license'],
                r['deerflow_compat'], r['offline_readiness'], r['type'], r['environment_dependencies'], r['description']
            ])

    shortlist = [
        r for r in out
        if r['deerflow_compat'] in ('high', 'medium')
        and r['offline_readiness'] in ('high', 'medium')
        and r['stars'] >= 700
    ]
    (OUT_DIR / 'shortlist.json').write_text(json.dumps(shortlist, ensure_ascii=False, indent=2), encoding='utf-8')

    # enterprise offline first
    enterprise = [
        r for r in shortlist
        if r['type'] in ('collection', 'index')
        and ('None' in r['environment_dependencies'] or 'Python' in r['environment_dependencies'] or 'Node.js' in r['environment_dependencies'])
    ][:60]
    (OUT_DIR / 'enterprise_offline_top60.json').write_text(json.dumps(enterprise, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f'total_unique={len(out)}')
    print(f'shortlist={len(shortlist)}')
    print(f'enterprise_top60={len(enterprise)}')

if __name__ == '__main__':
    main()
