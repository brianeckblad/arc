"""Filesystem paths for ARC.

Single source of truth for where things live so loaders never hard-code paths.

Layout:
    <repo>/app/        core application code (this package)
    <repo>/settings/   USER-EDITABLE assets — banner, theme, features, structure
    <repo>/config/     per-user secrets (config.json) — never committed
    <repo>/docs/       documentation rendered by `help`

To customize ARC without touching code, edit files under ``settings/``.
"""

from __future__ import annotations

from pathlib import Path

# Repo root = parent of the app/ package.
REPO_ROOT = Path(__file__).resolve().parent.parent

# User-editable assets (committed; safe to hand-edit).
SETTINGS_DIR = REPO_ROOT / "settings"

BANNER_FILE   = SETTINGS_DIR / "banner.txt"
GOODBYE_FILE  = SETTINGS_DIR / "goodbye.txt"
THEME_FILE    = SETTINGS_DIR / "theme.json"
STRUCTURE_FILE = SETTINGS_DIR / "cli-structure.yaml"
FEATURES_FILE = SETTINGS_DIR / "features.json"

# Per-command argument structure that drives Tab completion and `?` help.
# Hand-editable; the CSV holds only the ORDER of each command's fields
# (object,field,field,...), with all field metadata resolved from the code-side
# field library.  A nested JSON form is read as a fallback when no CSV exists.
COMMAND_STRUCTURE_CSV  = SETTINGS_DIR / "command-structure.csv"
COMMAND_STRUCTURE_JSON = SETTINGS_DIR / "command-structure.json"

# Per-user secrets directory (config.json is written here, never committed).
CONFIG_DIR = REPO_ROOT / "config"

# Documentation root.
DOCS_DIR = REPO_ROOT / "docs"

# Per-command help docs (Markdown with YAML front-matter — the single source of
# truth for each command's description + usage shown by `?` and `help`).
COMMAND_DOCS_DIR = DOCS_DIR / "commands"

