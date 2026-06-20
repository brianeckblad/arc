"""Loader for per-command help text — read from docs/commands/*.md front-matter.

Each command's help lives in **one** file: ``docs/commands/<slug>.md``.  The top
of the file is a YAML *front-matter* block that holds the structured fields the
shell needs; the Markdown body below it is the full ``help <command>`` page::

    ---
    command: packet-tracer
    description: Trace a packet through the folder's security rule base
    usage: packet-tracer from <zone> to <zone> source <ip> destination <ip> ...
        feature_flag: packet_tracer
    category: diagnostics
    api: (client-side)
    ---
    # packet-tracer
    ...full help page...

This is the single source of truth: the inline ``?`` / ``<command> ?`` help reads
``description`` and ``usage`` from the front-matter, and ``help <command>``
renders the body.  Regenerate everything (index, API reference, and any missing
front-matter) with ``python dev/generate_command_docs.py`` — it also runs as part of
``docsupdate``.

The loader is tolerant: a doc with no front-matter (or PyYAML missing) simply
leaves that command on its built-in ``CommandDef`` default, so the shell always
starts cleanly.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

from app.paths import COMMAND_DOCS_DIR as _COMMAND_DOCS_DIR

if TYPE_CHECKING:  # avoid an import cycle — registry imports this module
    from app.commands.base import CommandDef

logger = logging.getLogger(__name__)

# Module-level cache — doc front-matter is read once per session (edit + restart).
# Holds two maps: {command: description} and {command: usage}.
_cache: tuple[dict[str, str], dict[str, str]] | None = None


def parse_front_matter(text: str) -> tuple[dict[str, Any], str]:
    """Split *text* into (front_matter_dict, body).

    Front-matter is a leading ``---`` fenced YAML block.  When absent (or PyYAML
    is missing / the block is malformed) returns ``({}, text)`` so callers can
    fall back gracefully.
    """
    if not text.startswith("---"):
        return {}, text
    # Find the closing fence on its own line.
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return {}, text
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            block = "".join(lines[1:index])
            body = "".join(lines[index + 1:])
            try:
                import yaml

                meta = yaml.safe_load(block) or {}
                if not isinstance(meta, dict):
                    return {}, text
                return meta, body.lstrip("\n")
            except ImportError:
                logger.debug("PyYAML not available — front-matter not parsed")
                return {}, text
            except Exception as exc:  # noqa: BLE001 — never break startup
                logger.warning("front-matter parse error: %s", exc)
                return {}, text
    return {}, text


def _load() -> tuple[dict[str, str], dict[str, str]]:
    """Scan docs/commands/*.md front-matter into (descriptions, usages) maps.

    Each doc that declares a ``command`` and a ``description`` contributes one
    entry, keyed by the exact command string.  Cached after the first call.
    """
    global _cache
    if _cache is not None:
        return _cache

    descriptions: dict[str, str] = {}
    usages: dict[str, str] = {}

    if not _COMMAND_DOCS_DIR.is_dir():
        _cache = ({}, {})
        return _cache

    for path in _COMMAND_DOCS_DIR.glob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        if not text.startswith("---"):
            continue  # plain doc, no structured help
        meta, _body = parse_front_matter(text)
        command = meta.get("command")
        if not isinstance(command, str) or not command.strip():
            continue
        name = command.strip()
        description = meta.get("description")
        usage = meta.get("usage")
        if isinstance(description, str) and description.strip():
            descriptions[name] = description.strip()
        if isinstance(usage, str) and usage.strip():
            usages[name] = usage.strip()

    _cache = (descriptions, usages)
    return _cache


def description_overrides() -> dict[str, str]:
    """Return ``{command_key: description}`` from doc front-matter (cached)."""
    return _load()[0]


def usage_overrides() -> dict[str, str]:
    """Return ``{command_key: usage}`` from doc front-matter (cached)."""
    return _load()[1]


def apply_overrides(commands: dict[str, "CommandDef"]) -> None:
    """Apply description + usage from doc front-matter onto the CommandDefs in place.

    Mutates the ``CommandDef`` objects so every help/completion code path that
    reads ``CommandDef.description`` / ``.usage`` shows the doc-file text.  Called
    once by the registry after it merges every domain module.
    """
    descriptions, usages = _load()
    for key, description in descriptions.items():
        cmd = commands.get(key)
        if cmd is not None:
            cmd.description = description
    for key, usage in usages.items():
        cmd = commands.get(key)
        if cmd is not None:
            cmd.usage = usage


def invalidate_cache() -> None:
    """Force a re-read on next access (used by tools/tests that rewrite docs)."""
    global _cache
    _cache = None





