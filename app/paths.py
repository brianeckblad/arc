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

# Feature flags live in a directory of small per-domain files (the glossary):
#   settings/features/scm-<spec>.json      one per pulled OpenAPI spec
#   settings/features/panos-ops.json       PAN-OS operational command families
#   settings/features/panos-config.json    PAN-OS config tree (break-glass)
#   settings/features/curated.json         hand-written command flags
#   settings/features/local.json           flags with no generated home
# FEATURES_FILE is the LEGACY single-file location — read for backward compat,
# absorbed and removed by dev/generate_feature_flags.py.
FEATURES_DIR  = SETTINGS_DIR / "features"
FEATURES_FILE = SETTINGS_DIR / "features.json"

# PAN-OS CLI docs pages pulled by dev/panosupdate.py — user-editable URL
# registry: add new "commands added/deleted in X" pages here.
PANOS_SOURCES_FILE = SETTINGS_DIR / "panos-sources.json"

# Per-command argument structure that drives Tab completion and `?` help.
# Hand-editable; the JSON holds only the ORDER of each command's fields
# ({"object": ["field", "field", ...]}), with all field metadata resolved from
# the code-side field library.
COMMAND_STRUCTURE_JSON = SETTINGS_DIR / "command-structure.json"

# CLI-generated command structure entries — written by `command-structure update`
# inside ARC (dev mode). Loaded between the hand-curated JSON and field_catalog;
# the hand file wins on collisions. Never edit by hand — use the CLI command.
COMMAND_STRUCTURE_GENERATED_JSON = SETTINGS_DIR / "command-structure-generated.json"

# System command aliases — shorthand input → canonical dispatch line.
# User-defined aliases live in config/<user>/preferences.json.
COMMAND_ALIASES_JSON = SETTINGS_DIR / "command-aliases.json"

# Application variables — referenced in banner.txt etc. with {{variable_name}} syntax.
APP_VARIABLES_JSON = SETTINGS_DIR / "app-variables.json"

# Per-user secrets directory (config.json is written here, never committed).
CONFIG_DIR = REPO_ROOT / "config"

# Documentation root.
DOCS_DIR = REPO_ROOT / "docs"

# Per-command help docs (Markdown with YAML front-matter — the single source of
# truth for each command's description + usage shown by `?` and `help`).
COMMAND_DOCS_DIR = DOCS_DIR / "commands"

