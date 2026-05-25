"""Documentation loader for ARC CLI help.

ARC keeps user-facing documentation in the repository-level docs/ folder.  The
shell reads those Markdown files at runtime so command details can be updated
without changing command dispatch logic.

The same docs folder is served by a local HTTP server when `arc docs` is run,
pointing the default browser at docs/index.html which renders a pan.dev-style
documentation portal.
"""

from __future__ import annotations

import http.server
import re
import socketserver
import threading
import webbrowser
from pathlib import Path
from typing import Optional

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
    "overview": "README.md",
    "usage": "usage.md",
    "architecture": "architecture.md",
    "configuration": "configuration.md",
    "config": "configuration.md",
    "commands": "commands/index.md",
}

# ---------------------------------------------------------------------------
# Module-level server state — single background server for the session
# ---------------------------------------------------------------------------

_server_instance: Optional[socketserver.TCPServer] = None
_server_port: Optional[int] = None
_server_lock = threading.Lock()


def slugify(topic: str) -> str:
    """Return the docs filename slug for a shell command or topic."""
    lowered = topic.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", lowered).strip("-")
    return slug or "overview"


def available_help_topics() -> list[str]:
    """Return topics that can be completed after `help `."""
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
# Local HTTP docs server
# ---------------------------------------------------------------------------

def _make_handler_class(docs_dir: str) -> type:
    """Return a SimpleHTTPRequestHandler subclass rooted at *docs_dir*."""

    class _Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=docs_dir, **kwargs)

        def log_message(self, fmt, *args) -> None:  # noqa: D102  (suppress access log)
            pass

    return _Handler


def start_docs_server(start_port: int = 8765) -> str:
    """Start a background HTTP server serving the docs/ folder.

    The server runs in a daemon thread so it exits cleanly when ARC exits.
    Returns the base URL (e.g. ``http://localhost:8765``).
    Calling this function a second time returns the already-running URL.
    """
    global _server_instance, _server_port

    with _server_lock:
        if _server_instance is not None:
            return f"http://localhost:{_server_port}"

        handler = _make_handler_class(str(DOCS_ROOT))

        for port in range(start_port, start_port + 10):
            try:
                server = socketserver.TCPServer(("127.0.0.1", port), handler)
                server.allow_reuse_address = True
                _server_instance = server
                _server_port = port
                t = threading.Thread(target=server.serve_forever, daemon=True)
                t.start()
                return f"http://localhost:{port}"
            except OSError:
                continue

        raise RuntimeError(
            f"Could not bind a docs server port in range {start_port}–{start_port + 9}."
        )


def topic_to_page_path(topic: str) -> str:
    """Convert a help topic string to a relative docs page path.

    The returned path is relative to DOCS_ROOT and suitable for use as the
    ``?page=`` URL parameter in the browser docs viewer.
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
    """Start the docs server (if not running) and open the browser.

    If *topic* is given, opens the specific page for that topic.
    Returns the URL that was opened.
    """
    base_url = start_docs_server()

    if topic:
        page = topic_to_page_path(topic)
        url = f"{base_url}/?page={page}"
    else:
        url = f"{base_url}/"

    webbrowser.open(url)
    return url
