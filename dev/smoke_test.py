#!/usr/bin/env python3
"""ARC smoke test suite.

Covers eleven concern areas:
  1. Syntax       — py_compile every Python module under app/
  2. Imports      — every module imports cleanly (no side-effect errors)
  3. Registry     — COMMANDS dict is structurally valid (no lambdas, required fields, etc.)
  4. Arg parser   — _parse_args() and match_command() return the right shapes
  5. Token opts   — KEYWORD_PARAMS is a module-level constant in registry.py
  6. Config types — ArcConfig / SCMConfig + FeatureFlags default-construct correctly
  7. Formatter    — key renderer functions accept sample data without raising
  8. CLI banner   — every banner line lands descriptions at visual column 28
  9. Inline help  — builtin names in sync via shell_catalog; no markup; width fit
 10. Theme system — ArcTheme fields, THEME_KEYS, load_theme(), file locations
 11. Code map     — dev/CODE_MAP.md is current (no line-range drift in large files)

Run directly:
    python dev/smoke_test.py

Run targeted sections (saves tokens + time when editing one area):
    python dev/smoke_test.py --only 1,2,3     # syntax + imports + registry
    python dev/smoke_test.py --only 3         # registry only (fastest after adding a command)
    python dev/smoke_test.py --file app/commands/network.py   # auto-selects sections

Run from pre-commit hook:
    python dev/smoke_test.py --quiet   (exit 0 = OK, exit 1 = failure)

File → section mapping for --file:
    commands/*.py          → 1,2,3
    utils/formatter.py     → 1,2,6
    shell.py               → 1,2,7,8
    theme.py / *.json      → 1,2,9
    config.py              → 1,2,5
    any .py                → 1,2

MAINTENANCE NOTE:
  • After any change to app/ modules → re-run to verify imports + registry.
  • After any change to the CLI banner in app/shell.py → re-run section 8.
  • After adding a new CommandDef → registry tests auto-pick it up; no edit needed.
  • After adding a new formatter function → add a minimal call in section 7.
  • After token optimization code changes → verify section 5 passes.
"""

from __future__ import annotations

import importlib
import py_compile
import re
import sys
import time
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
# --only / --file argument parsing
# ---------------------------------------------------------------------------

def _parse_cli_args() -> tuple[set[int], bool]:
    """Return (sections_to_run, quiet_mode).

    --only 1,2,3  → run only sections 1, 2, 3
    --file path   → auto-select sections based on which area the file belongs to
    --quiet       → suppress per-check output; used by pre-commit hook
    """
    args = sys.argv[1:]
    quiet = "--quiet" in args
    all_sections = set(range(1, 12))

    if "--only" in args:
        idx = args.index("--only")
        try:
            raw = args[idx + 1]
            sections = {int(s.strip()) for s in raw.split(",")}
            return sections, quiet
        except (IndexError, ValueError):
            print("Usage: --only 1,2,3", file=sys.stderr)
            sys.exit(2)

    if "--file" in args:
        idx = args.index("--file")
        try:
            path_str = args[idx + 1]
        except IndexError:
            print("Usage: --file app/commands/network.py", file=sys.stderr)
            sys.exit(2)
        path = Path(path_str)
        name = path.name
        parts = path.parts

        # Map file patterns to relevant section sets.
        # Always include 1 (syntax) and 2 (imports) for any Python file.
        # Section 11 (code-map drift) is added for files large enough to be mapped.
        base = {1, 2}
        # Files mapped in dev/CODE_MAP.md trigger the drift check too.
        _mapped_large_files = {
            "shell.py", "cli.py", "formatter.py", "client.py",
            "config.py", "setup.py", "manager.py",
        }
        map_check = {11} if name in _mapped_large_files else set()
        if "commands" in parts and name.endswith(".py"):
            return base | {3} | map_check, quiet
        if name == "formatter.py":
            return base | {7} | map_check, quiet
        if name in ("shell.py", "shell_catalog.py"):
            return base | {8, 9} | map_check, quiet
        if name in ("theme.py", "theme.json"):
            return base | {10}, quiet
        if name in ("config.py", "features.py"):
            return base | {6} | map_check, quiet
        if name == "registry.py":
            return base | {3, 4, 5}, quiet
        # Default: syntax + imports for any other .py
        return base | map_check, quiet

    return all_sections, quiet


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
        "app.features",
        "app.commands.base",
        "app.commands.setup",
        "app.commands.objects",
        "app.commands.security",
        "app.commands.network",
        "app.commands.operations",
        "app.commands.registry",
        "app.api.client",
        "app.shell_catalog",
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
# 5. Token optimization checks
# ---------------------------------------------------------------------------

