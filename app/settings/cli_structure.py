"""Loader for settings/cli-structure.yaml — the user-editable CLI customization file.

Reading from this file lets operators change how the ARC CLI looks (labels,
descriptions, help text, configure banner) without editing Python code.

The file is optional. All functions return sensible hard-coded defaults when
the YAML file is missing or malformed, so the shell always starts cleanly.
"""

from __future__ import annotations

import logging
from typing import Any

from app.paths import STRUCTURE_FILE as _STRUCTURE_FILE

logger = logging.getLogger(__name__)


# Module-level cache — loaded once per session.
_cache: dict[str, Any] | None = None


def _load() -> dict[str, Any]:
    """Return the parsed YAML structure, or an empty dict on failure."""
    global _cache
    if _cache is not None:
        return _cache

    if not _STRUCTURE_FILE.exists():
        _cache = {}
        return _cache

    try:
        import yaml  # PyYAML (dev extra — may be absent in minimal installs)
        raw = _STRUCTURE_FILE.read_text(encoding="utf-8")
        parsed = yaml.safe_load(raw) or {}
        if not isinstance(parsed, dict):
            logger.warning("cli-structure.yaml: top-level value is not a mapping — ignored")
            _cache = {}
        else:
            _cache = parsed
    except ImportError:
        # PyYAML not installed.  The file exists but we can't parse it.
        # Fail silently so the shell starts without YAML being a hard dependency.
        logger.debug("PyYAML not available — cli-structure.yaml not loaded (run: uv pip install pyyaml)")
        _cache = {}
    except Exception as exc:  # noqa: BLE001
        logger.warning("cli-structure.yaml: parse error — %s", exc)
        _cache = {}

    return _cache


def invalidate_cache() -> None:
    """Force a re-read on next access (called by `cli reload` if ever added)."""
    global _cache
    _cache = None


# ── Public accessors ────────────────────────────────────────────────────────

# Default verb-group metadata used when cli-structure.yaml is absent.
_DEFAULT_VERB_GROUPS: dict[str, dict[str, str]] = {
    "show":    {"visible": "true", "description": "Show configuration and status",            "hint": "type 'show ?' for sub-commands"},
    "set":     {"visible": "true", "description": "Create or modify configuration",           "hint": "configure mode — type 'set ?' for sub-commands"},
    "commit":  {"visible": "true", "description": "Push candidate config to managed devices", "hint": ""},
    "test":    {"visible": "hidden","description": "Test policy and connectivity",            "hint": "type 'test ?' for sub-commands"},
    "ping":    {"visible": "true", "description": "Ping a host from a managed device",        "hint": "use --remote or connect first"},
    "request": {"visible": "true", "description": "Request system operations",               "hint": "type 'request ?' for sub-commands"},
    "delete":  {"visible": "true", "description": "Remove configuration objects",             "hint": "configure mode — type 'delete ?' for sub-commands"},
}

# Maps raw visible values to canonical states (same semantics as builtin commands).
_VERB_VIS_ON     = "true"
_VERB_VIS_HIDDEN = "hidden"
_VERB_VIS_DEV    = "dev"
_VERB_VIS_OFF    = "false"


def _coerce_verb_visible(raw: object) -> str:
    """Normalise a verb visible value to a canonical state string."""
    if raw is True or raw is None:        # default: visible
        return _VERB_VIS_ON
    if raw is False:
        return _VERB_VIS_OFF
    token = str(raw).strip().lower()
    if token in ("true", "on", "1", "yes", "visible"):
        return _VERB_VIS_ON
    if token in ("hidden", "invisible"):
        return _VERB_VIS_HIDDEN
    if token in ("dev", "development", "wip"):
        return _VERB_VIS_DEV
    if token in ("false", "off", "0", "no", "blocked"):
        return _VERB_VIS_OFF
    return _VERB_VIS_ON


def verb_description(verb: str, count: int) -> str:
    """Return the description string for *verb* in bare ? output.

    Falls back to a generated string when the verb is not in the config.
    """
    data = _load()
    groups: dict = data.get("verb_groups") or {}
    entry = groups.get(verb) or _DEFAULT_VERB_GROUPS.get(verb)
    if entry:
        desc = entry.get("description", "")
        hint = entry.get("hint", "")
        if hint:
            return f"{desc}  ({hint})" if desc else hint
        return desc
    # Fallback for unknown verbs.
    return f"({count} sub-command{'s' if count != 1 else ''} — type '{verb} ?' to expand)"


def verb_visible(verb: str, dev_mode: bool = False) -> bool:
    """Return True when *verb* should appear as a top-level entry in bare ? output.

    Dev mode reveals hidden/dev verbs but never false/blocked ones.
    """
    data = _load()
    groups: dict = data.get("verb_groups") or {}
    entry = groups.get(verb) or _DEFAULT_VERB_GROUPS.get(verb)
    raw = entry.get("visible", True) if isinstance(entry, dict) else True
    state = _coerce_verb_visible(raw)
    if state == _VERB_VIS_OFF:
        return False
    if state == _VERB_VIS_ON:
        return True
    # _VERB_VIS_HIDDEN and _VERB_VIS_DEV — visible only in dev mode
    return dev_mode


def section_label(key: str, default: str) -> str:
    """Return a section header label from the config."""
    data = _load()
    sections: dict = data.get("sections") or {}
    return str(sections.get(key, default))


def help_footer() -> str:
    """Return the footer hint line shown at the bottom of bare ? output."""
    data = _load()
    return str(data.get("help_footer", "show ?  → sub-commands  |  <cmd> help  → full docs  |  help all  → complete reference"))


def configure_banner() -> str:
    """Return the text shown when entering configure mode."""
    data = _load()
    raw = data.get("configure_banner", "")
    if raw:
        return str(raw).strip()
    return "Entered configure mode.  Use 'set' to create objects, 'exit' to leave.\n  set ? → create operations  |  show ? → read configuration  |  exit → leave configure mode"


def cd_hint(event: str, name: str = "") -> str:
    """Return the feedback message for a cd navigation event.

    event: 'device' | 'folder' | 'clear'
    """
    _defaults = {
        "device": "API context → {name}.  Use 'connect' to open an SSH session.",
        "folder": "SCM folder scope → {name}.",
        "clear":  "Context cleared.  Back at global scope.",
    }
    data = _load()
    hints: dict = data.get("cd_hints") or {}
    template = str(hints.get(event, _defaults.get(event, "")))
    return template.replace("{name}", name)

