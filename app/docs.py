"""Documentation loader for ARC CLI help.

ARC keeps user-facing documentation in the repository-level docs/ folder.  The
shell reads those Markdown files at runtime so command details can be updated
without changing command dispatch logic.

Running ``arc cliup`` pre-builds ``docs/docs-bundle.js`` (all Markdown embedded
as a JS object) and downloads vendor JS/CSS to ``docs/vendor/``.  After that,
``arc docs`` opens ``docs/index.html`` directly as a ``file://`` URL — no
server required.
"""

from __future__ import annotations

import re
import webbrowser
from pathlib import Path

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from app.commands.registry import COMMANDS

DOCS_ROOT = Path(__file__).resolve().parents[1] / "docs"
COMMAND_DOCS_ROOT = DOCS_ROOT / "commands"

SHELL_TOPICS = {
    "cd": "commands/cd.md",
    "remote": "commands/remote.md",
    "connect": "commands/connect.md",
    "disconnect": "commands/disconnect.md",
    "exit": "commands/exit.md",
    "quit": "commands/exit.md",
    "ls": "commands/ls.md",
    "devices": "commands/ls.md",
    "pwd": "commands/pwd.md",
    "folder": "commands/folder.md",
    "clear": "commands/clear.md",
    "help": "commands/help.md",
    "?": "commands/help.md",
    "docs": "commands/help.md",
}

GENERAL_TOPICS = {
    "overview":         "README.md",
    "usage":            "usage.md",
    "architecture":     "architecture.md",
    "configuration":    "configuration.md",
    "config":           "configuration.md",
    "config osx":       "config-osx.md",
    "config mac":       "config-osx.md",
    "config win":       "config-win.md",
    "config windows":   "config-win.md",
    "config nix":       "config-nix.md",
    "config linux":     "config-nix.md",
    "config generate":  "config-generate.md",
    "commands":         "commands/index.md",
}


def slugify(topic: str) -> str:
    """Return the docs filename slug for a shell command or topic."""
    lowered = topic.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", lowered).strip("-")
    return slug or "overview"


def available_help_topics() -> list[str]:
    """Return topics that can be completed after ``help ``."""
    topics = set(GENERAL_TOPICS)
    topics.update(SHELL_TOPICS)
    topics.update(COMMANDS)
    return sorted(topics)


def doc_path_for_topic(topic: str) -> Path | None:
    """Return the Markdown path for a help topic, if one exists."""
    normalized = topic.strip().lower()
    if not normalized:
        return DOCS_ROOT / GENERAL_TOPICS["overview"]

    if normalized in GENERAL_TOPICS:
        return DOCS_ROOT / GENERAL_TOPICS[normalized]

    if normalized in SHELL_TOPICS:
        return DOCS_ROOT / SHELL_TOPICS[normalized]

    if normalized in COMMANDS:
        return COMMAND_DOCS_ROOT / f"{slugify(normalized)}.md"

    # Last-chance direct lookup lets docs add aliases without code changes.
    candidate = COMMAND_DOCS_ROOT / f"{slugify(normalized)}.md"
    if candidate.exists():
        return candidate

    candidate = DOCS_ROOT / f"{slugify(normalized)}.md"
    if candidate.exists():
        return candidate

    return None


def render_help_topic(console: Console, topic: str) -> bool:
    """Render a Markdown help topic inside the ARC shell.

    Returns True when a document was found and printed; False otherwise.
    """
    path = doc_path_for_topic(topic)
    if path is None or not path.exists() or not path.is_file():
        return False

    markdown_text = path.read_text(encoding="utf-8")
    console.print()
    console.print(Panel(Markdown(markdown_text), title=f"Help: {topic or 'overview'}", border_style="cyan"))
    console.print()
    return True


# ---------------------------------------------------------------------------
# Browser docs opener — no server, just a file:// URL
# ---------------------------------------------------------------------------

def topic_to_page_path(topic: str) -> str:
    """Convert a help topic string to a relative docs page path.

    The returned path is relative to DOCS_ROOT and used as the ``?page=``
    query parameter in the browser docs viewer.
    """
    normalized = topic.strip().lower()

    if not normalized:
        return "README.md"

    if normalized in GENERAL_TOPICS:
        return GENERAL_TOPICS[normalized]

    if normalized in SHELL_TOPICS:
        return SHELL_TOPICS[normalized]

    if normalized in COMMANDS:
        return f"commands/{slugify(normalized)}.md"

    return f"commands/{slugify(normalized)}.md"


def open_docs_in_browser(topic: str = "") -> str:
    """Open docs/index.html in the default browser using a file:// URL.

    No HTTP server is needed — all content is pre-bundled into
    ``docs/docs-bundle.js`` by ``arc cliup``.

    If *topic* is given, opens the specific page for that topic.
    Returns the URL that was opened.
    """
    index_path = DOCS_ROOT / "index.html"

    if topic:
        page = topic_to_page_path(topic)
        url = index_path.as_uri() + f"?page={page}"
    else:
        url = index_path.as_uri()

    webbrowser.open(url)
    return url
