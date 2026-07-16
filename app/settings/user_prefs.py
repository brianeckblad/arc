"""Per-user shell preferences — stored in ``config/<os_username>/config.json``.

Preferences are personal (not shared with the team like ``settings/``) and now
live inside the same ``config.json`` as the rest of the per-user config, under a
top-level ``"preferences"`` block.  Earlier versions used a separate
``preferences.json``; it is migrated into ``config.json`` automatically on first
load and then removed.

Current keys:
    terminal_length   int   Lines per page for long help/docs output.
                            0 = paging disabled (default).
    terminal_width    int   Force a render width in columns. 0 = auto-detect.
    terminal_height   int   Force a render height. 0 = auto-detect.
    spinner           bool  Show the "querying SCM…" spinner during API calls.
    aliases           dict  User-defined command aliases.
    gui_theme         dict  Shared browser-GUI theme (both consoles).
    preferred_auth    str   Preferred SCM auth method: "service" | "user".
    scm_token_expiry  int   Deprecated — real token expiry now lives in auth.json
                            (SCMConfig.token_expiry). Retained only so older
                            config.json preference blocks still load.
"""

from __future__ import annotations

import json
import logging
from dataclasses import asdict, dataclass, field, fields
from pathlib import Path

from app.config import (
    CONFIG_DIR,
    CONFIG_FILE,
    _CONFIG_WRITE_LOCK,
    _read_config_file,
    _to_new_format,
    _write_config_file,
)

logger = logging.getLogger(__name__)

# Legacy standalone prefs file (migrated into config.json on first load).
_LEGACY_PREFS_FILE: Path = CONFIG_DIR / "preferences.json"


@dataclass
class UserPrefs:
    terminal_length: int = 0    # 0 = paging disabled
    terminal_width: int = 0     # 0 = auto-detect
    terminal_height: int = 0    # 0 = auto-detect (terminal height for rich tables)
    spinner: bool = True
    aliases: dict[str, str] = field(default_factory=dict)
    # Shared browser-GUI theme (both the feature editor and ARC console):
    # {"base": <name>, "overrides": {"--token": "#hex"}}.  Per-user only; never
    # affects the terminal shell theme (settings/theme.json).
    gui_theme: dict = field(default_factory=dict)
    # Preferred SCM auth method surfaced in the ARC console: "service" | "user".
    preferred_auth: str = "service"
    # Deprecated: the real token expiry now lives in auth.json
    # (SCMConfig.token_expiry). Kept so older config.json preference blocks that
    # still carry this key continue to load without error.
    scm_token_expiry: int = 0


_THEME_KEYS = ("gui_theme",)


def _coerce(prefs: "UserPrefs", raw: dict) -> "UserPrefs":
    """Populate *prefs* from a raw dict, tolerating bad/unknown values."""
    known = {f.name for f in fields(UserPrefs)}
    for key, value in raw.items():
        if key not in known:
            continue  # forward-compat: ignore keys from newer versions
        try:
            current = getattr(prefs, key)
            if isinstance(current, bool):
                setattr(prefs, key, bool(value))
            elif isinstance(current, int):
                setattr(prefs, key, max(0, int(value)))
            elif isinstance(current, dict):
                if not isinstance(value, dict):
                    continue
                if key in _THEME_KEYS:
                    # {"base": str, "overrides": {str: str}}; empty stays empty.
                    if not value:
                        setattr(prefs, key, {})
                    else:
                        ov = value.get("overrides", {})
                        setattr(prefs, key, {
                            "base": str(value.get("base", "")),
                            "overrides": ({str(k): str(v) for k, v in ov.items()}
                                          if isinstance(ov, dict) else {}),
                        })
                else:
                    setattr(prefs, key, {str(k): str(v) for k, v in value.items()})
            else:
                setattr(prefs, key, str(value) if value is not None else current)
        except (TypeError, ValueError):
            logger.debug("preferences: ignoring bad value for %s: %r", key, value)
    return prefs


def _migrate_legacy() -> dict | None:
    """Read a legacy preferences.json (if present) and return its dict, else None."""
    if not _LEGACY_PREFS_FILE.exists():
        return None
    try:
        data = json.loads(_LEGACY_PREFS_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else None
    except (OSError, json.JSONDecodeError):
        return None


def load_prefs() -> UserPrefs:
    """Read preferences from config.json (migrating a legacy preferences.json)."""
    raw = _to_new_format(_read_config_file())
    block = raw.get("preferences")
    if not isinstance(block, dict):
        block = None

    legacy = None
    if block is None:
        legacy = _migrate_legacy()

    prefs = UserPrefs()
    source = block if block is not None else (legacy or {})
    # Legacy theme keys → unified gui_theme (prefer arc console's theme).
    if "gui_theme" not in source:
        for old in ("arc_gui_theme", "feature_gui_theme"):
            if isinstance(source.get(old), dict) and source.get(old):
                source = {**source, "gui_theme": source[old]}
                break
    _coerce(prefs, source)

    # Persist the migration (write the preferences block, drop the legacy file).
    if block is None and (legacy is not None):
        save_prefs(prefs)
        try:
            _LEGACY_PREFS_FILE.unlink()
        except OSError:
            pass
    return prefs


def save_prefs(prefs: UserPrefs) -> bool:
    """Persist preferences into the config.json ``preferences`` block."""
    try:
        with _CONFIG_WRITE_LOCK:
            raw = _to_new_format(_read_config_file())
            raw["preferences"] = asdict(prefs)
            _write_config_file(raw)
        return True
    except OSError as exc:
        logger.debug("Could not write preferences to %s: %s", CONFIG_FILE, exc)
        return False
