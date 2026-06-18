# ARC Quick Reference — Minimum-Context Agent Map
<!--
  Read this INSTEAD of AGENTS.md for most tasks.
  AGENTS.md = full spec.  QUICK.md = minimum viable context.
  If something here is ambiguous, AGENTS.md is the source of truth.
-->

---

## File Ownership — Read ONLY What You Need

| Task | Read | Edit |
|------|------|------|
| Add a registered command | `app/commands/<module>.py` (COMMANDS dict at bottom) | same + `docs/commands/<slug>.md` |
| Look up an API endpoint | **`dev/API_INDEX.md`** (299 lines, all specs) | — |
| Find a method's line range | **`dev/CODE_MAP.md`** (method→lines for all large files) | — |
| Deep-dive one endpoint | `docs/scm-api/specs/<category>.md` | — |
| Add a shell builtin | `app/shell_catalog.py` first, then `dev/CODE_MAP.md` for `_dispatch` range | catalog + one `_cmd_*` + `_dispatch()` |
| Edit one shell method | `dev/CODE_MAP.md` → read only that line range | same |
| Change API endpoint | `app/api/client.py` | same |
| Change output rendering | `app/utils/formatter.py` + `app/shell.py _render()` | same |
| Config / auth changes | `app/config.py`, `app/cli.py` | same |
| Theme / UI | `app/theme.py`, `app/cli_theme.json`, `app/shell.py _styled()` | same |
| Feature flags | `app/features.py` + `config/features.json` | same |

**`dev/API_INDEX.md`** replaces reading individual spec files for endpoint lookups.
**`dev/CODE_MAP.md`** gives the exact line range of every method in large files — read it, then `read_file(offset, limit)` for just that method. Never read `app/shell.py` whole.
**`app/features.py`** — read this to understand what features are available and their default state.

---

## Add a Registered Command — 5 Steps

```python
# 1. Write handler in the right domain module
def _show_thing(ctx: ExecutionContext, args: dict) -> Any:
    scm = require_scm(ctx)
    return scm.get_things(folder=ctx.folder)

# 2. Add CommandDef to that module's COMMANDS dict
COMMANDS: dict[str, CommandDef] = {
    ...
    'show thing': CommandDef(
        description='Show things',
        category='objects',         # matches module domain
        scope='folder',             # 'folder' | 'device' | 'global'
        api_handler=_show_thing,
        ssh_command='show thing',   # str or named Callable(args)->str
        render='list',              # key into ArcShell._render()
    ),
}
```

3. `docs/commands/show-thing.md` — one paragraph + usage examples
4. If new `render=` key: add formatter call in `smoke_test.py` section 6 + case in `ArcShell._render()`
5. `python dev/smoke_test.py --only 1,2,3` — syntax + imports + registry

**Module → SCM path:**
| Module | SCM base URL suffix |
|--------|-------------------|
| `setup.py` | `/config/setup/v1` — devices, snippets, folders, jobs, commit |
| `objects.py` | `/config/objects/v1` — addresses, address-groups, services, tags, EDLs |
| `security.py` | `/config/security/v1` — security-rules, url-categories |
| `network.py` | `/config/network/v1` — interfaces, zones, routing, HA |
| `operations.py` | `/config/setup/v1` + live-device — jobs, system info, logs, ping |

---

## Add a Shell Builtin — 5 Steps

1. Add the accepted command token to `SHELL_BUILTINS` in `app/shell_catalog.py`
2. Add/update the help row in `SHELL_HELP_ROWS` in `app/shell_catalog.py`
3. Write `def _cmd_<name>(self, args: list[str]) -> None:` in `app/shell.py`
4. Add `elif tokens[0] == "name":` dispatch case in `_dispatch()`
5. Add tab completion case in `ArcCompleter` if the command takes structured args

**Smoke after:** `python dev/smoke_test.py --file app/shell_catalog.py`

---

## Feature Flags — Enable/Disable API Commands

Flags let you add a command to the registry but keep it hidden until tested.

```python
# 1. Add flag to app/features.py FeatureFlags (default=False)
nat_rules: bool = False

# 2. Set on CommandDef
'show nat-rules': CommandDef(..., feature_flag='nat_rules')

# 3. Enable locally — add to config/features.json (git-ignored)
{"nat_rules": true}

# 4. Or use env var for one session:
ARC_FEATURE_NAT_RULES=1 python run.py

# 5. When ready to ship: flip default to True in FeatureFlags
nat_rules: bool = True   # ships to everyone
```

When a flag is OFF: command hidden from `?`, blocked at execution with actionable message.  
When a flag is ON: works normally.  
Empty `feature_flag=""` (default) = always enabled, never gated.

**Scaffold with a flag:**
```bash
python dev/scaffold.py "show nat-rules" network --feature-flag nat_rules
```

---

