
#!/bin/bash
set -e

cd "$(dirname "$0")"

git add -A

if git diff --cached --quiet; then
    exit 0
fi

git commit -m "Auto update: $(date '+%Y-%m-%d %H:%M:%S')"

git push origin HEAD
