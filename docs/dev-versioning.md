# Local Auto-Versioning Setup

ARC uses a simple **local-only** git pre-commit hook to keep the version
number in sync with your commit history.  The hook is never pushed to GitHub
— it lives on your machine only, which keeps the repo clean while still giving
every commit a meaningful version number.

## How it works

| What | Detail |
|------|--------|
| **Format** | `0.1.<N>` — patch number = total commit count |
| **Source of truth** | `app/__init__.py` → `__version__` |
| **Also updated** | `pyproject.toml` → `version` |
| **When** | The hook runs automatically before every `git commit` |
| **Visible in ARC** | Printed on the `✓ SCM connected` startup line |

Example startup line after setup:

```
✓ SCM connected  (profile: default  |  TSG: 1851678086)  — Version: 0.1.14
Loaded: 22 device(s), 68 folder(s), 5 TSG(s)
```

---

## One-time setup

**1. Create the hooks directory and hook file:**

```bash
mkdir -p .githooks
```

Then create `.githooks/pre-commit` with the content below.

**2. Make it executable:**

```bash
chmod +x .githooks/pre-commit
```

**3. Tell git to use it:**

```bash
git config core.hooksPath .githooks
```

That's it — every subsequent `git commit` will auto-bump the version.

---

## Hook content

Create `.githooks/pre-commit` with exactly this content:

```bash
#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# ARC pre-commit hook — auto-bump version on every commit.
#
# Format: 0.1.<N>  where N = total commit count after this commit lands.
#
# Files updated:
#   app/__init__.py  — runtime __version__ (read by the shell at startup)
#   pyproject.toml   — package version (kept in sync for pip/uv installs)
#
# Install once per clone:
#   git config core.hooksPath .githooks
# ---------------------------------------------------------------------------
set -e

COUNT=$(git rev-list --count HEAD 2>/dev/null || echo 0)
NEXT=$((COUNT + 1))
VERSION="0.1.${NEXT}"

# Update app/__init__.py
python3 - "$VERSION" << 'PYEOF'
import re, sys
path = "app/__init__.py"
txt  = open(path).read()
new  = re.sub(r'__version__\s*=\s*"[^"]+"', f'__version__ = "{sys.argv[1]}"', txt)
open(path, "w").write(new)
PYEOF

# Update pyproject.toml (first version = line only, not dependency specs)
python3 - "$VERSION" << 'PYEOF'
import re, sys
path = "pyproject.toml"
txt  = open(path).read()
new  = re.sub(r'^version\s*=\s*"[^"]+"', f'version = "{sys.argv[1]}"', txt, count=1, flags=re.MULTILINE)
open(path, "w").write(new)
PYEOF

git add app/__init__.py pyproject.toml
echo "[arc] version bumped to ${VERSION}"
```

---

## Verify it is working

After setup, make any change and commit:

```bash
git commit -m "test: verify version hook"
# Expected output includes:
# [arc] version bumped to 0.1.XX
```

Then confirm the runtime version:

```bash
python3 -c "from app import __version__; print(__version__)"
# 0.1.XX
```

---

## Disabling

To stop auto-versioning, remove the hook path config:

```bash
git config --unset core.hooksPath
```

The hook file stays on disk but is no longer active.  Re-enable at any time by
re-running the `git config` command above.

---

## Why local-only?

The hook is excluded from the repo via `.gitignore` (`.githooks/` is listed
there).  This is intentional:

- **No side-effects for contributors** who clone without setting up the hook — their commits still work normally, version just does not auto-bump.
- **No CI surprises** — automated pipelines don't have unexpected version mutations.
- **Simple to opt in** — one `git config` line, as documented above.

