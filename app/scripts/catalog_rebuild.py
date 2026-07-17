#!/usr/bin/env python3
"""Canonical catalog rebuild — the single source of truth for regenerating ARC's
generated code artifacts, command docs, and the offline browser bundle after a
spec or registry change.

Both entry points call THIS list, so they can never drift again:
  * ``app/scripts/docsupdate.py``          — runs it after pulling fresh specs.
  * the dev shell ``catalog rebuild``      — runs it offline (app/shell/configure.py).

Everything here is NETWORK-FREE: every generator reads already-mirrored files
on disk.  The network pulls (SCM specs + the PAN-OS CLI mirror) live in
``docsupdate.py`` and run *before* this.

Order matters — each stage may read a previous stage's output:
  1. resource catalog   pulled specs      → app/commands/resource_catalog.py
  2. PAN-OS catalog     mirrored CLI docs → app/commands/panos_catalog.py
  3. feature flags      both catalogs     → settings/features/
  4. field library      request schemas   → app/settings/field_catalog.py
  5. command structure  live registry     → settings/command-structure.json  (commandupdate)
  6. command docs       live registry     → docs/commands/
  7. API index          docs + registry   → app/scripts/API_INDEX.md
  8. code map           source tree       → app/scripts/CODE_MAP.md
  9. docs bundle        docs/*.md         → docs/docs-bundle.js  (arc cliup)

Run directly (``python app/scripts/catalog_rebuild.py``) or import ``rebuild()``.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

DEV_DIR = Path(__file__).resolve().parent      # app/scripts/
REPO_ROOT = DEV_DIR.parent.parent              # repo root

# The canonical ordered rebuild — (script filename in this dir, human label).
# commandupdate.py and generate_code_map.py were previously missing from the
# docsupdate path; arc cliup (the offline bundle) is appended after the scripts.
REBUILD_STEPS: list[tuple[str, str]] = [
    ("generate_resource_catalog.py", "resource catalog   → app/commands/resource_catalog.py"),
    ("generate_panos_catalog.py",    "PAN-OS catalog     → app/commands/panos_catalog.py"),
    ("generate_feature_flags.py",    "feature flags      → settings/features/"),
    ("generate_field_library.py",    "field library      → app/settings/field_catalog.py"),
    ("commandupdate.py",             "command structure  → settings/command-structure.json"),
    ("generate_command_docs.py",     "command docs       → docs/commands/"),
    ("generate_api_index.py",        "API index          → app/scripts/API_INDEX.md"),
    ("generate_code_map.py",         "code map           → app/scripts/CODE_MAP.md"),
]


def _rebuild_cliup(verbose: bool) -> bool:
    """Rebuild docs/docs-bundle.js so the offline browser portal matches the
    freshly generated command docs.  Best-effort; skips vendor downloads so the
    rebuild stays network-free (run ``arc cliup`` to refresh vendor JS/CSS)."""
    try:
        if str(REPO_ROOT) not in sys.path:
            sys.path.insert(0, str(REPO_ROOT))
        from app.cli import _do_cliup

        stats = _do_cliup(silent=not verbose, skip_vendor=True)
        if verbose:
            print(f"\n▶ docs bundle       → docs/docs-bundle.js "
                  f"({stats.get('bundled', '?')} pages, arc cliup)")
        return True
    except Exception as exc:  # noqa: BLE001 — cliup is best-effort, never fatal
        print(f"  [warn] docs bundle (cliup) not rebuilt: {exc}", file=sys.stderr)
        return False


def rebuild(*, verbose: bool = True, run_cliup: bool = True) -> bool:
    """Run every generator in order, then rebuild the offline docs bundle.

    Generators run as isolated subprocesses so a single failure is contained and
    reported rather than aborting the rest.  Returns True only if every step and
    the bundle succeeded.
    """
    ok = True
    for script, label in REBUILD_STEPS:
        path = DEV_DIR / script
        if not path.exists():
            print(f"  skip  {label}  (script not found: {script})", file=sys.stderr)
            ok = False
            continue
        if verbose:
            print(f"\n▶ {label}")
        proc = subprocess.run(
            [sys.executable, str(path)],
            cwd=str(REPO_ROOT),
            capture_output=not verbose,
            text=True,
        )
        if proc.returncode != 0:
            ok = False
            print(f"  [warn] {script} failed (exit {proc.returncode})", file=sys.stderr)
            if not verbose and proc.stderr:
                for line in proc.stderr.splitlines()[-5:]:
                    print(f"    {line}", file=sys.stderr)

    if run_cliup:
        ok = _rebuild_cliup(verbose) and ok

    return ok


def main() -> int:
    print("● catalog rebuild")
    return 0 if rebuild(verbose=True) else 1


if __name__ == "__main__":
    raise SystemExit(main())
