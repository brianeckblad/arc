# ARC Developer Guide — Tokenmaxing + Keyword Dictionary

The single reference for developing ARC efficiently (humans and AI agents).
Goal: the **"string theory" model** — every request names the one small file/
string to touch, not the whole CLI, so context (and tokens) stay minimal.

- **`README.md`** — what ARC is and how to run it (user-facing).
- **`README.dev.md`** (this file) — how to develop ARC with minimum context.
- **`AGENTS.md`** — the full spec (architecture, security, SCM gateway map).
  Read it only when this file is not enough. Agents load it automatically.

---

## Fast Start for AI Agents

Read in order, stopping as soon as you have enough context:

1. **This file** — recipes, file ownership, keyword vocabulary
2. `docs/RENDER_CATALOG.md` — all available render= keys (saves reading formatter.py)
3. `docs/COMMAND_PATTERNS.md` — copy a minimal working example pattern
4. `docs/COMMANDDEF_REFERENCE.md` — CommandDef field table (saves reading base.py)
5. `dev/API_INDEX.md` — compact SCM endpoint table (all specs, ~300 lines)
6. `dev/CODE_MAP.md` — exact line range of every method in large files
7. The one small file named by the keyword/recipe below
8. `AGENTS.md` — only for full policy/security/architecture context

**Never read `app/shell.py` (or any 300+ line file) whole.** Look up the method
in `dev/CODE_MAP.md`, then `read_file(offset, limit)` for just that range.

---

## Token-Saver Trigger Words

Say a trigger word and the agent jumps straight to the right small "string"
without scanning the whole codebase. One word replaces a paragraph.

| Trigger word | Means | Agent action (no full-repo read) |
|---|---|---|
| `render` | available render types | Read `docs/RENDER_CATALOG.md` — all render= keys with examples (saves reading formatter.py) |
| `patterns` | command pattern examples | Read `docs/COMMAND_PATTERNS.md` — copy one of 5 minimal patterns (saves reading existing commands) |
| `commanddef` | CommandDef fields | Read `docs/COMMANDDEF_REFERENCE.md` — all fields in one table (saves reading base.py) |
| `map` | use the code map | Read `dev/CODE_MAP.md`, then read only the listed line range |
| `index` | use the API index | Read `dev/API_INDEX.md` for the endpoint, skip spec files |
| `string <file>` | work only in this small file | Edit only the named string file; don't open `shell.py` whole |
| `catalog` | builtin metadata | Open `app/shell_catalog.py` only |
| `flag <name>` | feature flag work | Open `app/features.py` + the one CommandDef |
| `scaffold <cmd> <module>` | generate boilerplate | Run `dev/scaffold.py`, then fill TODOs |
| `smoke <file>` | targeted validation | Run `python dev/smoke_test.py --file <file>` |
| `only <n>` | run smoke section n | Run `python dev/smoke_test.py --only <n>` |
| `endpoint <resource>` | API lookup | Find row in `dev/API_INDEX.md`, note methods + SSH column |
| `method <name>` | read one method | Look up name in `dev/CODE_MAP.md`, read just that range |
| `debug` | start the debug protocol | Use the debug template; read only files the error names |
| `ship <flag>` | enable a feature for all | Flip `app/features.py` default to `True`; run smoke |
| `docsupdate` | pull + self-heal docs | Run `dev/update_scm_docs.py`; read `docs/scm-api/CHANGES.md`; follow `dev/DOCS_AGENT.md` |
| `docs agent` | enter docs mode | Read `dev/DOCS_AGENT.md`; pull docs, report changes, update affected API calls only |

---

## Keyword Vocabulary — Intent → Recipe

Say these keywords when requesting a feature — agent maps directly to the
pattern without reading AGENTS.md.

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

## Request Templates

Copy one of these and replace the angle-bracket values.

```text
add scm command: show <resource>
module: <objects|security|network|setup|operations>
feature_flag: <flag_name>
endpoint keyword: <resource from dev/API_INDEX.md>
```

