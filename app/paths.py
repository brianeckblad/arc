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

# Per-user secrets directory (config.json is written here, never committed).
CONFIG_DIR = REPO_ROOT / "config"

# Documentation root.
DOCS_DIR = REPO_ROOT / "docs"

