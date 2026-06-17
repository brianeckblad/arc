"""Command registry — merges domain modules. See AGENTS.md Command Registry Pattern section for details."""

from __future__ import annotations

from typing import Optional

# Re-export shared types so existing callers (shell.py, tests) keep working
# without changing their import paths.
from app.commands.base import CommandDef, ExecutionContext  # noqa: F401

# Domain-specific command tables
from app.commands.network import COMMANDS as _NETWORK
from app.commands.objects import COMMANDS as _OBJECTS
from app.commands.operations import COMMANDS as _OPERATIONS
from app.commands.security import COMMANDS as _SECURITY
from app.commands.setup import COMMANDS as _SETUP

# ---------------------------------------------------------------------------
# Merged command table
#
# Order matters for longest-prefix matching in match_command():
# more-specific entries (more tokens) must shadow less-specific ones.
# Each domain dict is responsible for ordering within its own set — here we
# simply merge them all. SORTED_COMMANDS below sorts by token count so the
# match loop always tries the longest prefix first.
# ---------------------------------------------------------------------------

COMMANDS: dict[str, CommandDef] = {
    **_SETUP,
    **_OBJECTS,
    **_SECURITY,
    **_NETWORK,
    **_OPERATIONS,
}

# Sorted longest-first so match_command() always finds the most-specific key.
SORTED_COMMANDS: list[tuple[str, CommandDef]] = sorted(
    COMMANDS.items(), key=lambda kv: len(kv[0]), reverse=True
)

# Category index — used by the help renderer in shell.py
CATEGORIES: dict[str, list[str]] = {}
for _key, _cmd in COMMANDS.items():
    CATEGORIES.setdefault(_cmd.category, []).append(_key)


# ---------------------------------------------------------------------------
# Arg parser
# ---------------------------------------------------------------------------

# Keywords that legitimately consume the next token as a named value.
# Add entries here when a new command needs ``keyword value`` syntax.
KEYWORD_PARAMS: set[str] = {
    "id", "name", "host", "source", "destination", "application",
    "protocol", "destination-port", "description", "count",
    "source-user", "category", "service", "to", "from",
}


def _parse_args(tokens: list[str]) -> dict:
    """Parse remainder tokens into a dict of named / positional args.

    Parsing rules (in order of precedence):
      1. ``--key value``  → explicit flag: result["key"] = value
      2. ``--key``        → boolean flag: result["key"] = True
      3. Known keyword tokens that take a value (see KEYWORD_PARAMS) followed
         by a non-flag token → result[keyword] = next_token
      4. Everything else  → positional list

    This ensures that ``show snippet My-Snippet-Name details`` correctly
    produces positional=["My-Snippet-Name", "details"] rather than treating
    "My-Snippet-Name" as a key and "details" as its value.

    The first positional also sets "id", "name", and "host" as shortcuts so
    handler code can use whichever is most semantically appropriate.
    """

    result: dict = {}
    positional: list[str] = []
    i = 0
    while i < len(tokens):
        token = tokens[i]

        # Explicit --flag handling
        if token.startswith("--"):
            key = token.lstrip("-")
            if i + 1 < len(tokens) and not tokens[i + 1].startswith("-"):
                result[key] = tokens[i + 1]
                i += 2
            else:
                result[key] = True
                i += 1
            continue

        # Known keyword that takes a value
        if token.lower() in KEYWORD_PARAMS and i + 1 < len(tokens):
            result[token.lower()] = tokens[i + 1]
            i += 2
            continue

        # Everything else is positional (bare names, subcommand words, etc.)
        positional.append(token)
        i += 1

    if positional:
        result["_positional"] = positional
        result.setdefault("id",   positional[0])
        result.setdefault("name", positional[0])
        result.setdefault("host", positional[0])
    return result


# ---------------------------------------------------------------------------
# Command matcher
# ---------------------------------------------------------------------------

def match_command(tokens: list[str]) -> tuple[Optional[str], CommandDef, dict]:
    """Find the longest matching command prefix in COMMANDS.

    Returns (matched_key, CommandDef, leftover_args_dict).
    Returns (None, None, {}) when no prefix matches.
    """
    sentence = " ".join(tokens).lower()
    for key, cmd_def in SORTED_COMMANDS:
        if sentence == key or sentence.startswith(key + " "):
            remainder = tokens[len(key.split()):]
            return key, cmd_def, _parse_args(remainder)
    return None, None, {}  # type: ignore[return-value]