```text
add device command: show <live-state>
ssh: <PAN-OS command>
scope: device
feature_flag: <flag_name>
```

```text
debug:
file: <file or command you were working on>
error: <paste traceback/output>
context: <device set? folder? configure mode? profile? SCM connected?>
```

```text
docs agent:
goal: <pull latest | check changes | update code for renamed endpoints>
notes: <anything you already know changed on pan.dev>
```

---

## Keyword Dictionary — Task → Files → Validation

| Say this | Agent reads first | Usually edits | Validation |
|---|---|---|---|
| `add scm command` | `docs/COMMAND_PATTERNS.md` (pattern 1), `dev/API_INDEX.md` for resource | command module + `app/api/client.py` if method missing + docs page | `python dev/smoke_test.py --only 1,2,3` |
| `add feature-flagged command` | `app/features.py`, `docs/COMMAND_PATTERNS.md` | `app/features.py`, command module | `python dev/smoke_test.py --file app/features.py` then `--only 1,2,3` |
| `add device command` | `docs/COMMAND_PATTERNS.md` (pattern 4), `dev/API_INDEX.md` SSH column | `operations.py`, docs page | `python dev/smoke_test.py --only 1,2,3` |
| `add shell builtin` | `app/shell_catalog.py`, `dev/CODE_MAP.md` | `shell_catalog.py`, one `_cmd_*`, `_dispatch()` | `python dev/smoke_test.py --file app/shell_catalog.py` |
| `change help text` | `app/shell_catalog.py` for SHELL help, command module for registered commands | small catalog/module only | `python dev/smoke_test.py --only 8` |
| `change prompt/banner` | `dev/CODE_MAP.md` (`_print_banner`/`_prompt`), `app/banner.txt` | banner/theme files | `python dev/smoke_test.py --only 7,9` |
| `change renderer` | `docs/RENDER_CATALOG.md` (find matching render= key), then `app/utils/formatter.py` | formatter + `_render` dispatch | `python dev/smoke_test.py --file app/utils/formatter.py` |
| `debug API 4xx` | `app/api/client.py`, `dev/API_INDEX.md` | client method or handler params | targeted smoke + reproduce command |
| `debug tab completion` | `dev/CODE_MAP.md` (`ArcCompleter.get_completions`) | completer only | `python dev/smoke_test.py --file app/shell.py` |
| `debug feature hidden` | `app/features.py`, command `feature_flag=` | feature flag default/local config | `python dev/smoke_test.py --file app/features.py` |
| `update docs` / `docs agent` | `dev/DOCS_AGENT.md`, then `docs/scm-api/CHANGES.md` | `dev/scm_sources.json` (auto), `app/api/client.py` for removed endpoints | `python dev/update_scm_docs.py --self-test` |

---

## File Ownership — Read ONLY What You Need

| Task | Read | Edit |
|------|------|------|
| Add a registered command | `app/commands/<module>.py` (COMMANDS dict at bottom) | same + `docs/commands/<slug>.md` |
| Look up an API endpoint | **`dev/API_INDEX.md`** (all specs, one line each) | — |
| Find a method's line range | **`dev/CODE_MAP.md`** (method→lines for all large files) | — |
| Deep-dive one endpoint | `docs/scm-api/specs/<category>.md` | — |
| Add a shell builtin | `app/shell_catalog.py` first, then `dev/CODE_MAP.md` for `_dispatch` range | catalog + one `_cmd_*` + `_dispatch()` |
| Edit one shell method | `dev/CODE_MAP.md` → read only that line range | same |
| Change API endpoint | `app/api/client.py` | same |
| Change output rendering | `app/utils/formatter.py` + `app/shell.py _render()` | same |
| Config / auth changes | `app/config.py`, `app/cli.py` | same |
| Theme / UI | `app/theme.py`, `app/cli_theme.json`, `app/shell.py _styled()` | same |
| Feature flags | `app/features.py` + `config/features.json` | same |

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
4. If new `render=` key: add formatter call in `smoke_test.py` section 7 + case in `ArcShell._render()`
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
5. Add a tab-completion case in `ArcCompleter` if the command takes structured args

