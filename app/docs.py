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
import sys
import webbrowser
from contextlib import contextmanager
from pathlib import Path

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from app.commands.registry import COMMANDS
from app.settings.command_help import parse_front_matter

DOCS_ROOT = Path(__file__).resolve().parents[1] / "docs"
COMMAND_DOCS_ROOT = DOCS_ROOT / "commands"

SHELL_TOPICS = {
    "cd":           "commands/cd.md",
    "connect":      "commands/connect.md",
    "exit":         "commands/exit.md",
    "quit":         "commands/exit.md",
    "pwd":          "commands/pwd.md",
    "folder":       "commands/folder.md",
    "clear":        "commands/clear.md",
    "help":         "commands/help.md",
    "?":            "commands/help.md",
    "docs":         "commands/help.md",
    # Feature flags builtin
    "feature":      "commands/features.md",
    "features":     "commands/features.md",
    # Per-user terminal preferences builtin
    "terminal":     "commands/terminal.md",
}

GENERAL_TOPICS = {
    "overview":         "README.md",
    "usage":            "usage.md",
    "architecture":     "architecture.md",
    "configuration":    "configuration.md",
    "config":           "configuration.md",
    "config generate":  "config-generate.md",
    "commands":         "commands/index.md",
    # API reference — complete mapping of API resources to ARC commands
    "api-reference":    "commands/api-reference.md",
    "api":              "commands/api-reference.md",
    # Guided credential setup — also reachable via the `setup` shell builtin
    "setup":            "setup.md",
    "getting-started":  "setup.md",
    # Device access & auth planes (SCM API vs SCM proxy vs SSH/2FA)
    "device-access":    "device-access.md",
    "device access":    "device-access.md",
    "device-auth":      "device-access.md",
    "remote-access":    "device-access.md",
    "2fa":              "device-access.md",
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


def synthesize_command_help(key: str) -> str:
    """Build a Markdown help page for a command straight from the registry.

    Most generated commands have no hand-written doc file — their CommandDef
    already carries everything the operator needs.  Write a real
    ``docs/commands/<slug>.md`` page only when there is more to say; it then
    takes precedence over this synthesized text.

    Results are cached per session — the registry never changes at runtime so
    re-generating the same page on every help request is wasteful.
    """
    cached = _synthesis_cache.get(key)
    if cached is not None:
        return cached
    cmd = COMMANDS[key]
    lines = [f"# {key}", "", cmd.description or "(no description)", ""]
    if cmd.usage:
        lines += ["**Usage**", "", f"    {cmd.usage}", ""]
    lines.append(f"- **Category:** {cmd.category}")
    lines.append(f"- **Scope:** {cmd.scope}")
    if cmd.feature_flag:
        lines.append(f"- **Feature flag:** `{cmd.feature_flag}` (see `feature show`)")
    if cmd.ssh_command is not None:
        lines.append("- **Remote:** supports `--remote <device>` (SSH)")
    lines += ["", "_Synthesized from the command registry — no hand-written page exists for this command._"]
    result = "\n".join(lines)
    _synthesis_cache[key] = result
    return result


# Per-session cache for synthesized command help pages.  The registry is
# immutable at runtime so we never need to invalidate this.
_synthesis_cache: dict[str, str] = {}


# Pager behavior — set once at shell startup from the user's preferences file
# (`terminal length <n>` persists it). 0 = paging disabled: print everything
# and rely on terminal scrollback. There is no terminal-size auto-detection.
_PAGE_LENGTH = 0


def set_page_length(lines: int) -> None:
    """Set the pager threshold (0 disables paging). Called from shell startup."""
    global _PAGE_LENGTH
    _PAGE_LENGTH = max(0, int(lines))


def page_length() -> int:
    """Current pager threshold in lines (0 = paging disabled)."""
    return _PAGE_LENGTH


class _PagingFile:
    """A sys.stdout wrapper that pauses output every *page_size* lines.

    Preserves ANSI escape codes (isatty() returns True so Rich keeps colours).
    Used by paging_stdout() to make *all* shell output — builtins, API results,
    help text — respect ``terminal length``.
    """

    def __init__(self, real_file, page_size: int) -> None:
        self._real = real_file
        self._page_size = page_size
        self._lines = 0
        self._stopped = False
        try:
            import termios as _t  # noqa: F401
            import tty as _tty    # noqa: F401
            self._has_termios = True
        except ImportError:
            self._has_termios = False

    # Rich checks isatty() to decide whether to emit ANSI codes.
    def isatty(self) -> bool:       # noqa: D102
        return True

    def fileno(self) -> int:        # noqa: D102
        return self._real.fileno()

    def write(self, data: str) -> int:  # noqa: D102
        if self._stopped or not data:
            return len(data)

        # Split on newlines; each separator means one completed visible line.
        parts = data.split("\n")
        for i, chunk in enumerate(parts):
            last = i == len(parts) - 1
            self._real.write(chunk)
            if not last:
                self._real.write("\n")
                self._real.flush()
                self._lines += 1
                if self._lines >= self._page_size:
                    if not self._show_more():
                        self._stopped = True
                        return len(data)
                    # _show_more resets _lines for space/enter
        return len(data)

    def flush(self) -> None:        # noqa: D102
        self._real.flush()

    def _getch(self) -> str:
        if not self._has_termios:
            return sys.stdin.readline()[:1]
        import termios, tty
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.buffer.read(1)
            return ch.decode("utf-8", errors="replace")
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

    def _show_more(self) -> bool:
        """Print --More-- prompt; return False if user quits."""
        prompt = " --More-- "
        self._real.write(f"\033[7m{prompt}\033[m")
        self._real.flush()
        key = self._getch()
        self._real.write(f"\r{' ' * len(prompt)}\r")
        self._real.flush()
        if key in ("q", "Q", "\x03", "\x04"):
            self._real.write("[output truncated]\n")
            self._real.flush()
            return False
        elif key in ("\r", "\n"):
            # Enter: show one more line then pause again
            self._lines = self._page_size - 1
        else:
            # Space or anything else: next full page
            self._lines = 0
        return True


# Commands that take over the terminal (interactive PTY, screen redraws, etc.)
# — paging must not be installed for these.
_PAGING_EXEMPT = frozenset({
    "connect", "configure", "conf", "setup", "watch", "clear", "docs",
})


@contextmanager
def paging_stdout(page_size: int):
    """Context manager: wrap sys.stdout with line-based paging.

    Installs a *_PagingFile* as sys.stdout so that ALL output — Rich console
    prints, plain print() calls, direct writes — is paged through --More--.
    Because _PagingFile.isatty() returns True, Rich preserves ANSI colours.
    """
    if page_size <= 0:
        yield
        return
    pager = _PagingFile(sys.stdout, page_size)
    old = sys.stdout
    sys.stdout = pager
    try:
        yield
    finally:
        sys.stdout = old


def cisco_pager(lines: list, page_size: int) -> None:
    """Cisco IOS-style --More-- interactive pager.

    Prints *lines* one page at a time (page_size lines per page).
    At each pause the operator presses:
      space / any key  — next full page
      enter            — one more line
      q / Q / Ctrl-C   — quit (truncate)

    When stdout is not a TTY (piped/redirected), all lines are printed
    without pausing.
    """
    import sys

    if not lines:
        return

    if not sys.stdout.isatty():
        sys.stdout.write("\n".join(lines) + "\n")
        sys.stdout.flush()
        return

    try:
        import termios
        import tty
        _has_termios = True
    except ImportError:
        _has_termios = False

    def _getch() -> str:
        if not _has_termios:
            return sys.stdin.readline()[:1]
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.buffer.read(1)
            return ch.decode("utf-8", errors="replace")
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

    total = len(lines)
    idx = 0
    lines_on_screen = 0

    while idx < total:
        sys.stdout.write(lines[idx] + "\n")
        sys.stdout.flush()
        idx += 1
        lines_on_screen += 1

        if lines_on_screen >= page_size and idx < total:
            remaining = total - idx
            prompt = f" --More-- ({idx}/{total} lines, {remaining} remaining) "
            sys.stdout.write(f"\033[7m{prompt}\033[m")
            sys.stdout.flush()

            key = _getch()

            # Erase the prompt line
            sys.stdout.write(f"\r{' ' * len(prompt)}\r")
            sys.stdout.flush()

            if key in ("q", "Q", "\x03", "\x04"):
                sys.stdout.write("[output truncated]\n")
                sys.stdout.flush()
                return
            elif key in ("\r", "\n"):
                # Enter: show one more line then pause again
                lines_on_screen = page_size - 1
            else:
                # Space or anything else: next full page
                lines_on_screen = 0


def render_help_topic(console: Console, topic: str, use_pager: bool = True) -> bool:
    """Render a Markdown help topic inside the ARC shell.

    Args:
        console: Rich console for output
        topic: Topic name to render
        use_pager: If False, never page (regardless of `terminal length`)

    Returns True when a document was found and printed; False otherwise.
    """
    path = doc_path_for_topic(topic)
    if path is None or not path.exists() or not path.is_file():
        # Registered commands without a doc file get a registry-synthesized page.
        normalized = topic.strip().lower()
        if normalized in COMMANDS:
            markdown_text = synthesize_command_help(normalized)
            console.print()
            console.print(Panel(Markdown(markdown_text), title=f"Help: {normalized}", border_style="cyan"))
            console.print()
            return True
        return False

    markdown_text = path.read_text(encoding="utf-8")
    # Command docs begin with YAML front-matter (the structured help fields used
    # by `?`).  Strip it so only the human-readable body is rendered here.
    _meta, markdown_text = parse_front_matter(markdown_text)
    
    # Page only when the user set a terminal length (`terminal length <n>`)
    # and the document exceeds it. 1 line of markdown ≈ 1 terminal line.
    line_count = len(markdown_text.split('\n'))
    needs_pager = _PAGE_LENGTH > 0 and line_count > _PAGE_LENGTH

    def _print_doc():
        console.print()
        console.print(Panel(Markdown(markdown_text), title=f"Help: {topic or 'overview'}", border_style="cyan"))
        console.print()
    
    if use_pager and needs_pager:
        with console.pager(styles=True):
            _print_doc()
    else:
        _print_doc()
    
    return True


# OS-key → platform doc.  Rendered by the `setup <os>` subcommands (these guides
# used to be reachable as `help config <os>` topics; they now live under setup).
_OS_SETUP_DOCS = {
    "osx": "setup-osx.md", "mac": "setup-osx.md", "macos": "setup-osx.md",
    "darwin": "setup-osx.md",
    "linux": "setup-linux.md", "nix": "setup-linux.md", "wsl": "setup-linux.md",
    "win": "setup-win.md", "windows": "setup-win.md",
}


def os_setup_doc(os_key: str) -> str | None:
    """Return the platform doc filename for an OS key (or None if unknown)."""
    return _OS_SETUP_DOCS.get(os_key.strip().lower())


def render_doc_file(console: Console, filename: str, title: str | None = None,
                    use_pager: bool = True) -> bool:
    """Render a Markdown file from the docs root by filename (front-matter stripped).

    Used for guides that are no longer registered as `help` topics (e.g. the
    per-OS `setup osx|linux|win` pages).  Returns True when rendered.
    """
    path = DOCS_ROOT / filename
    if not path.exists() or not path.is_file():
        return False
    _meta, markdown_text = parse_front_matter(path.read_text(encoding="utf-8"))
    line_count = len(markdown_text.split("\n"))
    needs_pager = _PAGE_LENGTH > 0 and line_count > _PAGE_LENGTH

    def _print_doc():
        console.print()
        console.print(Panel(Markdown(markdown_text), title=title or f"Help: {filename}",
                            border_style="cyan"))
        console.print()

    if use_pager and needs_pager:
        with console.pager(styles=True):
            _print_doc()
    else:
        _print_doc()
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
