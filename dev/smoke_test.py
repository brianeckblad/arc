#!/usr/bin/env python3
"""ARC smoke test suite.

Covers three concern areas:
  1. Syntax       — py_compile every Python module under app/
  2. Imports      — every module imports cleanly (no side-effect errors)
  3. Registry     — COMMANDS dict is structurally valid (no lambdas, required fields, etc.)
  4. Arg parser   — _parse_args() and match_command() return the right shapes
  5. Config types — ArcConfig / SshConfig dataclasses default-construct correctly
  6. Formatter    — key renderer functions accept sample data without raising
  7. CLI banner   — every banner line lands descriptions at visual column 28

Run directly:
    python dev/smoke_test.py

Run from pre-commit hook:
    python dev/smoke_test.py --quiet   (exit 0 = OK, exit 1 = failure)

MAINTENANCE NOTE:
  • After any change to app/ modules → re-run to verify imports + registry.
  • After any change to the CLI banner in app/shell.py → re-run section 7.
  • After adding a new CommandDef → registry tests auto-pick it up; no edit needed.
  • After adding a new formatter function → add a minimal call in section 6.
"""

from __future__ import annotations

import importlib
import py_compile
import re
import sys
import traceback
from pathlib import Path
from typing import Any

# Ensure the project root is on sys.path so `import app.*` works when the
# script is invoked from any directory (e.g. `python dev/smoke_test.py`).
ROOT = Path(__file__).resolve().parent.parent   # arc/
APP  = ROOT / "app"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

PASS = "\033[32m✓\033[0m"
FAIL = "\033[31m✗\033[0m"
SKIP = "\033[33m-\033[0m"

_failures: list[str] = []
_passes:   int = 0


def ok(msg: str) -> None:
    global _passes
    _passes += 1
    print(f"  {PASS}  {msg}")


def fail(msg: str, detail: str = "") -> None:
    _failures.append(msg)
    detail_str = f"\n       {detail}" if detail else ""
    print(f"  {FAIL}  {msg}{detail_str}")


def section(title: str) -> None:
    print(f"\n{title}")
    print("─" * len(title))


# ---------------------------------------------------------------------------
# 1. Syntax — py_compile every .py under app/
# ---------------------------------------------------------------------------

def test_syntax() -> None:
    section("1. Syntax (py_compile)")
    py_files = sorted(APP.rglob("*.py"))
    for path in py_files:
        rel = path.relative_to(ROOT)
        try:
            py_compile.compile(str(path), doraise=True)
            ok(str(rel))
        except py_compile.PyCompileError as exc:
            fail(str(rel), str(exc))


# ---------------------------------------------------------------------------
# 2. Imports — every module in app/ imports without error
# ---------------------------------------------------------------------------

def test_imports() -> None:
    section("2. Imports")

    # Modules in dependency order — base types before consumers.
    modules = [
        "app",
        "app.config",
        "app.commands.base",
        "app.commands.setup",
        "app.commands.objects",
        "app.commands.security",
        "app.commands.network",
        "app.commands.operations",
        "app.commands.registry",
        "app.api.client",
        "app.ssh.manager",
        "app.utils.formatter",
        "app.theme",
        "app.docs",
    ]

    for mod in modules:
        try:
            importlib.import_module(mod)
            ok(mod)
        except Exception as exc:
            fail(mod, traceback.format_exc(limit=3).strip())


# ---------------------------------------------------------------------------
# 3. Registry integrity
# ---------------------------------------------------------------------------