**Smoke after:** `python dev/smoke_test.py --file app/shell_catalog.py`

## Remove a Shell Builtin — Checklist

Run each grep, act on every hit, then smoke test once at the end.

```bash
# 1. Remove from catalog (builtin name + help row)
#    Edit app/shell_catalog.py — SHELL_BUILTINS tuple + SHELL_HELP_ROWS

# 2. Remove dispatch branch in shell.py
grep -n '"<name>"' app/shell.py        # find the elif in _dispatch()

# 3. Remove completer case in shell.py
grep -n "first == \"<name>\"" app/shell.py

# 4. Remove/update ALL hint strings that mention the command
grep -rn '\b<name>\b' app/shell.py docs/commands/

# 5. Remove the docs page (no auto-delete)
rm -f docs/commands/<name>.md

# 6. Update smoke test shorthand if the command affected ambiguity
grep -n "<name>" dev/smoke_test.py

# 7. Validate
python dev/smoke_test.py --file app/shell_catalog.py
```

---

## Scope Rules (Every CommandDef Must Declare This)

| `scope=` | Meaning | Examples |
|----------|---------|---------|
| `"folder"` | SCM config at folder/snippet level; handler passes `folder=ctx.folder` | all config/policy/network/objects |
| `"device"` | Requires `cd <device>` first; live operational state | system resources, logs, ping |
| `"global"` | TSG-wide, no folder/device filter | show devices, jobs, commit, snippets |

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

When a flag is OFF: command hidden from `?`, blocked at execution with an
actionable message. Empty `feature_flag=""` (default) = always enabled.

---

## Shell "String Theory" Map

`app/shell.py` is the shell spine; small strings are split out so you edit a
tiny file instead of the whole CLI:

| String file | Owns | Edit when |
|---|---|---|
| `app/shell_catalog.py` | builtin command names + SHELL `?` help rows | adding/renaming builtin metadata |
| `app/features.py` | feature flags + local/env override loader | gating unfinished commands |
| `app/commands/<module>.py` | registered command handlers + `CommandDef`s | adding SCM/device commands |
| `app/api/client.py` | SCM HTTP methods | endpoint path/query changes |
| `app/utils/formatter.py` | output renderers | display changes |
| `app/theme.py` + `app/cli_theme.json` | color roles | theme changes |

**Section jumps:** `app/shell.py` is large — never read it whole. `dev/CODE_MAP.md`
lists the exact, always-current line range of every method (smoke section 10
fails if it drifts):

```python
# 1. Read dev/CODE_MAP.md to find the range, e.g.:  ._cmd_folder_create()  1450-1570
# 2. Read ONLY that range:
read_file("app/shell.py", offset=1450, limit=121)
```

Regenerate after editing any 300+ line file: `python dev/gen_code_map.py`

Future extraction order if `shell.py` keeps growing (one string at a time,
validate with `python dev/smoke_test.py --file app/shell.py` after each):

1. `app/shell_help.py` — `_cmd_help*`, collapsed prefix/tier helpers
2. `app/shell_nav.py` — `cd`, `folder`, `ls`, `pwd`, cache refresh
3. `app/shell_sessions.py` — `connect`, `remote`, `tsg`, `account`
4. `app/shell_execution.py` — `_execute_api`, `_execute_remote`, `_render`
5. `app/shell_prompt.py` — banner, prompt, goodbye, lifecycle

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

## API Resource Lookup — One Line Per Endpoint

Read `dev/API_INDEX.md` instead of any spec file. It covers all SCM specs:
Methods key `L`=List `R`=Get `C`=Create `U`=Update `D`=Delete, plus the existing
ARC command and the PAN-OS SSH equivalent for `--remote`.

