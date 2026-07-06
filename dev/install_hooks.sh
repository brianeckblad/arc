#!/usr/bin/env bash
# Install ARC git hooks.
# Run once after cloning: bash dev/install_hooks.sh
set -e
REPO_ROOT="$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel)"
HOOKS_DIR="$REPO_ROOT/.git/hooks"

cat > "$HOOKS_DIR/pre-commit" << 'HOOK'
#!/usr/bin/env bash
# ARC pre-commit hook
# Bumps version to 0.1.<commit-count>, regenerates CODE_MAP.md, runs smoke tests.
set -e
REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

# ── Bump version: 0.1.<commit-count+1> ──────────────────────────────────────
COMMIT_COUNT=$(git rev-list --count HEAD 2>/dev/null || echo 0)
NEW_COUNT=$((COMMIT_COUNT + 1))
NEW_VERSION="0.1.${NEW_COUNT}"
INIT_FILE="app/__init__.py"
CURRENT=$(grep -o '"0\.[0-9]*\.[0-9]*"' "$INIT_FILE" | head -1 | tr -d '"')
if [ "$CURRENT" != "$NEW_VERSION" ]; then
    sed -i '' "s/__version__ = \".*\"/__version__ = \"${NEW_VERSION}\"/" "$INIT_FILE"
    git add "$INIT_FILE"
    echo "pre-commit: version bumped ${CURRENT} → ${NEW_VERSION}"
fi

# ── Regenerate CODE_MAP if any .py file under app/ changed ─────────────────
if git diff --cached --name-only | grep -q '^app/.*\.py$'; then
    echo "pre-commit: Python files changed — regenerating dev/CODE_MAP.md"
    uv run python dev/generate_code_map.py
    git add dev/CODE_MAP.md
fi

echo "pre-commit: running smoke sections 1,2,3 …"
uv run python dev/smoke_test.py --only 1,2,3
echo "pre-commit: OK"
HOOK

chmod +x "$HOOKS_DIR/pre-commit"
echo "✓ pre-commit hook installed at $HOOKS_DIR/pre-commit"