def test_registry() -> None:
    section("3. Registry integrity")

    from app.commands.registry import COMMANDS, SORTED_COMMANDS, match_command
    from app.commands.base import CommandDef

    # 3a — COMMANDS is non-empty
    if COMMANDS:
        ok(f"COMMANDS populated  ({len(COMMANDS)} entries)")
    else:
        fail("COMMANDS is empty")

    # 3b — All values are CommandDef instances
    bad_types = [k for k, v in COMMANDS.items() if not isinstance(v, CommandDef)]
    if bad_types:
        fail(f"Non-CommandDef values: {bad_types[:5]}")
    else:
        ok("All COMMANDS values are CommandDef instances")

    # 3c — Every CommandDef has required fields set
    bad_fields: list[str] = []
    for key, cmd in COMMANDS.items():
        if not cmd.description:
            bad_fields.append(f"{key!r}: missing description")
        if cmd.scope not in ("folder", "device", "global"):
            bad_fields.append(f"{key!r}: invalid scope {cmd.scope!r}")
    if bad_fields:
        for b in bad_fields:
            fail(b)
    else:
        ok("All CommandDef entries have description + valid scope")

    # 3d — No inline lambdas as ssh_command (lambdas cannot be pickled / inspected)
    lambda_cmds: list[str] = []
    for key, cmd in COMMANDS.items():
        if callable(cmd.ssh_command) and cmd.ssh_command.__name__ == "<lambda>":
            lambda_cmds.append(key)
    if lambda_cmds:
        fail(f"Inline lambda ssh_command detected (must be a named def): {lambda_cmds}")
    else:
        ok("No inline lambda ssh_commands")

    # 3e — SORTED_COMMANDS is longest-string-first (sorts by key string length, not token count)
    key_lengths = [len(k) for k, _ in SORTED_COMMANDS]
    if key_lengths == sorted(key_lengths, reverse=True):
        ok("SORTED_COMMANDS is ordered longest-key-string-first")
    else:
        fail("SORTED_COMMANDS is not longest-prefix-first")

    # 3f — match_command returns correct shape
    test_cases: list[tuple[list[str], str | None]] = [
        (["show", "address"],             "show address"),
        (["show", "devices"],             "show devices"),
        (["show", "security", "policy"],  "show security policy"),
        (["nonexistent", "command"],      None),
    ]
    for tokens, expected_key in test_cases:
        matched_key, cmd_def, args = match_command(tokens)
        if matched_key == expected_key:
            ok(f"match_command({tokens!r}) → {matched_key!r}")
        else:
            fail(
                f"match_command({tokens!r})",
                f"expected {expected_key!r}, got {matched_key!r}",
            )


# ---------------------------------------------------------------------------
# 4. Arg parser
# ---------------------------------------------------------------------------

def test_arg_parser() -> None:
    section("4. Arg parser (_parse_args)")

    from app.commands.registry import _parse_args

    cases: list[tuple[list[str], dict]] = [
        # positional sets _positional, id, name, host
        (["my-object"],        {"_positional": ["my-object"], "id": "my-object",
                                "name": "my-object", "host": "my-object"}),
        # explicit flag
        (["--remote"],         {"remote": True}),
        # flag with value
        (["--count", "10"],    {"count": "10"}),
        # keyword param — consumes next token; no positional list set
        (["id", "abc-123"],    {"id": "abc-123"}),
        # empty
        ([],                   {}),
    ]

    for tokens, expected in cases:
        result = _parse_args(tokens)
        if result == expected:
            ok(f"_parse_args({tokens!r}) → correct")
        else:
            fail(
                f"_parse_args({tokens!r})",
                f"expected {expected!r}\n       got     {result!r}",
            )


# ---------------------------------------------------------------------------
# 5. Config types
# ---------------------------------------------------------------------------

def test_config() -> None:
    section("5. Config types")

    from app.config import ArcConfig, SSHConfig, SCMConfig

    # 5a — Default-construct without errors
    try:
        cfg = ArcConfig()
        ok("ArcConfig() constructs with defaults")
    except Exception as exc:
        fail("ArcConfig() construction failed", str(exc))
        return

    # 5b — SCMConfig.is_configured is False when empty
    scm = SCMConfig()
    if not scm.is_configured:
        ok("SCMConfig().is_configured == False when empty")
    else:
        fail("SCMConfig().is_configured should be False when empty")

    # 5c — SCMConfig.is_configured is True when bearer token is set
    scm_with_token = SCMConfig(bearer_token="test-token")
    if scm_with_token.is_configured:
        ok("SCMConfig(bearer_token=...).is_configured == True")
    else:
        fail("SCMConfig with bearer_token should be is_configured")

    # 5d — SCMConfig.is_configured is True when OAuth triple is set
    scm_oauth = SCMConfig(client_id="cid", client_secret="csec", tsg_id="tsg")
    if scm_oauth.is_configured:
        ok("SCMConfig(client_id+secret+tsg_id).is_configured == True")
    else:
        fail("SCMConfig with OAuth creds should be is_configured")

    # 5e — profile_name defaults to 'default'
    if cfg.profile_name == "default":
        ok("ArcConfig.profile_name defaults to 'default'")
    else:
        fail(f"ArcConfig.profile_name expected 'default', got {cfg.profile_name!r}")


