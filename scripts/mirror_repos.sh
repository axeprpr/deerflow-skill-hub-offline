#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SEED_FILE="${1:-$ROOT_DIR/data/seed_repos_top20.txt}"
MIRROR_DIR="${2:-$ROOT_DIR/mirrors}"

mkdir -p "$MIRROR_DIR"

if [[ ! -f "$SEED_FILE" ]]; then
  echo "seed file not found: $SEED_FILE" >&2
  exit 1
fi

while IFS= read -r url; do
  [[ -z "$url" ]] && continue
  repo="${url#https://github.com/}"
  target="$MIRROR_DIR/${repo//\//__}"

  if [[ -d "$target/.git" ]]; then
    echo "update $repo"
    git -C "$target" fetch --depth=1 origin
    default_branch="$(git -C "$target" symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@' || echo main)"
    git -C "$target" checkout -q "$default_branch" || true
    git -C "$target" pull --ff-only origin "$default_branch" || true
  else
    echo "clone $repo"
    git clone --depth=1 "$url" "$target"
  fi
done < "$SEED_FILE"

echo "mirrored repos in $MIRROR_DIR"
