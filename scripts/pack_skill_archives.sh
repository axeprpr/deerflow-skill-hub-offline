#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="${1:-$ROOT_DIR/output/skills/custom}"
DIST_DIR="${2:-$ROOT_DIR/dist}"

mkdir -p "$DIST_DIR"

if [[ ! -d "$SKILLS_DIR" ]]; then
  echo "skills dir not found: $SKILLS_DIR" >&2
  exit 1
fi

count=0
for d in "$SKILLS_DIR"/*; do
  [[ -d "$d" ]] || continue
  name="$(basename "$d")"
  out="$DIST_DIR/${name}.skill"
  (
    cd "$d"
    zip -qr "$out" .
  )
  count=$((count+1))
done

echo "packed $count .skill archives into $DIST_DIR"