def test_token_optimizations() -> None:
    section("5. Token optimization checks")

    from app.commands import registry

    # 5a — KEYWORD_PARAMS is a module-level constant (not recreated per call)
    if hasattr(registry, 'KEYWORD_PARAMS'):
        if isinstance(registry.KEYWORD_PARAMS, set):
            ok("KEYWORD_PARAMS is module-level constant (set)")
        else:
            fail("KEYWORD_PARAMS exists but is not a set", f"type: {type(registry.KEYWORD_PARAMS)}")
    else:
        fail("KEYWORD_PARAMS not found at module level in registry.py")


# ---------------------------------------------------------------------------
# 6. Config types
# ---------------------------------------------------------------------------

def test_config() -> None:
    section("6. Config types")

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

    # 6e — profile_name defaults to 'default'
    if cfg.profile_name == "default":
        ok("ArcConfig.profile_name defaults to 'default'")
    else:
        fail(f"ArcConfig.profile_name expected 'default', got {cfg.profile_name!r}")

    # 6f — load_features() returns a dict and is_enabled works
    from app.features import load_features, is_enabled
    try:
        loaded = load_features()
        if isinstance(loaded, dict):
            ok(f"load_features() returns a dict ({len(loaded)} flags)")
        else:
            fail(f"load_features() returned unexpected type: {type(loaded)}")
    except Exception as exc:
        fail("load_features() raised", str(exc))
        return
    flags = loaded

    # 6g — is_enabled: empty flag name always True
    if is_enabled(flags, ""):
        ok("is_enabled(flags, '') → True (no flag = always enabled)")
    else:
        fail("is_enabled(flags, '') should be True for empty flag name")

    # 6h — CommandDef.feature_flag field exists
    from app.commands.base import CommandDef
    cd = CommandDef(description="test", category="test", scope="folder")
    if hasattr(cd, "feature_flag") and cd.feature_flag == "":
        ok("CommandDef.feature_flag defaults to ''")
    else:
        fail("CommandDef.feature_flag missing or non-empty default")


# ---------------------------------------------------------------------------
# 7. Formatter
# ---------------------------------------------------------------------------

def test_formatter() -> None:
    section("7. Formatter")

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
# 8. CLI banner alignment
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
    section("8. CLI banner alignment  (descriptions at visual col 28)")

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
# 9. Inline help alignment
#    All command names in every ? menu section must:
#      a) contain no [markup] tags (Rich silently eats them, breaking alignment)
#      b) fit within _HELP_CMD_WIDTH chars so descriptions align on the same column
#
#    The builtins list in _print_shell_builtins() is checked by extracting it
#    from app/shell_catalog.py so builtin metadata stays in a tiny agent-friendly file.
# ---------------------------------------------------------------------------

_MARKUP_RE = re.compile(r'\[[a-zA-Z/_][^\]]*\]')


def test_inline_help_alignment() -> None:
    section("9. Inline help alignment")

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
    from app.shell_catalog import SHELL_BUILTINS, shell_help_names, shell_help_rows
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
    builtin_names = shell_help_names()
    markup_builtins = [n for n in builtin_names if _MARKUP_RE.search(n)]
    if markup_builtins:
        for n in markup_builtins:
            fail(f"Builtin name contains [markup] (breaks alignment): {n!r}")
    else:
        ok(f"No [markup] tags in any of the {len(builtin_names)} builtin names")

    oversized_builtins = [n for n in builtin_names if len(n) > cmd_width]
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
        # 'd' now expands unambiguously to 'docs' (devices builtin removed).
        # 'd' is ambiguous (docs vs delete) since 'delete' was added as a builtin — stays unexpanded
        (["d"], ["d"]),
    ]
    for raw, expected in cases:
        got = _expand_unambiguous_prefix(raw, phrases)
        if got == expected:
            ok(f"shorthand {raw!r} -> {expected!r}")
        else:
            fail(f"shorthand expansion mismatch for {raw!r}", f"expected {expected!r}, got {got!r}")

    # 9c — Verify shell.py is wired to shell_catalog source of truth.
    if tuple(_SHELL_BUILTINS) == tuple(SHELL_BUILTINS):
        ok(f"_SHELL_BUILTINS wired to shell_catalog ({len(SHELL_BUILTINS)} entries)")
    else:
        fail("_SHELL_BUILTINS differs from shell_catalog.SHELL_BUILTINS")

    # 9d — Configure-mode split is intentional: configure shows only mutation helpers.
    normal_rows = shell_help_rows(configure_mode=False)
    config_rows = shell_help_rows(configure_mode=True)
    if normal_rows and config_rows:
        ok(f"shell_help_rows() returns normal={len(normal_rows)} config={len(config_rows)} rows")
    else:
        fail("shell_help_rows() returned empty normal or configure-mode list")


