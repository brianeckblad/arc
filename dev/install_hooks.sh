#!/usr/bin/env bash
# Install ARC git hooks.
# Run once after cloning: bash dev/install_hooks.sh
set -e
REPO_ROOT="$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel)"
HOOKS_DIR="$REPO_ROOT/.git/hooks"

cat > "$HOOKS_DIR/pre-commit" << 'HOOK'
#!/usr/bin/env bash
# ARC pre-commit hook — regenerates CODE_MAP and runs fast smoke tests.
set -e
REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

if git diff --cached --name-only | grep -q '^app/.*\.py$'; then
    echo "pre-commit: Python files changed — regenerating dev/CODE_MAP.md"
    python dev/gen_code_map.py
    git add dev/CODE_MAP.md
fi

echo "pre-commit: running smoke sections 1,2,3 …"
python dev/smoke_test.py --only 1,2,3
echo "pre-commit: OK"
HOOK

chmod +x "$HOOKS_DIR/pre-commit"
echo "✓ pre-commit hook installed at $HOOKS_DIR/pre-commit"