## Shell.py Section Jumps (Tokenmax read strategy)

`app/shell.py` is large. **Never read it whole.** `dev/CODE_MAP.md` lists the
exact, always-current line range of every method (auto-generated; smoke section
10 fails if it drifts). Look up the method, then read only its range:

```python
# 1. Read dev/CODE_MAP.md (small) to find the line range, e.g.:
#      ._cmd_folder_create()   1450-1570
# 2. Read ONLY that range:
read_file("app/shell.py", offset=1450, limit=121)
```

Regenerate after editing any 300+ line file: `python dev/gen_code_map.py`

---

## Keyword Vocabulary — Intent → Recipe

Say these keywords when requesting a feature — agent maps directly to pattern without reading AGENTS.md.

| Keyword | Module | Scope | Guard | Notes |
|---------|--------|-------|-------|-------|
| `scm command` | any commands/ | `folder` | `require_scm(ctx)` | API GET/list, pass `folder=ctx.folder` |
| `global command` | setup.py / ops | `global` | `require_scm(ctx)` | TSG-wide, no folder filter |
| `device command` | operations.py | `device` | `require_device(ctx)` | needs `cd <device>` first |
| `config mode` | any | any | `_state.configure_mode` check | write ops blocked outside config |
| `ssh command` | operations.py | `device` | `require_device` | ssh_command= only; --remote flag |
| `show X` | network/objects/security/setup | `folder` | `require_scm` | GET list; render='list' |
| `show X <name>` | same | `folder` | `require_scm` | GET list + filter client-side |
| `create X` | same | `folder` | config mode + `require_scm` | POST endpoint; configure guard |
| `delete X` | same | `folder` | config mode + `require_scm` | DELETE endpoint; configure guard |
| `ping / traceroute` | operations.py | `device` | `require_device` | live device only; ssh_command= |
| `show log` | operations.py | `device` | `require_device` | live device only; ssh_command= |
| `commit` | operations.py | `global` | config mode | POST /config-versions/candidate:push |

---

## API Resource Lookup — One Line Per Endpoint

Read `dev/API_INDEX.md` (299 lines) instead of any spec file.
It covers all 12 SCM specs: Methods key `L`=List `R`=Get `C`=Create `U`=Update `D`=Delete

Quick spot-check — most common unimplemented resources worth adding:

| Resource | API module | Methods | SSH equivalent |
|----------|-----------|---------|---------------|
| `nat-rules` | network/v1 | LRCUD | `show running nat-policy` |
| `ipsec-tunnels` | network/v1 | LRCUD | `show vpn ipsec-sa` |
| `ike-gateways` | network/v1 | LRCUD | `show vpn ike-sa` |
| `pbf-rules` | network/v1 | LRCUD | `show pbf rule all` |
| `bgp-address-family-profiles` | network/v1 | LRCUD | `show routing protocol bgp summary` |
| `logical-routers` | network/v1 | LRCUD | `show routing summary` |
| `dhcp-interfaces` | network/v1 | LRCUD | `show dhcp server lease interface <name>` |
| `decryption-rules` | security/v1 | LRCUD | `show security decryption-policy` |
| `authentication-profiles` | identity/v1 | LRCUD | `show authentication` |
| `sdwan-rules` | network/v1 | LRCUD | `show sdwan traffic` |
| `application-groups` | objects/v1 | LRCUD | `show objects application-group` |

Refresh full index: `python dev/gen_api_index.py`

---

## Docs Agent Mode (pull pan.dev docs + update code)

Full playbook: `dev/DOCS_AGENT.md`. Common commands:

```bash
python dev/update_scm_docs.py            # pull all docs, self-heal moved paths, write CHANGES.md
python dev/update_scm_docs.py --check     # report drift/relocations, write nothing
python dev/update_scm_docs.py --list-remote   # live pan.dev spec paths
python dev/update_scm_docs.py --self-test     # offline tests (no network)
```

- Source paths live in `dev/scm_sources.json` (auto-updated when pan.dev renames files).
- After a pull, read `docs/scm-api/CHANGES.md` — **Removed** endpoints = ARC code to fix; **Added** = new features.
- "file not found" no longer happens: a 404 triggers tree discovery → registry self-heals.

---

## Scope Rules (Every CommandDef Must Declare This)

| `scope=` | Meaning | Examples |
|----------|---------|---------|
| `"folder"` | SCM config at folder/snippet level; handler passes `folder=ctx.folder` | all config/policy/network/objects |
| `"device"` | Requires `cd <device>` first; live operational state | system resources, logs, ping |
| `"global"` | TSG-wide, no folder/device filter | show devices, jobs, commit, snippets |

---

## Debug Error Patterns

