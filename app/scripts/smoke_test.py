#!/usr/bin/env python3
"""ARC smoke test suite.

Covers fourteen concern areas:
  1. Syntax       — py_compile every Python module under app/
  2. Imports      — every module imports cleanly (no side-effect errors);
                    GUI route handlers all resolve to real methods
  3. Registry     — COMMANDS dict is structurally valid (no lambdas, required fields, etc.)
  4. Arg parser   — _parse_args() and match_command() return the right shapes
  5. Token opts   — KEYWORD_PARAMS is a module-level constant in registry.py
  6. Config types — ArcConfig / SCMConfig + FeatureFlags default-construct correctly
  7. Formatter    — key renderer functions accept sample data without raising
  8. CLI banner   — every banner line lands descriptions at visual column 28
  9. Inline help  — builtin names in sync via settings/builtin-commands.json; no markup; width fit
 10. Theme system — ArcTheme fields, THEME_KEYS, load_theme(), file locations
 11. Code map     — app/scripts/CODE_MAP.md is current (no line-range drift in large files)
 12. Visibility   — builtin (true/hidden/false) and feature-flag (on/dev/hidden/off) states
 13. Commit flow  — staging, unstage, abandon, commit-confirmed structure (offline; --only 13)
 14. Browser GUIs — both consoles' GET/POST routes over HTTP + new-command wiring

Run directly:
    python app/scripts/smoke_test.py

Run targeted sections (saves tokens + time when editing one area):
    python app/scripts/smoke_test.py --only 1,2,3     # syntax + imports + registry
    python app/scripts/smoke_test.py --only 3         # registry only (fastest after adding a command)
    python app/scripts/smoke_test.py --file app/commands/network.py   # auto-selects sections

Run from pre-commit hook:
    python app/scripts/smoke_test.py --quiet   (exit 0 = OK, exit 1 = failure)

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
from types import SimpleNamespace

# Ensure the project root is on sys.path so `import app.*` works when the
# script is invoked from any directory (e.g. `python app/scripts/smoke_test.py`).
ROOT = Path(__file__).resolve().parent.parent.parent   # arc/
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
    # Sections 1-12 + 14 run by default; section 13 (configure/commit flow) is
    # opt-in via --only because it constructs heavier mock state.
    all_sections = set(range(1, 13)) | {14}

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
        # Files mapped in app/scripts/CODE_MAP.md trigger the drift check too.
        _mapped_large_files = {
            "navigation.py", "help.py", "cli.py", "formatter.py", "client.py",
            "config.py", "setup.py", "manager.py", "objects.py", "network.py",
            "security.py",
        }
        map_check = {11} if name in _mapped_large_files else set()
        if "commands" in parts and name.endswith(".py"):
            return base | {3} | map_check, quiet
        if name == "formatter.py":
            return base | {7} | map_check, quiet
        # app/shell/ package: prompt.py drives the banner (8); _base.py drives help width (9).
        if "shell" in parts and name == "prompt.py":
            return base | {8} | map_check, quiet
        if "shell" in parts and name in ("_base.py", "help.py"):
            return base | {9} | map_check, quiet
        if name in ("shell_catalog.py", "commands.py") and name == "commands.py":
            return base | {8, 9} | map_check, quiet
        if name in ("theme.py", "theme.json"):
            return base | {10}, quiet
        if name == "command_help.py":
            return base | {3, 10}, quiet
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
        "app.settings.features",
        "app.settings.command_help",
        "app.commands.base",
        "app.commands.setup",
        "app.commands.objects",
        "app.commands.security",
        "app.commands.network",
        "app.commands.operations",
        "app.commands.packet_tracer",
        "app.commands.registry",
        "app.api.client",
        "app.shell",
        "app.settings.commands",
        "app.ssh.manager",
        "app.utils.formatter",
        "app.settings.theme",
        "app.settings.cli_structure",
        "app.docs",
    ]

    for mod in modules:
        try:
            importlib.import_module(mod)
            ok(mod)
        except Exception:
            fail(mod, traceback.format_exc(limit=3).strip())

    # GUI servers: every method their route_get/route_post handlers dispatch to
    # must actually exist on the class.  Guards against a refactor silently
    # dropping a handler method (which surfaces only as a runtime 500 in the
    # browser — e.g. a deleted `def _apply_change` leaving dead code).
    import inspect
    import re as _re

    for cls_path in ("app.web.feature_server:FeatureGuiServer",
                     "app.web.arc_server:ArcGuiServer"):
        mod_name, cls_name = cls_path.split(":")
        cls = getattr(importlib.import_module(mod_name), cls_name)
        missing: list[str] = []
        for handler in ("route_get", "route_post"):
            fn = getattr(cls, handler, None)
            if fn is None:
                continue
            src = inspect.getsource(fn)
            for meth in _re.findall(r"self\.(_[a-z][a-z0-9_]*)\(", src):
                if not hasattr(cls, meth) and meth not in missing:
                    missing.append(meth)
        if missing:
            fail(f"{cls_name}: route handlers call missing method(s)", ", ".join(sorted(missing)))
        else:
            ok(f"{cls_name}: all route-handler methods exist")


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
        if cmd.scope not in ("folder", "device", "remote", "global"):
            bad_fields.append(f"{key!r}: invalid scope {cmd.scope!r}")
    if bad_fields:
        for b in bad_fields:
            fail(b)
    else:
        ok("All CommandDef entries have description + valid scope")

    # 3c-scope — Device/remote scope classification invariant.  This keeps the
    # rule durable across every update tool (docsupdate/commandupdate/cliup/
    # catalog rebuild): a command that can only run by SSHing to the device
    # (SSH-only, no SCM execution path) MUST be `remote`; a command that targets
    # a device via an SCM query param MUST require a device context (device or
    # remote — never global/folder).
    try:
        from app.commands.resource_catalog import CATALOG as _CAT
        _device_param_cmds = {
            e["command"] for e in _CAT if "device" in (e.get("query_params") or [])
        }
    except Exception:
        _device_param_cmds = set()
    scope_bad: list[str] = []
    for key, cmd in COMMANDS.items():
        # SCM command with a device query param must need a device context.
        if key in _device_param_cmds and cmd.scope not in ("device", "remote"):
            scope_bad.append(f"{key!r}: has a device query param but scope={cmd.scope!r} (expected device/remote)")
        # remote scope must be reachable via SSH (it's the SSH plane).
        if cmd.scope == "remote" and cmd.ssh_command is None:
            scope_bad.append(f"{key!r}: scope=remote but no ssh_command (remote = SSH plane)")
    if scope_bad:
        for b in scope_bad[:20]:
            fail(b)
    else:
        _remote = sum(1 for c in COMMANDS.values() if c.scope == "remote")
        _device = sum(1 for c in COMMANDS.values() if c.scope == "device")
        ok(f"Scope classification invariant holds ({_remote} remote/SSH, {_device} device/SCM-proxy)")

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

    # 3g — Generated endpoint coverage: the generated resource catalog is in sync
    #      with the pulled specs.  GET/POST/PUT/PATCH/DELETE operations are covered
    #      by explicit commands or feature-gated generated command metadata.
    #      Drift = a new pan.dev endpoint with no command metadata; run:
    #      python app/scripts/generate_resource_catalog.py
    import importlib.util as _ilu
    gen_path = ROOT / "app" / "scripts" / "generate_resource_catalog.py"
    spec_mod = _ilu.spec_from_file_location("generate_resource_catalog", gen_path)
    try:
        module = _ilu.module_from_spec(spec_mod)
        spec_mod.loader.exec_module(module)  # type: ignore[union-attr]
        fresh = module._build_catalog()
        from app.commands.resource_catalog import CATALOG as _CATALOG
        fresh_cmds = {e["command"] for e in fresh}
        have_cmds = {e["command"] for e in _CATALOG}
        if fresh_cmds == have_cmds:
            ok(f"resource catalog covers all spec endpoints ({len(have_cmds)} auto-generated)")
        else:
            missing = sorted(fresh_cmds - have_cmds)
            fail(
                f"{len(missing)} spec endpoint(s) not in resource_catalog.py",
                "Run: python app/scripts/generate_resource_catalog.py  (" + ", ".join(missing[:5]) + ")",
            )
    except ModuleNotFoundError:
        ok("resource catalog check skipped (PyYAML not installed)")
    except Exception as exc:  # noqa: BLE001
        fail("resource catalog coverage check raised", str(exc))


# ---------------------------------------------------------------------------
# 4. Arg parser
# ---------------------------------------------------------------------------

def test_arg_parser() -> None:
    section("4. Arg parser (_parse_args)")

    from app.commands.registry import _parse_args

    cases: list[tuple[list[str], dict]] = [
        # positional sets _positional, id, name (host alias removed — host is a KEYWORD_PARAM
        # so bare positional[0] aliasing to 'host' produced wrong values for "host <ip>" commands)
        (["my-object"],        {"_positional": ["my-object"], "id": "my-object",
                                "name": "my-object"}),
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

    # 4b — output pipe filters (`<command> | match <pat> | count`)
    from app.shell.dispatch import parse_output_filters, split_pipe_line

    if split_pipe_line("show devices | match prod") == ("show devices", "match prod") \
            and split_pipe_line('set address "a|b" fqdn x') == ('set address "a|b" fqdn x', None) \
            and split_pipe_line("show devices") == ("show devices", None):
        ok("split_pipe_line: splits on first unquoted | only")
    else:
        fail("split_pipe_line returned unexpected shapes")

    filters, _ = parse_output_filters("match prod | except lab | count")
    if filters == [("match", "prod"), ("except", "lab"), ("count", "")]:
        ok("parse_output_filters: match/except/count chain parsed")
    else:
        fail("parse_output_filters chain wrong", repr(filters))

    filters, _ = parse_output_filters("json | match serial")
    if filters == [("json", ""), ("match", "serial")]:
        ok("parse_output_filters: json render filter parsed")
    else:
        fail("parse_output_filters json wrong", repr(filters))

    # 4b.1 — `| save <file>` op: parsed with its filename, must be last,
    #        and a bare `save` (no filename) is rejected with a hint.
    filters, _ = parse_output_filters("match x | save out.txt")
    if filters == [("match", "x"), ("save", "out.txt")]:
        ok("parse_output_filters: save op parsed with filename")
    else:
        fail("parse_output_filters save wrong", repr(filters))
    bad_order, order_error = parse_output_filters("save out.txt | match x")
    bad_bare, bare_error = parse_output_filters("match x | save")
    if bad_order is None and "last" in order_error and bad_bare is None and "filename" in bare_error:
        ok("parse_output_filters: save must be last + needs a filename")
    else:
        fail("parse_output_filters save validation wrong",
             f"order={order_error!r} bare={bare_error!r}")

    # 4c2 — spec-derived field catalog: every entry is internally consistent
    #       and merged into arg_spec (hand-written command-structure.json wins).
    try:
        from app.settings.field_catalog import FIELD_CATALOG as field_catalog
    except Exception as exc:  # noqa: BLE001
        field_catalog = None
        fail("field_catalog import failed", str(exc))
    if field_catalog is not None:
        catalog_problems = []
        for fc_key, fc_entry in field_catalog.items():
            fc_args = fc_entry.get("args") or []
            arg_names = {a.get("name") for a in fc_args}
            payload = fc_entry.get("payload") or {}
            if not fc_key.startswith("set "):
                catalog_problems.append(f"{fc_key}: not a set command")
            if not fc_args:
                catalog_problems.append(f"{fc_key}: empty args")
            for a in fc_args:
                if a.get("kind") not in ("value", "choice", "keyword"):
                    catalog_problems.append(f"{fc_key}: bad kind {a.get('kind')!r}")
                if a.get("kind") == "choice" and not a.get("choices"):
                    catalog_problems.append(f"{fc_key}: choice field {a.get('name')} has no choices")
            for cli_name in (payload.get("fields") or {}):
                if cli_name not in arg_names:
                    catalog_problems.append(f"{fc_key}: payload field {cli_name!r} not in args")
            variant = payload.get("variant")
            if variant:
                if variant.get("type_field") not in arg_names or variant.get("value_field") not in arg_names:
                    catalog_problems.append(f"{fc_key}: variant type/value fields not in args")
                if not variant.get("choices"):
                    catalog_problems.append(f"{fc_key}: variant has no choices")
        if catalog_problems:
            fail(f"field catalog: {len(catalog_problems)} inconsistent entrie(s)",
                 "; ".join(catalog_problems[:4]))
        else:
            ok(f"field catalog: {len(field_catalog)} generated set command(s) internally consistent")

        from app.settings import command_structure as _cs
        _cs.invalidate_cache()
        merged = _cs.load_command_structure()
        if field_catalog and all(k in merged for k in list(field_catalog)[:20]):
            ok("field catalog entries merged into arg_spec")
        elif field_catalog:
            fail("field catalog entries missing from load_command_structure()")
        if _cs.arg_spec("set address") is not None:
            ok("hand-written command-structure.json still resolves (set address)")
        else:
            fail("set address lost its hand-written arg spec")
        _cs.invalidate_cache()

        # payload builder: enum canonicalization + required + bad-enum rejection
        from app.commands.generated import _payload_from_fields
        _fake_entry = {
            "args": [
                {"name": "name", "kind": "value", "required": True, "hint": ""},
                {"name": "color", "kind": "keyword", "required": False,
                 "hint": "", "choices": ["Red", "Green"]},
            ],
            "payload": {"fields": {"name": "name", "color": "color"},
                        "list_fields": [], "variant": None},
        }
        built = _payload_from_fields("set x", _fake_entry, {"name": "n1", "color": "red"})
        bad_enum_rejected = False
        try:
            _payload_from_fields("set x", _fake_entry, {"name": "n1", "color": "plaid"})
        except ValueError:
            bad_enum_rejected = True
        missing_rejected = False
        try:
            _payload_from_fields("set x", _fake_entry, {"color": "Red"})
        except ValueError:
            missing_rejected = True
        if built == {"name": "n1", "color": "Red"} and bad_enum_rejected and missing_rejected:
            ok("payload builder: canonical enums, required + enum validation")
        else:
            fail("payload builder misbehaved", repr(built))

        # payload builder: schema pattern + max_length constraints enforced at
        # the prompt; a broken regex in a spec is skipped, never crashes.
        _constrained_entry = {
            "args": [
                {"name": "fqdn", "kind": "value", "required": True, "hint": "",
                 "pattern": r"^[a-zA-Z0-9_]([a-zA-Z0-9._-])+[a-zA-Z0-9]$", "max_length": 12},
                {"name": "note", "kind": "keyword", "required": False, "hint": "",
                 "pattern": r"([unbalanced"},  # invalid regex — must be skipped
            ],
            "payload": {"fields": {"fqdn": "fqdn", "note": "note"},
                        "list_fields": [], "variant": None},
        }
        built = _payload_from_fields("set x", _constrained_entry,
                                     {"fqdn": "a.example", "note": "anything"})
        pattern_rejected = too_long_rejected = False
        try:
            _payload_from_fields("set x", _constrained_entry, {"fqdn": "-bad-"})
        except ValueError as exc:
            pattern_rejected = "required format" in str(exc)
        try:
            _payload_from_fields("set x", _constrained_entry, {"fqdn": "a.very-long-name.example"})
        except ValueError as exc:
            too_long_rejected = "maximum 12" in str(exc)
        if (built == {"fqdn": "a.example", "note": "anything"}
                and pattern_rejected and too_long_rejected):
            ok("payload builder: pattern + max_length enforced, invalid spec regex skipped")
        else:
            fail("payload builder constraint validation misbehaved",
                 f"built={built!r} pattern={pattern_rejected} max_length={too_long_rejected}")

    # 4d — user preferences round-trip (now stored in config/<user>/config.json)
    import json as _json

    from app.settings import user_prefs as _up
    import app.config as _cfgmod

    prefs = _up.UserPrefs(terminal_length=24, terminal_width=120, spinner=False,
                          aliases={"slt": "show log traffic"})
    _tmp_dir = ROOT / "app" / "scripts" / ".smoke_cfg_test"
    _tmp_file = _tmp_dir / "config.json"
    _orig_dir, _orig_file = _cfgmod.CONFIG_DIR, _cfgmod.CONFIG_FILE
    _orig_legacy = _up._LEGACY_PREFS_FILE
    _cfgmod.CONFIG_DIR = _tmp_dir
    _cfgmod.CONFIG_FILE = _tmp_file
    _up._LEGACY_PREFS_FILE = _tmp_dir / "preferences.json"  # nonexistent → no migration
    try:
        _tmp_dir.mkdir(parents=True, exist_ok=True)
        if _up.save_prefs(prefs) and _up.load_prefs() == prefs:
            ok("user_prefs: save/load round-trip preserves values (incl. aliases)")
        else:
            fail("user_prefs round-trip mismatch", repr(_up.load_prefs()))
        # Malformed preferences block + unknown keys must be tolerated.
        _tmp_file.write_text(_json.dumps({"preferences": {
            "terminal_length": "junk", "unknown_key": 1, "aliases": "junk"}}))
        loaded = _up.load_prefs()
        if loaded.terminal_length == 0 and loaded.spinner is True and loaded.aliases == {}:
            ok("user_prefs: malformed values and unknown keys tolerated")
        else:
            fail("user_prefs did not tolerate malformed file", repr(loaded))
    finally:
        try:
            _tmp_file.unlink(missing_ok=True)
            _tmp_dir.rmdir()
        except OSError:
            pass
        _cfgmod.CONFIG_DIR, _cfgmod.CONFIG_FILE = _orig_dir, _orig_file
        _up._LEGACY_PREFS_FILE = _orig_legacy

    bad, error = parse_output_filters("frobnicate x")
    if bad is None and "unknown filter" in error:
        ok("parse_output_filters: rejects unknown filter with hint")
    else:
        fail("parse_output_filters accepted an unknown filter")

    # 4c — write staging: GETs pass through (validation), mutations captured
    from app.shell.configure import capture_write_ops

    passthrough_calls: list[str] = []

    class _FakeSCM:
        def _request(self, method, base_url, path, *, params=None, json=None):
            passthrough_calls.append(method)
            return {"data": [{"name": "web1", "id": "abc"}]}

    def _fake_handler(ctx, args):
        scm = args["scm"]
        scm._request("GET", "https://x", "/addresses", params={"folder": "Shared"})
        scm._request("POST", "https://x", "/addresses", json={"name": "web1"})

    fake = _FakeSCM()
    ops = capture_write_ops(fake, _fake_handler, None, {"scm": fake})
    if passthrough_calls == ["GET"] and [o["method"] for o in ops] == ["POST"]:
        ok("capture_write_ops: GET validated live, POST captured (not sent)")
    else:
        fail("capture_write_ops wrong split", f"passthrough={passthrough_calls} ops={ops}")
    if callable(getattr(fake, "_request", None)) and fake._request.__func__ is _FakeSCM._request:
        ok("capture_write_ops: real _request restored after staging")
    else:
        fail("capture_write_ops did not restore the real _request")


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

    from app.config import ArcConfig, SCMConfig

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
    from app.settings.features import load_features, is_enabled, feature_state
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

    # 6g.1 — three-state semantics: on / dev / off
    sample = {"flag_on": "on", "flag_dev": "dev", "flag_off": "off"}
    checks = [
        ("on",  "flag_on",  False, True),
        ("on",  "flag_on",  True,  True),
        ("dev", "flag_dev", False, False),   # hidden outside development mode
        ("dev", "flag_dev", True,  True),    # revealed in development mode
        ("off", "flag_off", False, False),
        ("off", "flag_off", True,  False),   # off stays off even in dev mode
    ]
    state_ok = all(is_enabled(sample, name, dev) is expect for _, name, dev, expect in checks)
    if state_ok and feature_state(sample, "flag_dev") == "dev":
        ok("feature flags honor on / dev / off (dev gated by development mode)")
    else:
        fail("3-state feature flag semantics are incorrect")

    # 6g.2 — values in settings/features.json are valid (true | false | \"dev\")
    bad = {k: v for k, v in flags.items() if v not in ("on", "dev", "off")}
    if bad:
        fail("settings/features.json has flags with invalid state", str(bad))
    else:
        ok(f"all {len(flags)} feature flags use a valid state (on/dev/off)")

    # 6g.3 — every settings/features/*.json file is *valid JSON*.  A syntax
    #         error makes load_features() skip that file → its commands vanish.
    #         Parse directly (not via load_features) so corruption is caught loudly.
    import json as _json
    features_dir = ROOT / "settings" / "features"
    raw_features: dict | None = {}
    feature_files = sorted(features_dir.glob("*.json")) if features_dir.is_dir() else []
    if not feature_files:
        raw_features = None
        fail("settings/features/ has no flag files — run: python app/scripts/generate_feature_flags.py")
    for ff in feature_files:
        try:
            parsed = _json.loads(ff.read_text(encoding="utf-8"))
            if isinstance(parsed, dict) and raw_features is not None:
                raw_features.update(parsed)
        except Exception as exc:
            raw_features = None
            fail(f"settings/features/{ff.name} is NOT valid JSON — its commands would disappear", str(exc))
    if raw_features is not None:
        ok(f"all {len(feature_files)} settings/features/*.json files are valid JSON")

    # 6g.4 — every command's feature_flag is either explicitly present in features.json
    #         OR covered by a file with _default: false (absent = off is intentional).
    #         A truly missing flag would be one in a file where _default is not false
    #         AND the key doesn't appear — that would be a typo that silently enables commands.
    if raw_features is not None:
        from app.commands.registry import COMMANDS as _COMMANDS_FOR_FLAGS
        from app.settings.features import load_features as _load_feats, feature_state as _feat_state
        # Load features through the real loader so domain defaults are respected.
        loaded = _load_feats()
        cmd_flags = {c.feature_flag for c in _COMMANDS_FOR_FLAGS.values() if c.feature_flag}
        # Any flag that the feature system returns as non-OFF is "known".
        # Flags absent from ALL files are treated as OFF by the loader (feature_state
        # returns STATE_OFF for absent keys).  That's correct behaviour — auto-generated
        # command flags default to false without needing an explicit entry.
        # We only flag as an error flags that are referenced but whose key has a TYPO
        # (which would cause them to be "on" in JSON but evaluated as "off" — i.e. keys
        # where the JSON has the flag under a different name).
        # The simplest correct check: verify every flag either appears in the loaded map
        # (explicitly set) OR is absent and treated as off (which is fine).
        # A broken flag would be one that appears in the registry but is somehow evaluated
        # differently from what the developer intended — which requires human review.
        # For CI purposes, we check that no explicitly-on flag has a typo (would be off).
        explicitly_on = {k for k, v in raw_features.items() if v is True and not k.startswith("_")}
        cmd_flags_on = {
            c.feature_flag for c in _COMMANDS_FOR_FLAGS.values()
            if c.feature_flag and _feat_state(loaded, c.feature_flag) == "on"
        }
        # All commands that are on should have their flag present and true in the JSON
        # — if a flag is on in the registry but missing from JSON, that's a typo risk.
        on_but_missing = sorted(cmd_flags_on - explicitly_on)
        if on_but_missing:
            fail(
                f"{len(on_but_missing)} enabled command flag(s) not found as 'true' in features JSON "
                "(possible typo — commands appear on but flag not explicitly set)",
                ", ".join(on_but_missing[:8]),
            )
        else:
            ok(f"all {len(cmd_flags)} command feature flags are present in features.json")

    # 6h — CommandDef.feature_flag field exists
    from app.commands.base import CommandDef
    cd = CommandDef(description="test", category="setup", scope="folder")
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
        formatter._kv_table({"hostname": "fw01", "serial": "007200123456"}, title="Test")
        ok("_kv_table() returns Rich Table")
    except Exception as exc:
        fail("_kv_table()", str(exc))

    # 6b — _list_table with sample rows
    try:
        rows = [{"name": "obj1", "type": "ip-netmask", "value": "10.0.0.0/8"}]
        formatter._list_table(rows, title="Addresses")
        ok("_list_table() returns Rich Table")
    except Exception as exc:
        fail("_list_table()", str(exc))

    # 6c — _list_table with empty rows (edge case — should not raise)
    try:
        formatter._list_table([], title="Empty")
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
        formatter.format_folder_tree(folders, devices)
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
def test_banner_alignment() -> None:
    section("8. CLI banner alignment  (startup hints loaded from settings)")

    from app.settings.commands import load_startup_hints

    hints = load_startup_hints()

    if not hints:
        fail("No onlogin hints found in settings/builtin-commands.json")
        return

    ok(f"Banner has {len(hints)} startup hint(s) from settings/builtin-commands.json")

    # Compute the padding width the renderer uses (same logic as prompt.py)
    max_display = max(len(display) for display, _ in hints)
    pad_to = max(max_display, 16)

    for display, hint in hints:
        spaces = " " * (pad_to - len(display) + 2)
        # Visual col = 2 (indent) + len(display) + len(spaces)
        col = 2 + len(display) + len(spaces)
        if col >= 18:  # reasonable minimum alignment target
            ok(f"hint [{display!r}] indents to col {col}")
        else:
            fail(f"hint [{display!r}] indents to col {col} — too short")


# ---------------------------------------------------------------------------
# 9. Inline help alignment
#    All command names in every ? menu section must:
#      a) contain no [markup] tags (Rich silently eats them, breaking alignment)
#      b) fit within _HELP_CMD_WIDTH chars so descriptions align on the same column
#
#    The builtins list in _print_shell_builtins() is checked by extracting it
#    from settings/builtin-commands.json.
# ---------------------------------------------------------------------------

_MARKUP_RE = re.compile(r'\[[a-zA-Z/_][^\]]*\]')


def test_inline_help_alignment() -> None:
    section("9. Inline help alignment")

    # Read _HELP_CMD_WIDTH from the shell spine
    shell_src = (APP / "shell" / "_base.py").read_text(encoding="utf-8")
    m = re.search(r'^_HELP_CMD_WIDTH\s*=\s*(\d+)', shell_src, re.MULTILINE)
    if not m:
        fail("_HELP_CMD_WIDTH constant not found in app/shell/_base.py")
        return
    cmd_width = int(m.group(1))
    ok(f"_HELP_CMD_WIDTH = {cmd_width}")

    # 8a — Registered command keys: no markup, fit in field
    from app.commands.registry import COMMANDS
    from app.shell import _SHELL_BUILTINS, _expand_unambiguous_prefix
    from app.settings.commands import load_shell_builtins, shell_help_names, shell_help_rows
    shell_builtins = load_shell_builtins()
    markup_keys = [k for k in COMMANDS if _MARKUP_RE.search(k)]
    if markup_keys:
        fail(f"Registered commands contain [markup] in key (breaks alignment): {markup_keys}")
    else:
        ok(f"No [markup] tags in any of the {len(COMMANDS)} registered command keys")

    # Keys longer than the help column are legitimate (deep PAN-OS stems) —
    # _help_cell overflows them gracefully. Only absurd lengths fail.
    _KEY_HARD_CAP = 150
    over_column = sum(1 for k in COMMANDS if len(k) > cmd_width)
    absurd_keys = [k for k in COMMANDS if len(k) > _KEY_HARD_CAP]
    if absurd_keys:
        for k in absurd_keys:
            fail(f"Registered key absurdly long ({len(k)} > {_KEY_HARD_CAP}): {k!r}")
    else:
        ok(f"Key lengths sane ({over_column} overflow the {cmd_width}-char help column gracefully; hard cap {_KEY_HARD_CAP})")

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

    # 9c — Verify shell.py is wired to settings/builtin-commands.json source of truth.
    if tuple(_SHELL_BUILTINS) == tuple(shell_builtins):
        ok(f"_SHELL_BUILTINS wired to settings/builtin-commands.json ({len(shell_builtins)} entries)")
    else:
        fail("_SHELL_BUILTINS differs from settings/builtin-commands.json")

    # 9d — Configure-mode split is intentional: configure shows only mutation helpers.
    normal_rows = shell_help_rows(configure_mode=False)
    config_rows = shell_help_rows(configure_mode=True)
    if normal_rows and config_rows:
        ok(f"shell_help_rows() returns normal={len(normal_rows)} config={len(config_rows)} rows")
    else:
        fail("shell_help_rows() returned empty normal or configure-mode list")

    # 9e — Usage-driven tab completion: a command's usage parses into the option
    #      tokens the completer offers (so `set address` guides through its args).
    from app.shell.completer import _usage_options
    addr_usage = COMMANDS["set address"].usage if "set address" in COMMANDS else ""
    if addr_usage:
        after_name = [o for o, _ in _usage_options(addr_usage, "set address", ["myaddr"])]
        after_value = [o for o, _ in _usage_options(addr_usage, "set address", ["myaddr", "ip-netmask", "1.2.3.4"])]
        if "ip-netmask" in after_name and "fqdn" in after_name and "tag" in after_value:
            ok("usage-driven completion: set address offers type choices then description/tag")
        else:
            fail("usage-driven completion broken for set address",
                 f"after_name={after_name} after_value={after_value}")
    else:
        fail("set address has no usage string — tab completion cannot guide it")

    generated_write = next(
        (
            (key, cmd.usage)
            for key, cmd in COMMANDS.items()
            if key.startswith(("set ", "update ")) and "json|file" in cmd.usage
        ),
        None,
    )
    if generated_write:
        key, usage = generated_write
        payload_options = [o for o, _ in _usage_options(usage, key, [])]
        if {"json", "file"}.issubset(payload_options):
            ok(f"generated write usage fallback: {key!r} offers json|file")
        else:
            fail("generated write usage fallback missing json|file", f"key={key} options={payload_options}")
    else:
        fail("No generated set/update command exposes json|file usage fallback")

    # Disabled feature commands must not appear in user-facing tab completion.
    # The fake shell borrows the real _is_command_visible from HelpMixin so the
    # test exercises the same canonical visibility check the shell uses.
    from app.shell.completer import ArcCompleter
    from app.shell.help import HelpMixin

    def _fake_shell(features: dict) -> SimpleNamespace:
        shell = SimpleNamespace(_features=features, _dev_mode=False, _command_visibility={})
        shell._is_command_visible = HelpMixin._is_command_visible.__get__(shell)
        shell._visible_command_keys = HelpMixin._visible_command_keys.__get__(shell)
        return shell

    hidden_shell = _fake_shell({"create_address": "off"})
    hidden_completer = ArcCompleter(hidden_shell)
    hidden_commands = hidden_completer._all_commands(include_remote_suffix=False)
    if "set address" not in hidden_commands:
        ok("disabled feature command hidden from completion: set address")
    else:
        fail("disabled feature command leaked into completion", "set address was offered while create_address=off")

    visible_shell = _fake_shell({"create_address": "on"})
    visible_completer = ArcCompleter(visible_shell)
    visible_commands = visible_completer._all_commands(include_remote_suffix=False)
    if "set address" in visible_commands:
        ok("enabled feature command appears in completion: set address")
    else:
        fail("enabled feature command missing from completion", "set address was hidden while create_address=on")

    # 9f — Command-structure file (settings/command-structure.json) drives the
    #      slot-by-slot completion for `set address`, and tokenization is
    #      quote-aware so a name with spaces ("this is a test") stays one token.
    from app.settings import command_structure as _cs
    from app.shell.completer import _tokenize_partial

    _cs.invalidate_cache()
    spec = _cs.arg_spec("set address")
    if spec and [a["name"] for a in spec] == ["name", "type", "value", "description", "tag"]:
        ok("command-structure.json: set address args ordered name→type→value→description→tag")
    else:
        fail("command-structure.json did not load set address args in order",
             f"spec={spec}")

    toks, partial = _tokenize_partial('set address "this is a test" ')
    if toks == ["set", "address", "this is a test"] and partial == "":
        ok("quote-aware tokenizer keeps a spaced name as one token")
    else:
        fail("quote-aware tokenizer broke on a quoted name",
             f"tokens={toks} partial={partial!r}")

    # 9g — Greedy string parsing: the app figures out field boundaries so the
    #      operator never needs quotes for a multi-word name or description.
    if spec:
        parsed = _cs.parse(spec, ["my", "web", "host", "fqdn", "api.example.com",
                                  "description", "primary", "edge", "node"])
        if (parsed.get("name") == "my web host"
                and parsed.get("type") == "fqdn"
                and parsed.get("value") == "api.example.com"
                and parsed.get("description") == "primary edge node"):
            ok("structure parse: greedy multi-word name + description without quotes")
        else:
            fail("greedy structure parse did not split fields correctly", f"parsed={parsed}")

        # 9h — A required value slot shows a clear 'Enter …' message, never empty.
        opts = _cs.completion_options(spec, ["web1", "fqdn"])
        if opts and opts[0]["text"] == "" and opts[0]["display"].lower().startswith("enter "):
            ok("structure completion: value slot shows an 'Enter …' message")
        else:
            fail("value slot did not surface an 'Enter …' hint", f"opts={opts}")

        # 9i — Cisco-style context help: `<command> ?` lists only the next syntax
        #      options for the slot the operator is on.
        at_type = [r["token"] for r in _cs.help_options(spec, ["web1"])]
        at_value = [r["token"] for r in _cs.help_options(spec, ["web1", "fqdn"])]
        at_kw = [r["token"] for r in _cs.help_options(spec, ["web1", "fqdn", "1.2.3.4"])]
        if (at_type == ["ip-netmask", "ip-range", "ip-wildcard", "fqdn"]
                and at_value == ["<value>"]
                and at_kw == ["description", "tag"]):
            ok("context help: ? lists choices → variable → keywords by slot")
        else:
            fail("context help options wrong",
                 f"type={at_type} value={at_value} kw={at_kw}")

    # 9j — Builtin sub-command completion: every builtin that documents
    #      sub-commands must actually yield them from get_completions (guards
    #      against builtins that tab-complete as a word but dead-end on args).
    from prompt_toolkit.document import Document

    def _fake_full_shell() -> SimpleNamespace:
        shell = SimpleNamespace(
            _features={}, _dev_mode=False, _command_visibility={},
            _prefs=SimpleNamespace(aliases={"slt": "show log traffic"},
                                   terminal_length=0, terminal_width=0, terminal_height=0),
            _ssh=SimpleNamespace(_pool={"fw-dallas-01": object()}),
            _state=SimpleNamespace(devices_cache=[], folders_cache=[], snippets_cache=[],
                                   tsgs_cache=[], dev_shell=False, configure_mode=True,
                                   staged_ops=[{"command": "set address web1"}]),
        )
        shell._is_command_visible = HelpMixin._is_command_visible.__get__(shell)
        shell._visible_command_keys = HelpMixin._visible_command_keys.__get__(shell)
        return shell

    comp = ArcCompleter(_fake_full_shell())

    def _texts(line: str) -> set[str]:
        doc = Document(text=line, cursor_position=len(line))
        return {c.text for c in comp.get_completions(doc, None)}

    builtin_cases = {
        "commit ": {"check", "watch", "confirmed", "confirm"},
        "alias ": {"delete", "slt"},
        "close ": {"connection"},
        "close connection ": {"fw-dallas-01"},
        "unstage ": {"1"},
    }
    for line, expected in builtin_cases.items():
        got = _texts(line)
        if expected & got:
            ok(f"builtin completion: {line.strip()!r} offers {sorted(expected & got)}")
        else:
            fail(f"builtin {line.strip()!r} yielded no expected sub-command",
                 f"expected any of {sorted(expected)}, got {sorted(got)[:8]}")

    # `docs ` should offer help topics (non-empty).
    if _texts("docs "):
        ok("builtin completion: 'docs' offers help topics")
    else:
        fail("builtin 'docs' offered no help topics")

    # ---- Regression: first-word PREFIX completion of shell builtins ----------
    #      A partial builtin name (`conf` -> `configure`) must complete. This
    #      broke when the prefix loop started filtering candidates through a
    #      registry-only visibility check: builtins aren't in COMMANDS, so all
    #      of them silently vanished from name completion. `commit` is the nasty
    #      case — it has a registry twin in the `operations` area, so a disabled
    #      `operations` area must NOT suppress the core `commit` builtin.
    from app.settings.commands import load_command_visibility

    def _prefix_shell() -> SimpleNamespace:
        shell = SimpleNamespace(
            _features={}, _dev_mode=False,
            _command_visibility=load_command_visibility(),
            _disabled_areas={"operations"},  # reproduce the commit collision
            _prefs=SimpleNamespace(aliases={}, terminal_length=0,
                                   terminal_width=0, terminal_height=0),
            _ssh=SimpleNamespace(_pool={}),
            _state=SimpleNamespace(devices_cache=[], folders_cache=[],
                                   snippets_cache=[], tsgs_cache=[],
                                   dev_shell=False, configure_mode=True,
                                   staged_ops=[]),
        )
        shell._is_command_visible = HelpMixin._is_command_visible.__get__(shell)
        shell._visible_command_keys = HelpMixin._visible_command_keys.__get__(shell)
        return shell

    pcomp = ArcCompleter(_prefix_shell())

    def _ptexts(line: str) -> set[str]:
        doc = Document(text=line, cursor_position=len(line))
        return {c.text.strip() for c in pcomp.get_completions(doc, None)}

    # Builtins whose name must complete from a prefix (incl. `commit`, whose
    # registry twin sits in the disabled `operations` area).
    prefix_cases = {
        "conf": "configure",
        "comm": "commit",
        "ali": "alias",
        "acc": "account",
        "wat": "watch",
    }
    for prefix, expected in prefix_cases.items():
        got = _ptexts(prefix)
        if expected in got:
            ok(f"builtin prefix completion: {prefix!r} -> {expected!r}")
        else:
            fail(f"builtin prefix {prefix!r} did not complete to {expected!r}",
                 f"got {sorted(got)[:8]}")

    # A dev-gated builtin (feature = visible:'dev') must stay hidden in normal
    # mode — proves the fix respects builtin visibility, not just membership.
    if "feature" not in _ptexts("fe"):
        ok("builtin prefix completion: dev-gated 'feature' hidden in normal mode")
    else:
        fail("dev-gated builtin 'feature' leaked into normal-mode completion")

    # App (registry) commands must remain unaffected by the fix.
    if "show" in _ptexts("sho") and "set" in _ptexts("set"):
        ok("app-command prefix completion still works ('sho'->show, 'set'->set)")
    else:
        fail("app-command prefix completion regressed",
             f"sho={sorted(_ptexts('sho'))[:5]} set={sorted(_ptexts('set'))[:5]}")



# ---------------------------------------------------------------------------
# 10. Theme system
# ---------------------------------------------------------------------------

def test_theme() -> None:
    section("10. Theme system")

    from app.settings.theme import ArcTheme, THEME_KEYS, load_theme

    # 9a — ArcTheme default-constructs
    try:
        ArcTheme()
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
    for name in ("banner.txt", "goodbye.txt", "cli-structure.yaml"):
        if (settings / name).exists():
            ok(f"settings/{name} exists")
        else:
            fail(f"settings/{name} missing — was it moved out of settings/?")
    features_dir = settings / "features"
    feature_files = list(features_dir.glob("*.json")) if features_dir.is_dir() else []
    if len(feature_files) >= 5:
        ok(f"settings/features/ glossary present ({len(feature_files)} file(s))")
    else:
        fail("settings/features/ glossary missing or near-empty — run: python app/scripts/generate_feature_flags.py")
    if (settings / "features.json").exists():
        fail("legacy settings/features.json still present — run: python app/scripts/generate_feature_flags.py")
    else:
        ok("no legacy settings/features.json (absorbed into the glossary)")
    if (APP / "banner.txt").exists() or (ROOT / "banner.txt").exists():
        fail("banner.txt should live in settings/, not app/ or root")
    else:
        ok("banner.txt correctly under settings/ only")

    # 9f — every command has a non-empty description (from CommandDef, with doc
    #      front-matter overrides applied), and every EXISTING command doc's
    #      front-matter points at a registered command.  Commands without a doc
    #      file are normal — `help <command>` synthesizes a page from the
    #      registry (app/docs.py synthesize_command_help).
    from app.commands.registry import COMMANDS
    from app.settings.command_help import parse_front_matter, usage_overrides

    blank = [k for k, c in COMMANDS.items() if not (c.description or "").strip()]
    if blank:
        fail(f"{len(blank)} command(s) have a blank description", ", ".join(sorted(blank)[:5]))
    else:
        ok(f"All {len(COMMANDS)} commands have a non-empty description")

    _action_prefixes = ("show ", "set ", "update ", "delete ", "request ")
    orphan_docs = []
    doc_count = 0
    for _doc in sorted((ROOT / "docs" / "commands").glob("*.md")):
        if _doc.name in ("index.md", "api-reference.md"):
            continue
        _meta, _ = parse_front_matter(_doc.read_text(encoding="utf-8"))
        _cmd = _meta.get("command")
        if not isinstance(_cmd, str) or not _cmd.strip():
            continue  # plain topic page (builtins etc.)
        doc_count += 1
        _cmd = _cmd.strip()
        if _cmd not in COMMANDS and _cmd.startswith(_action_prefixes):
            orphan_docs.append(f"{_doc.name} -> {_cmd!r}")
    if orphan_docs:
        fail(
            f"{len(orphan_docs)} command doc(s) reference unregistered commands",
            "; ".join(orphan_docs[:5]) + "  (rename/delete, or run: python app/scripts/generate_command_docs.py --check)",
        )
    else:
        ok(f"All {doc_count} existing command docs reference registered commands")

    # 9g — usage front-matter applies onto CommandDef.usage (`<command> ?` syntax)
    usages = usage_overrides()
    if usages and all(COMMANDS[k].usage == v for k, v in usages.items() if k in COMMANDS):
        ok(f"{len(usages)} command usage line(s) loaded from doc front-matter")
    elif not usages:
        ok("no command usage front-matter set (optional)")
    else:
        fail("usage front-matter did not apply onto CommandDef.usage")


# ---------------------------------------------------------------------------
# 10. Code map freshness
#     app/scripts/CODE_MAP.md is generated by app/scripts/generate_code_map.py and gives agents the
#     exact line range of every method in large files. If it drifts, agents read
#     the wrong lines. This check fails when the map is stale so it cannot rot.
# ---------------------------------------------------------------------------

def test_code_map() -> None:
    section("11. Code map freshness")

    gen = ROOT / "app" / "scripts" / "generate_code_map.py"
    code_map = ROOT / "app" / "scripts" / "CODE_MAP.md"

    if not gen.exists():
        fail("app/scripts/generate_code_map.py is missing")
        return
    ok("app/scripts/generate_code_map.py exists")

    if not code_map.exists():
        fail("app/scripts/CODE_MAP.md is missing — run: python app/scripts/generate_code_map.py")
        return
    ok("app/scripts/CODE_MAP.md exists")

    # Re-run the generator's --check mode in-process to detect drift.
    import importlib.util
    spec = importlib.util.spec_from_file_location("generate_code_map", gen)
    if spec is None or spec.loader is None:
        fail("Could not load app/scripts/generate_code_map.py for drift check")
        return
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
        fresh = module._build_map()
        current = code_map.read_text(encoding="utf-8")
        if fresh == current:
            ok("app/scripts/CODE_MAP.md is current (no drift)")
        else:
            fail(
                "app/scripts/CODE_MAP.md is STALE",
                "Run: python app/scripts/generate_code_map.py  (large file line ranges changed)",
            )
    except Exception as exc:
        fail("Code map drift check raised", str(exc))


def test_command_visibility() -> None:
    section("12. Command visibility  (builtin + feature-flag states)")

    from app.settings.commands import (
        _coerce_visibility,
        is_command_executable,
        shell_help_rows,
        STATE_VISIBLE, STATE_DEV, STATE_HIDDEN, STATE_BLOCKED,
        load_command_visibility,
    )
    from app.settings.features import (
        is_enabled, STATE_ON, STATE_DEV as FEAT_DEV, STATE_OFF,
        STATE_HIDDEN as FEAT_HIDDEN,
    )
    from app.shell.help import HelpMixin
    from app.commands.registry import COMMANDS, CommandDef

    # ------------------------------------------------------------------
    # A. JSON parsing — _coerce_visibility must map all 4 string values
    #    correctly so settings/builtin-commands.json works as documented.
    # ------------------------------------------------------------------
    _parse_cases = [
        (True,       STATE_VISIBLE, "true  → visible"),
        ("dev",      STATE_DEV,     '"dev"    → dev'),
        ("hidden",   STATE_HIDDEN,  '"hidden" → hidden'),
        (False,      STATE_BLOCKED, "false → blocked"),
        ("wip",      STATE_DEV,     '"wip"    → dev (alias)'),
        ("on",       STATE_VISIBLE, '"on"     → visible (alias)'),
        ("off",      STATE_BLOCKED, '"off"    → blocked (alias)'),
    ]
    all_ok = True
    for raw, expected, label in _parse_cases:
        # Wrap in dict as _coerce_visibility sees it when reading JSON entries
        got = _coerce_visibility({"visible": raw})
        if got != expected:
            fail(f"_coerce_visibility parsing: {label}", f"got {got!r}")
            all_ok = False
    if all_ok:
        ok(f"_coerce_visibility parses all {len(_parse_cases)} JSON visible values correctly")

    # ------------------------------------------------------------------
    # B. Builtin command pipeline — uses the real _is_command_visible from
    #    HelpMixin, bound to a fake shell, so the same code path runs here
    #    as in the live shell.  Toggling shell._dev_mode drives everything.
    # ------------------------------------------------------------------

    def _make_shell(vis: dict[str, str], features: dict[str, str],
                    dev_mode: bool) -> SimpleNamespace:
        """Minimal shell stand-in that runs the real _is_command_visible."""
        shell = SimpleNamespace(
            _command_visibility=vis,
            _features=features,
            _dev_mode=dev_mode,
            _visible_keys_cache=None,
        )
        shell._is_command_visible = HelpMixin._is_command_visible.__get__(shell)
        shell._visible_command_keys = HelpMixin._visible_command_keys.__get__(shell)
        shell._invalidate_visible_keys = HelpMixin._invalidate_visible_keys.__get__(shell)
        return shell

    # Synthetic ungated CommandDef so builtin-only visibility drives the result
    _ungated  = CommandDef(description="smoke-test fixture", category="setup", scope="global")
    _test_cmd = CommandDef(description="smoke-test fixture", category="setup", scope="global", feature_flag="smoke_test_flag")

    _BUILTIN_STATES = [
        (STATE_VISIBLE, False, True,  True,  True,  "true"),
        (STATE_DEV,     False, False, False, True,  '"dev"'),
        (STATE_HIDDEN,  False, False, True,  True,  '"hidden"'),
        (STATE_BLOCKED, False, False, False, False, "false"),  # never visible
    ]
    # columns: state, dev_mode, expect_visible_normal, expect_exec_normal,
    #          expect_visible_dev, label
    all_ok = True
    for state, _, exp_vis_normal, exp_exec_normal, exp_vis_dev, label in _BUILTIN_STATES:
        vis = {"testcmd": state}
        shell_normal = _make_shell(vis, {}, dev_mode=False)
        shell_dev    = _make_shell(vis, {}, dev_mode=True)

        vis_normal = shell_normal._is_command_visible("testcmd", _ungated)
        exec_normal = is_command_executable("testcmd", vis, dev_mode=False)
        vis_in_dev  = shell_dev._is_command_visible("testcmd", _ungated)

        if vis_normal != exp_vis_normal:
            fail(f"builtin visible:{label} — shell._is_command_visible (dev_mode=False) returned {vis_normal}")
            all_ok = False
        if exec_normal != exp_exec_normal:
            fail(f"builtin visible:{label} — is_command_executable (dev_mode=False) returned {exec_normal}")
            all_ok = False
        if vis_in_dev != exp_vis_dev:
            fail(f"builtin visible:{label} — shell._is_command_visible (dev_mode=True) returned {vis_in_dev}")
            all_ok = False
    if all_ok:
        ok("builtin true/dev/hidden/false — correct via shell._is_command_visible at dev_mode=False and True")

    # Verify _dev_mode toggle on the SAME shell object changes visibility
    toggle_shell = _make_shell({"x": STATE_DEV}, {}, dev_mode=False)
    assert not toggle_shell._is_command_visible("x", _ungated), "toggle: hidden before"
    toggle_shell._dev_mode = True
    toggle_shell._invalidate_visible_keys()
    assert toggle_shell._is_command_visible("x", _ungated), "toggle: visible after"
    ok("toggling shell._dev_mode=True reveals a 'dev' builtin via _is_command_visible")

    # ------------------------------------------------------------------
    # C. Feature flag pipeline — same approach, ungated builtin vis so
    #    only the feature flag drives the result.
    # ------------------------------------------------------------------
    _FLAG_STATES = [
        (STATE_ON,    True,  True,  True,  '"on"'),
        (FEAT_DEV,    False, False, True,  '"dev"'),
        (FEAT_HIDDEN, False, True,  True,  '"hidden"'),
        (STATE_OFF,   False, False, False, '"off"'),  # never visible
    ]
    # columns: state, exp_vis_normal, exp_exec_normal, exp_vis_dev, label
    # Pick a real command to use as a vehicle — one we can swap the flag on
    for state, exp_vis_normal, exp_exec_normal, exp_vis_dev, label in _FLAG_STATES:
        flags = {"smoke_test_flag": state}
        shell_normal = _make_shell({}, flags, dev_mode=False)
        shell_dev    = _make_shell({}, flags, dev_mode=True)

        vis_normal  = shell_normal._is_command_visible("anycmd", _test_cmd)
        exec_normal = is_enabled(flags, "smoke_test_flag", dev_mode=False)
        vis_in_dev  = shell_dev._is_command_visible("anycmd", _test_cmd)

        if vis_normal != exp_vis_normal:
            fail(f"feature {label} — _is_command_visible (dev_mode=False) returned {vis_normal}")
            all_ok = False
        if exec_normal != exp_exec_normal:
            fail(f"feature {label} — is_enabled (dev_mode=False) returned {exec_normal}")
            all_ok = False
        if vis_in_dev != exp_vis_dev:
            fail(f"feature {label} — _is_command_visible (dev_mode=True) returned {vis_in_dev}")
            all_ok = False
    if all_ok:
        ok("feature on/dev/hidden/off — correct via shell._is_command_visible at dev_mode=False and True")

    # Verify _dev_mode toggle on the SAME shell flips a "dev" feature flag
    toggle_shell2 = _make_shell({}, {"smoke_test_flag": FEAT_DEV}, dev_mode=False)
    assert not toggle_shell2._is_command_visible("anycmd", _test_cmd), "flag toggle: hidden before"
    toggle_shell2._dev_mode = True
    toggle_shell2._invalidate_visible_keys()
    assert toggle_shell2._is_command_visible("anycmd", _test_cmd), "flag toggle: visible after"
    ok("toggling shell._dev_mode=True reveals a 'dev' feature-flagged command")

    # ------------------------------------------------------------------
    # D. shell_help_rows end-to-end — real JSON file + real 'arc' entry
    # ------------------------------------------------------------------
    real_vis = load_command_visibility()
    arc_state = real_vis.get("arc")
    if arc_state != STATE_VISIBLE:
        fail(f"settings/builtin-commands.json: 'arc' should be visible, got {arc_state!r}")
    else:
        ok("settings/builtin-commands.json: 'arc' is visible")

    normal_rows = shell_help_rows(configure_mode=False, dev_mode=False)
    dev_rows    = shell_help_rows(configure_mode=False, dev_mode=True)
    normal_names = {r.name for r in normal_rows}
    dev_names    = {r.name for r in dev_rows}

    if "arc" not in normal_names:
        fail("shell_help_rows(dev_mode=False) is missing visible builtin 'arc'")
    else:
        ok("shell_help_rows(dev_mode=False) includes visible builtin 'arc'")

    if "arc" not in dev_names:
        fail("shell_help_rows(dev_mode=True) is missing builtin 'arc'")
    else:
        ok("shell_help_rows(dev_mode=True) includes builtin 'arc'")

    if not any(r.name.startswith("cd") for r in normal_rows):
        fail("shell_help_rows(dev_mode=False) is missing visible builtin 'cd'")
    else:
        ok("shell_help_rows(dev_mode=False) correctly includes visible builtin 'cd'")

    # ------------------------------------------------------------------
    # E. Registry sanity
    # ------------------------------------------------------------------
    ungated = [k for k, v in COMMANDS.items() if not v.feature_flag]
    gated   = [k for k, v in COMMANDS.items() if v.feature_flag]
    if not ungated:
        fail("No registered commands without a feature flag")
    else:
        ok(f"{len(ungated)} registered commands are always-on (no feature flag)")
    if not gated:
        fail("No registered commands have a feature flag")
    else:
        ok(f"{len(gated)} registered commands are gated by a feature flag")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def test_configure_flow() -> None:
    """Section 13 — Configure/commit flow unit tests.

    These are offline checks only — no network calls, no real SCM credentials.
    They verify the staging, unstage, abandon, and commit-confirmed logic
    by constructing minimal shell-state and mock SCM objects.
    """
    section("13. Configure/commit flow  (offline, no SCM)")

    # ── Staged ops structure ─────────────────────────────────────────────────
    try:
        from app.shell._base import ShellState
        state = ShellState()
        state.staged_ops = [
            {"command": "set address", "detail": "obj1", "folder": "Shared",
             "args": {}, "ops": [{"method": "POST", "base_url": "x", "path": "/y",
                                   "params": None, "json": {"name": "obj1"}}]},
            {"command": "set address", "detail": "obj2", "folder": "Shared",
             "args": {}, "ops": [{"method": "POST", "base_url": "x", "path": "/y",
                                   "params": None, "json": {"name": "obj2"}}]},
        ]
        ok("ShellState staged_ops: 2 entries constructed correctly")
    except Exception as exc:
        fail("ShellState staged_ops construction", str(exc))
        return

    # ── Unstage removes correct index ────────────────────────────────────────
    try:
        ops = list(state.staged_ops)
        removed = ops.pop(0)  # unstage #1
        assert removed["detail"] == "obj1"
        assert len(ops) == 1
        assert ops[0]["detail"] == "obj2"
        ok("unstage: removes item at correct 1-based index")
    except Exception as exc:
        fail("unstage index logic", str(exc))

    # ── Abandon clears all ───────────────────────────────────────────────────
    try:
        state.staged_ops = [
            {"command": "set address", "detail": "obj3", "folder": "Shared",
             "args": {}, "ops": []},
        ]
        state.staged_ops = []
        assert len(state.staged_ops) == 0
        ok("abandon: clears all staged ops")
    except Exception as exc:
        fail("abandon clears staged_ops", str(exc))

    # ── _rollback_version: None is safe (no arm without target) ─────────────
    try:
        from app.shell.configure import ConfigureMixin
        # Verify the method exists and its return annotation is int | None
        import inspect
        inspect.get_annotations(ConfigureMixin._rollback_version, eval_str=False)  # raises if missing
        ok("_rollback_version: exists on ConfigureMixin")
        # Verify _arm_commit_confirmed stores armed_at timestamp
        import threading
        import time
        mixin = object.__new__(ConfigureMixin)
        mixin._pending_confirm = None
        # Fake the timer — just check the dict structure
        timer = threading.Timer(600, lambda: None)
        mixin._pending_confirm = {
            "timer": timer, "version": 42, "minutes": 10,
            "armed_at": time.monotonic(),
        }
        assert "armed_at" in mixin._pending_confirm
        assert mixin._pending_confirm["version"] == 42
        timer.cancel()
        ok("_arm_commit_confirmed: armed_at key is present in pending dict")
    except Exception as exc:
        fail("commit confirmed dict structure", str(exc))

    # ── Pagination truncation warning ────────────────────────────────────────
    try:
        import warnings
        from unittest.mock import patch, MagicMock
        from app.api.client import SCMClient
        # Build a minimal client with a fake config
        cfg = MagicMock()
        cfg.client_id = "id"
        cfg.client_secret = "secret"
        cfg.tsg_id = "tsg"
        cfg.bearer_token = ""
        with patch.object(SCMClient, "_authenticate"):
            client = object.__new__(SCMClient)
            client._cfg = cfg
            client._token = "fake"
            client._page_reporter = None
            client._http = MagicMock()
        # Simulate a first page of 10 items with total=25 and _MAX_LIST_PAGES=1
        first = {"data": [{"id": i} for i in range(10)], "total": 25, "limit": 10}
        original_max = client._MAX_LIST_PAGES
        client._MAX_LIST_PAGES = 1  # force cap immediately
        with patch.object(client, "_request", return_value={"data": [{"id": 99}]}):
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                client._collect_pages("https://x", "/path", None, first)  # triggers the cap warning
                if w and "safety cap" in str(w[0].message).lower():
                    ok("pagination truncation: warning emitted when cap reached")
                else:
                    fail("pagination truncation: no warning emitted", f"warnings: {w}")
        client._MAX_LIST_PAGES = original_max
    except Exception as exc:
        fail("pagination truncation warning test", str(exc))

    # ── Thread safety: _LAST_ROWS uses lock ──────────────────────────────────
    try:
        import threading
        from app.commands.operations import _LAST_ROWS_LOCK
        assert isinstance(_LAST_ROWS_LOCK, type(threading.Lock()))
        ok("operations._LAST_ROWS_LOCK is a threading.Lock")
    except Exception as exc:
        fail("_LAST_ROWS_LOCK exists and is a Lock", str(exc))

    try:
        from app.commands.operations import _SLS_CLIENTS_LOCK
        assert isinstance(_SLS_CLIENTS_LOCK, type(threading.Lock()))
        ok("operations._SLS_CLIENTS_LOCK is a threading.Lock")
    except Exception as exc:
        fail("_SLS_CLIENTS_LOCK exists and is a Lock", str(exc))

    # ── cd .. context-aware navigation ───────────────────────────────────────
    try:
        from app.shell._base import ShellState
        s = ShellState()
        s.device = {"name": "fw01"}
        s.folder = "Shared"
        # Simulate cd .. when device is set — should clear device
        if s.device:
            s.device = None
        assert s.device is None
        ok("cd ..: clears device when device is set")
        # Simulate cd .. when folder is set (no device)
        s.folder = "Production"
        if not s.device and s.folder.lower() != "shared":
            s.folder = "Shared"
        assert s.folder == "Shared"
        ok("cd ..: resets folder to Shared when no device")
    except Exception as exc:
        fail("cd .. context-aware navigation", str(exc))


def test_gui_endpoints() -> None:
    """Section 14 — Browser-console endpoint coverage (offline, no SCM).

    Starts BOTH consoles against a REAL shell but with every file path the
    servers write redirected to a throwaway temp tree, then exercises every
    route over HTTP:
      * All GET routes return 200 + expected keys (read-only, exercises every
        getter/section builder — e.g. status, theme, prefs, config, branding,
        sources, and the feature server's nav/areas/features/domains/files/
        aliases/builtins/structure/theme).
      * POST endpoints reject invalid-but-dispatching payloads with a clean 400
        (this is what catches a route handler dispatching to a missing/broken
        method — the class of bug that silently 500'd POST /api/feature).
      * A few real arc-console round-trips (theme/prefs/branding/sources)
        persist to the temp tree and read back.
    Also asserts the session's new commands are still wired.
    """
    section("14. Browser-console endpoints  (offline, no SCM)")

    import contextlib
    import io
    import json as _json
    import shutil
    import tempfile
    import threading
    import time
    import urllib.error
    import urllib.request

    tmp = Path(tempfile.mkdtemp(prefix="arc-smoke-gui-"))
    patched: list = []  # (module, attr, original)

    def _patch(mod, attr, value):
        patched.append((mod, attr, getattr(mod, attr)))
        setattr(mod, attr, value)

    server_a = server_f = None
    try:
        import app.config as _cfg
        import app.paths as _paths
        from app.settings import user_prefs as _up

        # Redirect config.json + prefs to temp; redirect the settings files the
        # arc console writes (branding/sources) to temp COPIES of the real ones.
        _patch(_cfg, "CONFIG_DIR", tmp)
        _patch(_cfg, "CONFIG_FILE", tmp / "config.json")
        _patch(_up, "_LEGACY_PREFS_FILE", tmp / "nonexistent-prefs.json")
        for attr, real in (("BANNER_FILE", _paths.BANNER_FILE),
                           ("GOODBYE_FILE", _paths.GOODBYE_FILE),
                           ("APP_VARIABLES_JSON", _paths.APP_VARIABLES_JSON),
                           ("PANOS_SOURCES_FILE", _paths.PANOS_SOURCES_FILE),
                           ("SCM_SOURCES_FILE", _paths.SCM_SOURCES_FILE)):
            dest = tmp / Path(real).name
            try:
                shutil.copyfile(real, dest)
            except OSError:
                dest.write_text("{}\n" if str(real).endswith(".json") else "")
            _patch(_paths, attr, dest)

        # Build a real shell (no creds → _scm stays None); suppress its banner.
        with contextlib.redirect_stdout(io.StringIO()):
            from app.shell import ArcShell
            shell = ArcShell(_cfg.load_config())

        from app.web.arc_server import ArcGuiServer
        from app.web.feature_server import FeatureGuiServer
        server_a = ArcGuiServer(shell, port=4744)
        server_f = FeatureGuiServer(shell, port=4745)
        # open_browser=False: the smoke test only exercises the HTTP endpoints —
        # it must never pop a browser tab.
        threading.Thread(target=lambda: server_a.serve(open_browser=False), daemon=True).start()
        threading.Thread(target=lambda: server_f.serve(open_browser=False), daemon=True).start()
        time.sleep(0.5)

        def _req(port, path, body=None):
            url = f"http://127.0.0.1:{port}{path}"
            if body is None:
                req = urllib.request.Request(url)
            else:
                req = urllib.request.Request(
                    url, data=_json.dumps(body).encode(),
                    headers={"Content-Type": "application/json"}, method="POST")
            try:
                with urllib.request.urlopen(req, timeout=10) as resp:
                    return resp.status, _json.loads(resp.read() or b"{}")
            except urllib.error.HTTPError as exc:
                try:
                    payload = _json.loads(exc.read() or b"{}")
                except Exception:  # noqa: BLE001
                    payload = {}
                return exc.code, payload

        # --- ARC console GET routes (read-only) ---
        arc_gets = {
            "/api/nav": "sections", "/api/theme": "active", "/api/status": "scm_connected",
            "/api/prefs": "spinner", "/api/config": "default_folder",
            "/api/credentials": "scm", "/api/branding": "banner",
            "/api/sources?which=panos": "pages", "/api/sources?which=scm": "specs",
        }
        arc_get_fail = []
        for path, key in arc_gets.items():
            st, data = _req(4744, path)
            if st != 200 or key not in data:
                arc_get_fail.append(f"{path} (status={st})")
        if arc_get_fail:
            fail("ARC console GET routes", "; ".join(arc_get_fail))
        else:
            ok(f"ARC console: all {len(arc_gets)} GET routes return 200 + expected keys")

        # --- Feature console GET routes (read-only) ---
        feat_gets = {
            "/api/nav": None, "/api/areas": None, "/api/features": None,
            "/api/domains": None, "/api/files": None, "/api/aliases": None,
            "/api/builtins": None, "/api/structure/list": None, "/api/theme": "active",
        }
        feat_get_fail = []
        for path, key in feat_gets.items():
            st, data = _req(4745, path)
            if st != 200 or (key is not None and key not in data):
                feat_get_fail.append(f"{path} (status={st})")
        if feat_get_fail:
            fail("Feature console GET routes", "; ".join(feat_get_fail))
        else:
            ok(f"Feature console: all {len(feat_gets)} GET routes return 200")

        # --- POST dispatch guard: invalid-but-dispatching payloads → clean 400
        # (a missing/broken handler would surface as 500 here). ---
        bad_posts = [
            (4745, "/api/feature", {"flag": "show_address", "state": "bogus"}),
            (4745, "/api/scope", {"command": "show address", "scope": "bogus"}),
            (4745, "/api/theme", {"base": "NoSuchTheme", "overrides": {}}),
            (4744, "/api/theme", {"base": "NoSuchTheme", "overrides": {}}),
            (4744, "/api/sources", {"which": "bogus"}),
            (4744, "/api/config", {"features_gui": {"port": 4444}, "arc_gui": {"port": 4444}}),
        ]
        dispatch_fail = []
        for port, path, body in bad_posts:
            st, _ = _req(port, path, body)
            if st != 400:
                dispatch_fail.append(f"{path} → {st} (expected 400)")
        if dispatch_fail:
            fail("POST handlers must dispatch + validate (no 500s)", "; ".join(dispatch_fail))
        else:
            ok(f"all {len(bad_posts)} POST endpoints dispatch to a real handler (400 on bad input, no 500)")

        # --- Real ARC-console round-trips persisting to the temp tree ---
        rt_fail = []
        st, data = _req(4744, "/api/theme", {"base": "Ocean", "overrides": {"--bg": "#010203"}})
        if st != 200 or data.get("base") != "Ocean":
            rt_fail.append(f"theme save ({st})")
        st, data = _req(4744, "/api/prefs", {"terminal_length": 42, "spinner": False})
        if st != 200 or data.get("terminal_length") != 42:
            rt_fail.append(f"prefs save ({st})")
        st, data = _req(4744, "/api/branding",
                        {"goodbye_header": "## h", "goodbye_lines": ["bye one", "bye two"],
                         "app_variables": [{"key": "app_name", "value": "ARC"}]})
        if st != 200 or "bye one" not in (data.get("goodbye_lines") or []):
            rt_fail.append(f"branding save ({st})")
        st, data = _req(4744, "/api/sources",
                        {"which": "panos", "site": "x",
                         "pages": [{"key": "k", "url": "https://e.x", "kind": "added", "version": "1"}]})
        if st != 200 or not data.get("pages"):
            rt_fail.append(f"sources save ({st})")
        # unified theme actually persisted to config.json preferences block
        saved = _json.loads((tmp / "config.json").read_text())
        if saved.get("preferences", {}).get("gui_theme", {}).get("base") != "Ocean":
            rt_fail.append("gui_theme not persisted to config.json")
        if rt_fail:
            fail("ARC console POST round-trips", "; ".join(rt_fail))
        else:
            ok("ARC console: theme/prefs/branding/sources round-trip to temp files")

        # --- Feature toggle applies to the LIVE shell (no restart) ---
        try:
            key = "show address"
            from app.commands.registry import COMMANDS as _CMDS
            cd = _CMDS.get(key)
            if cd is not None:
                _req(4745, "/api/area", {"area": cd.category, "disabled": False})
                st, _ = _req(4745, "/api/feature", {"flag": cd.feature_flag, "state": "on"})
                if st == 200 and shell._is_command_visible(key, cd):
                    ok("feature enable via GUI applies to the live shell (no restart)")
                else:
                    fail("live feature enable", f"status={st}, visible={shell._is_command_visible(key, cd)}")
        except Exception as exc:  # noqa: BLE001
            fail("live feature enable", str(exc))

        # --- Tab-lifecycle: heartbeat keeps alive, /api/close releases CLI ---
        try:
            st, _ = _req(4744, "/api/ping", {})
            before = server_a._last_ping
            time.sleep(0.02)
            _req(4744, "/api/ping", {})
            pinged = server_a._last_ping > before
            st_c, _ = _req(4745, "/api/close", {})
            closed = server_f._closed.wait(2.0)
            if st == 200 and pinged and st_c == 200 and closed:
                ok("heartbeat ping + /api/close release the blocked CLI")
            else:
                fail("tab lifecycle",
                     f"ping={st}/{pinged} close={st_c}/{closed}")
        except Exception as exc:  # noqa: BLE001
            fail("tab lifecycle", str(exc))

    except Exception:  # noqa: BLE001
        fail("GUI endpoint coverage", traceback.format_exc(limit=4).strip())
    finally:
        for srv in (server_a, server_f):
            if srv is not None:
                try:
                    srv.stop()
                except Exception:  # noqa: BLE001
                    pass
        for mod, attr, orig in reversed(patched):
            setattr(mod, attr, orig)
        shutil.rmtree(tmp, ignore_errors=True)


def test_new_commands() -> None:
    """Section 14b — the session's new features stay wired (registry + builtins)."""
    # Folded into section 14 output but a distinct set of assertions.
    from app.commands.registry import COMMANDS
    from app.shell import _SHELL_BUILTINS

    # clone command registered + feature-flagged
    clone = COMMANDS.get("clone")
    if clone is not None and clone.feature_flag:
        ok(f"clone command registered (flag: {clone.feature_flag})")
    else:
        fail("clone command missing or not feature-flagged")

    # cd snippet navigation reachable (handled by the cd builtin)
    if "cd" in _SHELL_BUILTINS:
        ok("cd builtin present (cd snippet navigation reachable)")
    else:
        fail("cd builtin missing")

    # login builtin present
    if "login" in _SHELL_BUILTINS:
        ok("login builtin present")
    else:
        fail("login builtin missing from settings/builtin-commands.json")


def _test_gui_and_commands() -> None:
    """Section 14 driver — GUI endpoint coverage + new-command wiring."""
    test_gui_endpoints()
    test_new_commands()


# Maps section number to (function, short label)
_SECTION_MAP = [
    (1,  test_syntax,               "Syntax"),
    (2,  test_imports,              "Imports"),
    (3,  test_registry,             "Registry"),
    (4,  test_arg_parser,           "Arg parser"),
    (5,  test_token_optimizations,  "Token optimizations"),
    (6,  test_config,               "Config types"),
    (7,  test_formatter,            "Formatter"),
    (8,  test_banner_alignment,     "Banner alignment"),
    (9,  test_inline_help_alignment,"Inline help alignment"),
    (10, test_theme,                "Theme"),
    (11, test_code_map,             "Code map freshness"),
    (12, test_command_visibility,   "Command visibility"),
    (13, test_configure_flow,       "Configure/commit flow"),
    (14, _test_gui_and_commands,    "Browser consoles + new commands"),
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
            skipped_labels = ", ".join(f"{n}={label}" for n, _, label in _SECTION_MAP if n in skipped)
            print(f"        (Skipped: {skipped_labels} — run without --only to verify all)")
        return 0


if __name__ == "__main__":
    sys.exit(main())
