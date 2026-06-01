"""ARC CLI theme — controls colours used throughout the interactive shell.

All colour values are Rich markup style strings, e.g. ``"cyan"``,
``"bold yellow"``, ``"dim"``.  An empty string means no styling (plain text).

The active theme is stored in ``app/cli_theme.json``.  Edit that file
directly or use the ``conf color <key> <style>`` shell command.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

_THEME_FILE = Path(__file__).parent / "cli_theme.json"


@dataclass
class ArcTheme:
    """One field per named colour role in the ARC CLI.

    Change any value to a Rich style string to retheme that element.
    Run ``conf reset`` in the shell to restore all defaults.
    """

    # ? inline help — command names
    command_name: str = "cyan"
    # ? inline help — section headers (GLOBAL / FOLDER / DEVICE / SHELL)
    section_header: str = "bold yellow"
    # ? inline help — DEVICE section when no device is selected (locked)
    section_header_locked: str = "dim bold"
    # ? inline help — description text beside command names
    description: str = ""
    # ? inline help — dim/secondary text (context annotations, hints)
    description_dim: str = "dim"
    # banner — the startup logo block
    banner_logo: str = "bold cyan"
    # banner — the subtitle / legal line(s) below the logo
    banner_subtitle: str = "dim"


# The baseline defaults.  reset_theme() restores these.
_DEFAULT = ArcTheme()

# Friendly display names shown in ``conf show`` output.
THEME_KEYS: dict[str, str] = {
    "command_name":          "Command names in ? help",
    "section_header":        "Section headers  (GLOBAL / FOLDER / DEVICE / SHELL)",
    "section_header_locked": "Locked DEVICE section header",
    "description":           "Description text beside commands",
    "description_dim":       "Dim/secondary text and context annotations",
    "banner_logo":           "Startup logo colour",
    "banner_subtitle":       "Startup subtitle / legal text colour",
}


def load_theme() -> ArcTheme:
    """Read cli_theme.json; return defaults if the file is missing or invalid."""
    try:
        raw = json.loads(_THEME_FILE.read_text(encoding="utf-8"))
        # Only accept known keys; ignore unknown ones so old files don't crash.
        known = {k: v for k, v in raw.items() if hasattr(ArcTheme, k)}
        return ArcTheme(**known)
    except (OSError, json.JSONDecodeError, TypeError):
        return ArcTheme()


def save_theme(theme: ArcTheme) -> None:
    """Write the theme to cli_theme.json (creates the file if absent)."""
    _THEME_FILE.write_text(
        json.dumps(asdict(theme), indent=2) + "\n",
        encoding="utf-8",
    )


def reset_theme() -> ArcTheme:
    """Reset cli_theme.json to factory defaults and return the default theme."""
    theme = ArcTheme()
    save_theme(theme)
    return theme