| Error text | Look in | Likely cause |
|------------|---------|-------------|
| `HTTPStatusError 4xx/5xx` | `app/api/client.py` → `docs/scm-api/specs/<cat>.md` | Wrong path, missing param, bad auth |
| `AttributeError: ctx.*` | `app/commands/base.py` — `ExecutionContext` fields | Field doesn't exist on context |
| `KeyError` in `_render()` | `app/shell.py _render()` | `render=` key in CommandDef not in dispatch |
| `require_scm` raises | `app/commands/base.py` + check `scope=` | Command needs SCM but it's not configured |
| `require_device` raises | same + `ShellState.device` | `scope="device"` but no `cd <device>` |
| Builtin not dispatched | `app/shell.py _dispatch()` elif chain | Name not in `_SHELL_BUILTINS` or missing elif |
| Tab completion wrong | `app/shell.py ArcCompleter.get_completions()` | Case in completer missing |
| Import error on startup | `app/commands/registry.py` merge block | New module not added to registry imports |
| Profile / keychain error | `app/config.py _profile_key()` + `load_config()` | Profile name mismatch or missing keychain |

**ExecutionContext fields:** `.scm`, `.ssh`, `.device`, `.folder`, `.target`, `.device_host`, `.config`

---

## Smoke Test Section Map

```bash
python dev/smoke_test.py               # all 9 sections (~86 checks)
python dev/smoke_test.py --only 1,2,3  # syntax + imports + registry only
python dev/smoke_test.py --only 3      # registry only (fastest after adding a command)
python dev/smoke_test.py --file app/commands/network.py   # auto-selects 1,2,3
python dev/smoke_test.py --file app/shell.py              # auto-selects 1,2,7,8
```

| Section | Name | Run after changing |
|---------|------|-------------------|
| 1 | syntax | any `.py` file |
| 2 | imports | any `.py` file |
| 3 | registry integrity | any `commands/*.py` — adding/changing a `CommandDef` |
| 4 | arg parser | `registry._parse_args()` |
| 5 | config types | `app/config.py` — `ArcConfig` / `SCMConfig` fields |
| 6 | formatter | `app/utils/formatter.py` — new render function |
| 7 | banner alignment | `app/shell.py _print_banner()` |
| 8 | builtin alignment | `app/shell.py _print_shell_builtins()` or `_SHELL_BUILTINS` |
| 9 | theme | `app/theme.py`, `app/cli_theme.json` |
| 10 | code map freshness | any 300+ line file — fails if `dev/CODE_MAP.md` is stale |

---

## Key Constants & Entry Points

| Symbol | Location | Purpose |
|--------|----------|---------|
| `_SHELL_BUILTINS` | `app/shell.py` (imported from catalog) | Tuple driving dispatch + tab completion |
| `SHELL_BUILTINS` / `SHELL_HELP_ROWS` | `app/shell_catalog.py` | Source of truth for builtin names + SHELL help rows |
| `_HELP_CMD_WIDTH` | `app/shell.py` (see `dev/CODE_MAP.md`) | Column width for command names in `?` output |
| `COMMANDS` | each `commands/<module>.py` | Per-module command dict; `registry.py` merges all |
| `ArcShell._render()` | `app/shell.py` (see `dev/CODE_MAP.md`) | Dispatch on `render=` key from `CommandDef` |
| `ArcShell._dispatch()` | `app/shell.py` (see `dev/CODE_MAP.md`) | Shell input router — builtins then registry |
| `GOODBYE_FILE` | `app/shell.py` (see `dev/CODE_MAP.md`) | `app/goodbye.txt` — random exit messages |

---

## Scaffold a New Command Fast

```bash
# Generate handler stub + CommandDef + docs file in one shot:
python dev/scaffold.py "show bgp routes" network

# Then fill in the handler body and run:
python dev/smoke_test.py --only 1,2,3
```

---

## Model Routing Hints

| Task | Best fit | Why |
|------|----------|-----|
| Add one standard command | `claude-3-5-sonnet`, `gpt-4o` | Pattern is mechanical; fast+cheap |
| Debug API dispatch flow | `claude-3-7-sonnet`, `o3` | Needs multi-step reasoning through state |
| Read many files simultaneously | `gemini-2.0-flash`, `gemini-2.5-pro` | 1 M+ context window; fewer round-trips |
| Pure boilerplate generation | `gpt-4o-mini`, Copilot inline | Cheapest; pattern is fully specified here |
| Architecture / security review | `claude-opus-4`, `gemini-2.5-pro` | Depth over speed |
| Large refactor touching many files | `gemini-2.5-pro` | Load whole codebase at once |

---

## Start a Debug Session Efficiently

Paste this block when reporting a bug — the agent reads only what it needs:

```
debug:
file: <which file you were editing or which command you ran>
error: <paste traceback or error message>
context: <any relevant state — device set? configure mode? profile?>
```

The debug error table above maps error text to the 1–2 files that matter.
No full codebase re-read needed for most bugs.

