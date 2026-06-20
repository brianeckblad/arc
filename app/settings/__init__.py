"""Loaders for the user-editable ``settings/`` directory.

Each module here reads one file under the repo-root ``settings/`` folder and
turns it into Python the rest of ARC can use. Nothing here owns the data — the
``settings/*.json`` / ``settings/*.yaml`` files are the source of truth; these
modules are just the readers.

| Module | Reads | Purpose |
|--------|-------|---------|
| ``theme`` | ``settings/theme.json`` | CLI colour roles (``ArcTheme``) |
| ``features`` | ``settings/features.json`` | command on/off flags |
| ``cli_structure`` | ``settings/cli-structure.yaml`` | verb labels, help text, banners |
| ``command_help`` | ``docs/commands/*.md`` front-matter | per-command description + usage |

Import from the submodules (``from app.settings.theme import ArcTheme``) or use
the convenience re-exports below.
"""

from __future__ import annotations

from app.settings.cli_structure import (
    cd_hint,
    configure_banner,
    help_footer,
    invalidate_cache,
    section_label,
    verb_description,
)
from app.settings.command_help import (
    apply_overrides,
    description_overrides,
    usage_overrides,
)
from app.settings.features import (
    FeatureMap,
    dev_mode_from_env,
    feature_state,
    is_enabled,
    load_features,
)
from app.settings.theme import (
    THEME_KEYS,
    ArcTheme,
    load_theme,
    reset_theme,
    save_theme,
)

__all__ = [
    # theme
    "ArcTheme",
    "THEME_KEYS",
    "load_theme",
    "save_theme",
    "reset_theme",
    # features
    "FeatureMap",
    "load_features",
    "is_enabled",
    "feature_state",
    "dev_mode_from_env",
    # cli_structure
    "verb_description",
    "section_label",
    "help_footer",
    "configure_banner",
    "cd_hint",
    "invalidate_cache",
    # command_help
    "description_overrides",
    "usage_overrides",
    "apply_overrides",
]

