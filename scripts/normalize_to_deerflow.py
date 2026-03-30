#!/usr/bin/env python3
import argparse
import re
from pathlib import Path


def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = re.sub(r'-+', '-', s).strip('-')
    return s or 'skill'


def first_heading(text: str) -> str:
    for line in text.splitlines():
        line = line.strip()
        if line.startswith('#'):
            return line.lstrip('#').strip()
    return ''


def pick_candidates(repo_root: Path) -> list[Path]:
    candidates = []
    for p in repo_root.rglob('*.md'):
        rel = p.relative_to(repo_root).as_posix().lower()
        name = p.name.lower()
        if '/.git/' in f'/{rel}/':
            continue
        if name == 'skill.md':
            candidates.append(p)
            continue
        if any(k in rel for k in ['/skills/', '/skill/', '/rules/', '/prompts/']):
            candidates.append(p)

    # prioritize direct SKILL.md files, then path depth
    candidates.sort(key=lambda p: (p.name.lower() != 'skill.md', len(p.relative_to(repo_root).parts)))

    out = []
    seen = set()
    for p in candidates:
        rel = p.relative_to(repo_root).as_posix()
        # skip README noise in root
        if rel.lower() in {'readme.md', 'readme_cn.md'}:
            continue
        key = rel.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(p)
        if len(out) >= 30:
            break
    return out


def make_skill(repo_slug: str, repo_url: str, src_path: Path, repo_root: Path, out_root: Path):
    rel = src_path.relative_to(repo_root).as_posix()
    raw = src_path.read_text(encoding='utf-8', errors='replace')
    h = first_heading(raw)

    base = h or src_path.stem
    skill_name = slugify(f'{repo_slug}-{base}')[:64].strip('-')
    if len(skill_name) < 3:
        skill_name = f'{repo_slug}-skill'[:64]

    skill_dir = out_root / skill_name
    refs = skill_dir / 'references'
    refs.mkdir(parents=True, exist_ok=True)

    (refs / 'source.md').write_text(raw, encoding='utf-8')

    description = f'Adapted offline skill from {repo_slug} ({rel}).'
    fm = (
        '---\n'
        f'name: {skill_name}\n'
        f'description: "{description}"\n'
        'author: deerflow-skill-hub\n'
        'version: 0.1.0\n'
        'compatibility: deerflow\n'
        'license: see-source-repo\n'
        '---\n\n'
    )
    body = (
        '# Adapted Skill\n\n'
        f'- Source repository: {repo_url}\n'
        f'- Source file: `{rel}`\n\n'
        '## Usage\n\n'
        'Use this skill by following the instructions in `references/source.md`. '
        'When conflicts occur, prioritize your local policy and system/developer instructions.\n'
    )
    (skill_dir / 'SKILL.md').write_text(fm + body, encoding='utf-8')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mirrors', default='/root/deerflow-skill-hub-offline/mirrors')
    ap.add_argument('--out', default='/root/deerflow-skill-hub-offline/output/skills/custom')
    args = ap.parse_args()

    mirrors = Path(args.mirrors)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    repo_count = 0
    skill_count = 0

    for repo_dir in sorted(mirrors.iterdir()):
        if not repo_dir.is_dir():
            continue
        repo_slug = repo_dir.name.replace('__', '-')
        repo_url = 'https://github.com/' + repo_dir.name.replace('__', '/')

        candidates = pick_candidates(repo_dir)
        if not candidates:
            continue

        repo_count += 1
        for p in candidates:
            make_skill(repo_slug, repo_url, p, repo_dir, out)
            skill_count += 1

    print(f'repos_with_candidates={repo_count}')
    print(f'generated_skills={skill_count}')


if __name__ == '__main__':
    main()