Quick spot-check — common unimplemented resources worth adding:

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

## Scaffold a New Command Fast

```bash
python dev/scaffold.py "show bgp routes" network
python dev/scaffold.py "show nat-rules" network --feature-flag nat_rules
python dev/scaffold.py "show decryption-rules" security --feature-flag decryption_policy --dry-run
```

Then fill in the handler body and run `python dev/smoke_test.py --only 1,2,3`.

---

## Smoke Test Section Map

```bash
python dev/smoke_test.py               # all sections (full suite)
python dev/smoke_test.py --only 1,2,3  # syntax + imports + registry only
python dev/smoke_test.py --only 3      # registry only (fastest after adding a command)
python dev/smoke_test.py --file app/commands/network.py   # auto-selects relevant sections
python dev/smoke_test.py --file app/shell.py              # auto-selects relevant sections
```

| Section | Name | Run after changing |
|---------|------|-------------------|
| 1 | syntax | any `.py` file |
| 2 | imports | any `.py` file |
| 3 | registry integrity | any `commands/*.py` — adding/changing a `CommandDef` |
| 4 | arg parser | `registry._parse_args()` |
| 5 | token optimizations | `app/commands/registry.py` — `KEYWORD_PARAMS` constant |
| 6 | config types | `app/config.py` / `app/features.py` |
| 7 | formatter | `app/utils/formatter.py` — new render function |
| 8 | banner alignment | `app/shell.py _print_banner()` |
| 9 | inline help / builtins | `app/shell_catalog.py` or `app/shell.py` help |
| 10 | theme | `app/theme.py`, `app/cli_theme.json` |
| 11 | code map freshness | any 300+ line file — fails if `dev/CODE_MAP.md` is stale |

---

## Minimal Validation Matrix

| Changed | Run |
|---|---|
| `app/commands/*.py` | `python dev/smoke_test.py --only 1,2,3` |
| `app/shell_catalog.py` | `python dev/smoke_test.py --file app/shell_catalog.py` |
| `app/shell.py` (or any 300+ line file) | `python dev/gen_code_map.py && python dev/smoke_test.py --file app/shell.py` |
| `app/features.py` | `python dev/smoke_test.py --file app/features.py` |
| `app/utils/formatter.py` | `python dev/smoke_test.py --file app/utils/formatter.py` |
| before commit | `python dev/smoke_test.py` (pre-commit auto-refreshes `dev/CODE_MAP.md`) |

---

## Debug Error Patterns

| Error text | Look in | Likely cause |
|------------|---------|-------------|
| `HTTPStatusError 4xx/5xx` | `app/api/client.py` → `docs/scm-api/specs/<cat>.md` | Wrong path, missing param, bad auth |
| `AttributeError: ctx.*` | `app/commands/base.py` — `ExecutionContext` fields | Field doesn't exist on context |
| `KeyError` in `_render()` | `app/shell.py _render()` | `render=` key in CommandDef not in dispatch |
| `require_scm` raises | `app/commands/base.py` + check `scope=` | Command needs SCM but it's not configured |
| `require_device` raises | same + `ShellState.device` | `scope="device"` but no `cd <device>` |
| Builtin not dispatched | `app/shell.py _dispatch()` elif chain | Name not in `SHELL_BUILTINS` or missing elif |
| Tab completion wrong | `app/shell.py ArcCompleter.get_completions()` | Case in completer missing |
| Import error on startup | `app/commands/registry.py` merge block | New module not added to registry imports |
| Profile / keychain error | `app/config.py _profile_key()` + `load_config()` | Profile name mismatch or missing keychain |

**ExecutionContext fields:** `.scm`, `.ssh`, `.device`, `.folder`, `.target`, `.device_host`, `.config`

Paste this block when reporting a bug — the agent reads only what it needs:

```text
debug:
file: <which file you were editing or which command you ran>
error: <paste traceback or error message>
context: <any relevant state — device set? configure mode? profile?>
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