# ---------------------------------------------------------------------------
# 6. Formatter
# ---------------------------------------------------------------------------

def test_formatter() -> None:
    section("6. Formatter")

    from app.utils import formatter

    # 6a — _kv_table with sample data
    try:
        t = formatter._kv_table({"hostname": "fw01", "serial": "007200123456"}, title="Test")
        ok("_kv_table() returns Rich Table")
    except Exception as exc:
        fail("_kv_table()", str(exc))

    # 6b — _list_table with sample rows
    try:
        rows = [{"name": "obj1", "type": "ip-netmask", "value": "10.0.0.0/8"}]
        t = formatter._list_table(rows, title="Addresses")
        ok("_list_table() returns Rich Table")
    except Exception as exc:
        fail("_list_table()", str(exc))

    # 6c — _list_table with empty rows (edge case — should not raise)
    try:
        t = formatter._list_table([], title="Empty")
        ok("_list_table([]) handles empty list")
    except Exception as exc:
        fail("_list_table([]) raised unexpectedly", str(exc))

    # 6d — format_folder_tree with minimal data
    try:
        folders = [
            {"name": "Shared",     "id": "1", "parent": None},
            {"name": "Production", "id": "2", "parent": "Shared"},
        ]
        devices: list[dict] = []
        tree = formatter.format_folder_tree(folders, devices)
        ok("format_folder_tree() returns Rich Tree")
    except Exception as exc:
        fail("format_folder_tree()", str(exc))


# ---------------------------------------------------------------------------
# 7. CLI banner alignment
#    Descriptions in the startup banner must all start at visual column 28.
#    (2 spaces indent + visible command text + padding spaces = 28)
#
#    The logo itself lives in app/banner.txt — edit there to
#    change the art or add a legal notice.  This section only checks the
#    command-hint lines hardcoded in _print_banner().
# ---------------------------------------------------------------------------

# The exact banner lines as they appear in app/shell.py _print_banner().
# UPDATE THIS LIST whenever the banner lines change.
_BANNER_LINES: list[tuple[str, str]] = [
    # (visible_command_text,  expected_padding_spaces_after_[/cyan])
    ("cd <device>",     "               "),   # 11 chars → 15 sp → col 28
    ("remote <device>", "           "),        # 15 chars → 11 sp → col 28
    ("connect",         "                   "), # 7 chars → 19 sp → col 28
    ("folder <name>",   "             "),       # 13 chars → 13 sp → col 28
    ("account <name>",  "            "),        # 14 chars → 12 sp → col 28
    ("?",               "                         "),  # 1 char → 25 sp → col 28
]

_BANNER_TARGET_COL = 28
_BANNER_INDENT     = 2

# Also verify against the live shell.py source so this test fails immediately
# when someone edits the banner without updating _BANNER_LINES.
_BANNER_PATTERN = re.compile(
    r'\[cyan\]([^\[]+)\[/cyan\](\s+)\S'  # [cyan]CMD[/cyan]SPACES first-word
)


def test_banner_alignment() -> None:
    section("7. CLI banner alignment  (descriptions at visual col 28)")

    shell_src = (APP / "shell.py").read_text(encoding="utf-8")

    # Extract live banner lines from source
    live_matches = _BANNER_PATTERN.findall(shell_src)

    # Filter to only the banner block (inside _print_banner method)
    # We use the section between the console.print( containing cd <device>
    start_marker = '"  [cyan]cd <device>[/cyan]'
    end_marker   = '"  [cyan]?[/cyan]'
    banner_block_start = shell_src.find(start_marker)
    banner_block_end   = shell_src.find(end_marker, banner_block_start)
    if banner_block_start == -1:
        fail("Could not locate banner block in shell.py")
        return
    banner_block = shell_src[banner_block_start: banner_block_end + 200]

    live: list[tuple[str, str]] = _BANNER_PATTERN.findall(banner_block)

    if not live:
        fail("No banner lines found in shell.py — check _BANNER_PATTERN regex")
        return

    # 7a — Number of lines matches expected
    if len(live) == len(_BANNER_LINES):
        ok(f"Banner has {len(live)} command lines (expected {len(_BANNER_LINES)})")
    else:
        fail(
            f"Banner line count mismatch",
            f"expected {len(_BANNER_LINES)}, found {len(live)}",
        )

    # 7b — Each line lands on the right column
    for idx, (cmd_text, padding) in enumerate(live):
        col = _BANNER_INDENT + len(cmd_text) + len(padding)
        if col == _BANNER_TARGET_COL:
            ok(f"col {col}  [{cmd_text!r} + {len(padding)} spaces]")
        else:
            fail(
                f"col {col} ≠ {_BANNER_TARGET_COL}  [{cmd_text!r} + {len(padding)} spaces]",
                f"Need {_BANNER_TARGET_COL - _BANNER_INDENT - len(cmd_text)} spaces, "
                f"found {len(padding)}",
            )

    # 7c — Verify _BANNER_LINES reference table is in sync with live source
    for idx, ((ref_cmd, ref_pad), (live_cmd, live_pad)) in enumerate(
        zip(_BANNER_LINES, live)
    ):
        if ref_cmd != live_cmd or ref_pad != live_pad:
            fail(
                f"_BANNER_LINES[{idx}] out of sync with shell.py",
                f"reference: ({ref_cmd!r}, {ref_pad!r})\n"
                f"       live:      ({live_cmd!r}, {live_pad!r})\n"
                f"       → Update _BANNER_LINES in smoke_test.py",
            )
        else:
            ok(f"_BANNER_LINES[{idx}] in sync  ({ref_cmd!r})")


