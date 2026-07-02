"""Per-user shell preferences — ``config/<os_username>/preferences.json``.

Unlike ``settings/`` (repo-committed, shared by the whole team), preferences
are personal and live next to the user's credentials file. They are loaded at
every shell launch and written whenever a ``terminal …`` command changes one.

Current keys:
    terminal_length   int   Lines per page for long help/docs output.
                            0 = paging disabled (default — full output,
                            use your terminal's scrollback). `terminal length 24`
                            gives the classic vendor-CLI pager.
    terminal_width    int   Force a render width in columns. 0 = auto-detect
                            from the terminal (default).
    spinner           bool  Show the "querying SCM…" spinner during API calls.
    aliases           dict  User-defined command aliases (`alias <name> <expansion>`).
                            Expanded once per input line — never recursively.

Room to grow (add a field + a `terminal`/future subcommand, nothing else):
output format defaults, confirmation prompts, history size.
"""

from __future__ import annotations

import json
import logging
from dataclasses import asdict, dataclass, field, fields
from pathlib import Path

from app.config import CONFIG_DIR

logger = logging.getLogger(__name__)

PREFS_FILE: Path = CONFIG_DIR / "preferences.json"


@dataclass
class UserPrefs:
    terminal_length: int = 0    # 0 = paging disabled
    terminal_width: int = 0     # 0 = auto-detect
    spinner: bool = True
    aliases: dict[str, str] = field(default_factory=dict)


def load_prefs() -> UserPrefs:
    """Read preferences.json, tolerating a missing or malformed file."""
    try:
        raw = json.loads(PREFS_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return UserPrefs()
    if not isinstance(raw, dict):
        return UserPrefs()
    known = {f.name: f.type for f in fields(UserPrefs)}
    prefs = UserPrefs()
    for key, value in raw.items():
        if key not in known:
            continue  # forward-compat: ignore keys from newer versions
        try:
            if isinstance(getattr(prefs, key), bool):
                setattr(prefs, key, bool(value))
            elif isinstance(getattr(prefs, key), int):
                setattr(prefs, key, max(0, int(value)))
            elif isinstance(getattr(prefs, key), dict):
                if isinstance(value, dict):
                    setattr(prefs, key, {str(k): str(v) for k, v in value.items()})
                else:
                    logger.debug("preferences.json: %s must be an object, got %r", key, value)
            else:
                setattr(prefs, key, value)
        except (TypeError, ValueError):
            logger.debug("preferences.json: ignoring bad value for %s: %r", key, value)
    return prefs


def save_prefs(prefs: UserPrefs) -> bool:
    """Persist preferences; returns False (with a debug log) on failure."""
    try:
        PREFS_FILE.parent.mkdir(parents=True, exist_ok=True)
        PREFS_FILE.write_text(json.dumps(asdict(prefs), indent=2) + "\n", encoding="utf-8")
        return True
    except OSError as exc:
        logger.debug("Could not write %s: %s", PREFS_FILE, exc)
        return False