# ---------------------------------------------------------------------------
# 10. Theme system
# ---------------------------------------------------------------------------

def test_theme() -> None:
    section("10. Theme system")

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

    # 9d — settings/theme.json exists
    theme_file = ROOT / "settings" / "theme.json"
    if theme_file.exists():
        ok("settings/theme.json exists")
    else:
        fail("settings/theme.json is missing")

    # 9e — user assets live in settings/, not in app/ or root
    settings = ROOT / "settings"
    for name in ("banner.txt", "goodbye.txt", "cli-structure.yaml", "features.json"):
        if (settings / name).exists():
            ok(f"settings/{name} exists")
        else:
            fail(f"settings/{name} missing — was it moved out of settings/?")
    if (APP / "banner.txt").exists() or (ROOT / "banner.txt").exists():
        fail("banner.txt should live in settings/, not app/ or root")
    else:
        ok("banner.txt correctly under settings/ only")


# ---------------------------------------------------------------------------
# 10. Code map freshness
#     dev/CODE_MAP.md is generated by dev/gen_code_map.py and gives agents the
#     exact line range of every method in large files. If it drifts, agents read
#     the wrong lines. This check fails when the map is stale so it cannot rot.
# ---------------------------------------------------------------------------

def test_code_map() -> None:
    section("11. Code map freshness")

    gen = ROOT / "dev" / "gen_code_map.py"
    code_map = ROOT / "dev" / "CODE_MAP.md"

    if not gen.exists():
        fail("dev/gen_code_map.py is missing")
        return
    ok("dev/gen_code_map.py exists")

    if not code_map.exists():
        fail("dev/CODE_MAP.md is missing — run: python dev/gen_code_map.py")
        return
    ok("dev/CODE_MAP.md exists")

    # Re-run the generator's --check mode in-process to detect drift.
    import importlib.util
    spec = importlib.util.spec_from_file_location("gen_code_map", gen)
    if spec is None or spec.loader is None:
        fail("Could not load dev/gen_code_map.py for drift check")
        return
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
        fresh = module._build_map()
        current = code_map.read_text(encoding="utf-8")
        if fresh == current:
            ok("dev/CODE_MAP.md is current (no drift)")
        else:
            fail(
                "dev/CODE_MAP.md is STALE",
                "Run: python dev/gen_code_map.py  (large file line ranges changed)",
            )
    except Exception as exc:
        fail("Code map drift check raised", str(exc))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

# Maps section number to (function, short label)
_SECTION_MAP = [
    (1, test_syntax,               "Syntax"),
    (2, test_imports,              "Imports"),
    (3, test_registry,             "Registry"),
    (4, test_arg_parser,           "Arg parser"),
    (5, test_token_optimizations,  "Token optimizations"),
    (6, test_config,               "Config types"),
    (7, test_formatter,            "Formatter"),
    (8, test_banner_alignment,     "Banner alignment"),
    (9, test_inline_help_alignment,"Inline help alignment"),
    (10, test_theme,               "Theme"),
    (11, test_code_map,            "Code map freshness"),
]


def main() -> int:
    active_sections, quiet = _parse_cli_args()

    skipped = sorted(n for n, _, _ in _SECTION_MAP if n not in active_sections)
    running = sorted(n for n, _, _ in _SECTION_MAP if n in active_sections)

    print("ARC smoke test")
    print("=" * 40)
    if skipped:
        labels = ", ".join(
            f"{n}={label}" for n, _, label in _SECTION_MAP if n in skipped
        )
        print(f"{SKIP}  Skipping sections: {labels}")
    if len(running) < len(_SECTION_MAP):
        labels = ", ".join(
            f"{n}={label}" for n, _, label in _SECTION_MAP if n in active_sections
        )
        print(f"   Running sections: {labels}")

    t_start = time.monotonic()

    for num, fn, label in _SECTION_MAP:
        if num not in active_sections:
            continue
        t0 = time.monotonic()
        fn()
        elapsed = time.monotonic() - t0
        if not quiet and elapsed > 0.5:
            print(f"   [{elapsed:.1f}s]")

    total_elapsed = time.monotonic() - t_start

    print()
    print("=" * 40)
    total = _passes + len(_failures)
    if _failures:
        print(f"FAILED  {len(_failures)}/{total} checks failed  ({total_elapsed:.1f}s)\n")
        for f in _failures:
            print(f"  {FAIL}  {f}")
        return 1
    else:
        print(f"ALL OK  {_passes}/{total} checks passed  ({total_elapsed:.1f}s)")
        if skipped:
            print(f"        ({len(skipped)} section(s) skipped — run without --only to verify all)")
        return 0


if __name__ == "__main__":
    sys.exit(main())