# ---------------------------------------------------------------------------
# 8. Inline help alignment
#    All command names in every ? menu section must:
#      a) contain no [markup] tags (Rich silently eats them, breaking alignment)
#      b) fit within _HELP_CMD_WIDTH chars so descriptions align on the same column
#
#    The builtins list in _print_shell_builtins() is checked by extracting it
#    directly from the shell source so this test catches every future edit.
# ---------------------------------------------------------------------------

# Builtin command names as they appear in _print_shell_builtins().
# UPDATE this list whenever builtins are added, removed, or renamed.
_BUILTIN_NAMES: list[str] = [
    "cd <device>",
    "connect <device>",
    "remote <device>",
    "folder <name>",
    "folder create <name>",
    "tsg <id>",
    "account <name>",
    "configure",
    "cli <subcommand>",
    "ls",
    "pwd",
    "docs",
    "clear",
    "exit / quit",
]

_MARKUP_RE = re.compile(r'\[[a-zA-Z/_][^\]]*\]')


def test_inline_help_alignment() -> None:
    section("8. Inline help alignment")

    # Read _HELP_CMD_WIDTH from shell.py
    shell_src = (APP / "shell.py").read_text(encoding="utf-8")
    m = re.search(r'^_HELP_CMD_WIDTH\s*=\s*(\d+)', shell_src, re.MULTILINE)
    if not m:
        fail("_HELP_CMD_WIDTH constant not found in shell.py")
        return
    cmd_width = int(m.group(1))
    ok(f"_HELP_CMD_WIDTH = {cmd_width}")

    # 8a — Registered command keys: no markup, fit in field
    from app.commands.registry import COMMANDS
    from app.shell import _SHELL_BUILTINS, _expand_unambiguous_prefix
    markup_keys = [k for k in COMMANDS if _MARKUP_RE.search(k)]
    if markup_keys:
        fail(f"Registered commands contain [markup] in key (breaks alignment): {markup_keys}")
    else:
        ok(f"No [markup] tags in any of the {len(COMMANDS)} registered command keys")

    oversized_keys = [k for k in COMMANDS if len(k) > cmd_width]
    if oversized_keys:
        for k in oversized_keys:
            fail(f"Registered key too wide ({len(k)} > {cmd_width}): {k!r}")
    else:
        ok(f"All registered command keys fit within {cmd_width} chars")

    # 8b — Builtin names: no markup, fit in field
    markup_builtins = [n for n in _BUILTIN_NAMES if _MARKUP_RE.search(n)]
    if markup_builtins:
        for n in markup_builtins:
            fail(f"Builtin name contains [markup] (breaks alignment): {n!r}")
    else:
        ok(f"No [markup] tags in any of the {len(_BUILTIN_NAMES)} builtin names")

    oversized_builtins = [n for n in _BUILTIN_NAMES if len(n) > cmd_width]
    if oversized_builtins:
        for n in oversized_builtins:
            fail(f"Builtin name too wide ({len(n)} > {cmd_width}): {n!r}")
    else:
        ok(f"All builtin names fit within {cmd_width} chars")

    # 8b.1 — Unambiguous shorthand expansion
    phrases = [[b] for b in _SHELL_BUILTINS if b != "?"] + [k.split() for k in COMMANDS]
    cases = [
        (["e"], ["exit"]),
        (["q"], ["quit"]),
        (["sh", "sec", "pol"], ["show", "security", "policy"]),
        # Ambiguous (docs/devices) should remain unchanged.
        (["d"], ["d"]),
    ]
    for raw, expected in cases:
        got = _expand_unambiguous_prefix(raw, phrases)
        if got == expected:
            ok(f"shorthand {raw!r} -> {expected!r}")
        else:
            fail(f"shorthand expansion mismatch for {raw!r}", f"expected {expected!r}, got {got!r}")

    # 8c — Verify _BUILTIN_NAMES is in sync with shell.py source
    # Extract builtin names line-by-line from _print_shell_builtins block.
    in_block = False
    live_names: list[str] = []
    for line in shell_src.splitlines():
        if "_print_shell_builtins" in line and "def " in line:
            in_block = True
        if in_block:
            m2 = re.match(r'\s+\("([^"]+)"', line)
            if m2:
                live_names.append(m2.group(1))
            # Stop at the closing ] of the builtins list
            if live_names and line.strip() == "]":
                break

    if not live_names:
        fail("Could not locate builtins list in shell.py — check _print_shell_builtins")
        return

    if live_names == _BUILTIN_NAMES:
        ok(f"_BUILTIN_NAMES in sync with shell.py ({len(live_names)} entries)")
    else:
        in_ref_not_live = [n for n in _BUILTIN_NAMES if n not in live_names]
        in_live_not_ref = [n for n in live_names if n not in _BUILTIN_NAMES]
        if in_ref_not_live:
            fail(f"_BUILTIN_NAMES has entries not in shell.py: {in_ref_not_live}")
        if in_live_not_ref:
            fail(
                f"shell.py builtins not in _BUILTIN_NAMES (update smoke_test.py): "
                f"{in_live_not_ref}"
            )


# ---------------------------------------------------------------------------
# 9. Theme system
# ---------------------------------------------------------------------------

def test_theme() -> None:
    section("9. Theme system")

    from app.theme import ArcTheme, THEME_KEYS, load_theme

    # 9a — ArcTheme default-constructs
    try:
        t = ArcTheme()
        ok("ArcTheme() constructs with defaults")
    except Exception as exc:
        fail("ArcTheme() construction failed", str(exc))
        return

    # 9b — Every THEME_KEYS key exists on ArcTheme
    missing = [k for k in THEME_KEYS if not hasattr(ArcTheme, k)]
    if missing:
        fail(f"THEME_KEYS references unknown ArcTheme fields: {missing}")
    else:
        ok(f"All {len(THEME_KEYS)} THEME_KEYS map to ArcTheme fields")

    # 9c — load_theme() returns an ArcTheme (may read from file or use defaults)
    try:
        loaded = load_theme()
        if isinstance(loaded, ArcTheme):
            ok("load_theme() returns ArcTheme instance")
        else:
            fail(f"load_theme() returned unexpected type: {type(loaded)}")
    except Exception as exc:
        fail("load_theme() raised", str(exc))

    # 9d — cli_theme.json exists
    theme_file = APP / "cli_theme.json"
    if theme_file.exists():
        ok(f"app/cli_theme.json exists")
    else:
        fail("app/cli_theme.json is missing — run: arc (to create defaults)")

    # 9e — banner.txt is in app/, not in root
    if (APP / "banner.txt").exists():
        ok("app/banner.txt exists")
    else:
        fail("app/banner.txt missing — was it moved out of app/?")
    if (ROOT / "banner.txt").exists():
        fail("banner.txt found in project root — should be in app/")
    else:
        ok("banner.txt not in project root (correct)")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    quiet = "--quiet" in sys.argv

    print("ARC smoke test")
    print("=" * 40)

    test_syntax()
    test_imports()
    test_registry()
    test_arg_parser()
    test_config()
    test_formatter()
    test_banner_alignment()
    test_inline_help_alignment()
    test_theme()

    print()
    print("=" * 40)
    total = _passes + len(_failures)
    if _failures:
        print(f"FAILED  {len(_failures)}/{total} checks failed\n")
        for f in _failures:
            print(f"  {FAIL}  {f}")
        return 1
    else:
        print(f"ALL OK  {_passes}/{total} checks passed")
        return 0


if __name__ == "__main__":
    sys.exit(main())

