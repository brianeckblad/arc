# ARC — Agent Guide (the hub)

**ARC** is a PAN-OS-style interactive shell for Palo Alto firewalls managed by Strata Cloud Manager (SCM). Commands run through SCM REST APIs by default; live device state via SSH (`connect`, `--remote`). SCM is the only API integration.

**Read minimally.** Never read a 300+ line file whole — look up the method in `app/scripts/CODE_MAP.md` and read only that range. Follow the routing table to the one or two files a task needs.

---

## Task Routing

| Keyword / task | Read | Edit | Validate |
|---|---|---|---|
| `network` / `security` / `objects` / `identity` / `setup` / `operations` | `docs/COMMAND_PATTERNS.md`, `app/scripts/API_INDEX.md` | `app/commands/<domain>.py` | `--only 1,2,3` |
| `packet-tracer` | `app/commands/packet_tracer.py` | same | `--only 1,2,3` |
| `render` (output/table) | `docs/RENDER_CATALOG.md` | `app/utils/formatter.py`, `_render()` in `app/shell/execution.py` | `--file app/utils/formatter.py` |
| `commanddef` | `docs/COMMANDDEF_REFERENCE.md` | — | — |
| `shell` (REPL, dispatch, help UX) | `app/scripts/CODE_MAP.md` → range in `app/shell/<file>.py` | that one mixin file | `--file app/shell/<file>.py` |
| `builtin` (SHELL help rows, visibility) | `settings/builtin-commands.json`, `app/settings/commands.py` | `settings/builtin-commands.json` | `--only 8,9,12` |
| `builtin editor` (visibility/display/help via GUI) | `set_builtin_field` in `app/settings/commands.py`, `app/web/feature_server.py` | same | `--only 1,2,12` |
| `feature` / `flag <name>` | `settings/features/` (`local.json` = user overrides, never regenerated) | owning file + `CommandDef.feature_flag` | `--only 1,2,3` |
| `feature editor` / `feature gui` (browser) | `app/web/feature_server.py`, `app/web/feature_gui.html` | same | `--only 1,2,3` |
| `feature names` / human labels (GUI **and** CLI) | `app/settings/feature_labels.py`, `settings/feature-labels.json` | same (labels file is user-editable + auto-augmented) | `--only 1,2,3` |
| `feature scope` / `hidden` / `area` (CLI subcommands) | `_cmd_feature*` in `app/shell/configure.py`, helpers in `app/settings/features.py` | same | `--only 1,2,3,12` |
| `verb visibility` (bare `?` COMMANDS section) | `settings/cli-structure.yaml` (`visible:` field), `app/settings/cli_structure.py` | `settings/cli-structure.yaml` | `--only 9,12` |
| `theme` | `settings/theme.json`, `app/settings/theme.py` | same | `--only 10` |
| `terminal` / prefs | `app/settings/user_prefs.py`, `_cmd_terminal` in `app/shell/configure.py` | same | `--only 4` |
| `argspec` (greedy `set` parsing, slot completion) | `settings/command-structure.json` (hand-curated), `app/settings/field_catalog.py` (AUTO-GENERATED), `app/settings/command_structure.py` | hand file or `python app/scripts/generate_field_library.py` | `--only 4` |
| `auth` | `app/config.py`, `app/cli.py` (auth group) | same | `--file app/config.py` |
| `scm-api` / `endpoint` | `app/scripts/API_INDEX.md`; `docs/scm-api/specs/<cat>.md` | `app/api/client.py` | full suite |
| `docsupdate` | `app/scripts/DOCS_AGENT.md` | `python app/scripts/docsupdate.py` | `--self-test` |
| `commandupdate` | — | `python app/scripts/commandupdate.py` | `--only 1,2,4` |
| `panos` (PAN-OS CLI) | `settings/panos-sources.json`, `app/scripts/panos-curation.json` | curation file, or `python app/scripts/panosupdate.py && python app/scripts/generate_panos_catalog.py` | full suite |
| `logs` (SLS fleet queries) | `app/api/sls.py`, log handlers in `app/commands/operations.py` | same | `python app/scripts/test_sls.py` + `--only 1,2,3` |
| `config-view` | `app/commands/config_view.py` (`_FORMAT_SET_SPECS` table) | same | `--only 1,2,3` |
| `pipes` (match/except/count/json/save) | `parse_output_filters` + `_dispatch_piped` in `app/shell/dispatch.py` | same | `--only 4` |
| `alias` / `history` | `_cmd_alias`/`_cmd_history` in `app/shell/dispatch.py` | same | `--only 4` |
| `find` (search commands) | `_cmd_find` in `app/shell/help.py`, `_complete_find` in `app/shell/completer.py` | same | `--only 1,2` |
| `watch` | `_cmd_watch` in `app/shell/dispatch.py` | same | `--only 1,2` |
| `scaffold` | — | `python app/scripts/scaffold.py "<cmd>" <module>` | `--only 1,2,3` |
| `map` / `method <name>` | `app/scripts/CODE_MAP.md` | — | — |
| `debug` | error table below | files named there | targeted smoke |

**Spoke files:** `docs/COMMAND_PATTERNS.md` · `docs/RENDER_CATALOG.md` · `docs/COMMANDDEF_REFERENCE.md` · `app/scripts/API_INDEX.md` · `app/scripts/CODE_MAP.md` · `app/scripts/DOCS_AGENT.md`

---

## Project Structure

```
arc/
├── run.py / pyproject.toml        ← dev entry (python run.py); uv-managed
├── AGENTS.md                      ← this hub
├── settings/                      ← USER-EDITABLE, no code:
│   ├── features/                  ← per-domain flag glossary (scm-*.json,
│   │                                panos-ops.json, panos-config.json;
│   │                                local.json = user overrides, never regenerated)
│   ├── builtin-commands.json      ← all 7 fields per builtin (visible/display/
│   │                                help/configure_only/hide_in_configure/
│   │                                onlogin/startup_hint)
│   ├── cli-structure.yaml         ← verb group descriptions + visible: field
│   ├── command-structure.json     ← hand-curated set/update/delete arg specs
│   ├── theme.json, banner.txt, goodbye.txt, panos-sources.json
├── config/<os_username>/          ← gitignored: config.json + preferences.json
├── docs/                          ← user-facing Markdown (help <topic>)
│   ├── commands/                  ← hand-written pages only (no generated stubs)
│   └── scm-api/                   ← pulled pan.dev specs (docsupdate)
└── app/                           ← CODE ONLY
    ├── cli.py                     ← typer entry
    ├── paths.py                   ← single source for asset paths
    ├── config.py                  ← ArcConfig + profiles + keychain
    ├── docs.py                    ← help renderer + synthesize_command_help
    ├── api/client.py              ← SCMClient: _request() + per-domain wrappers
    ├── ssh/manager.py             ← paramiko pool
    ├── shell/                     ← REPL mixins (one concern per file):
    │   ├── _base.py               ← spine: imports/constants/ShellState
    │   ├── dispatch.py            ← route every input line
    │   ├── help.py                ← ? help + _is_command_visible()
    │   ├── completer.py           ← tab completion
    │   ├── configure.py           ← configure mode + dev shell
    │   ├── execution.py / navigation.py / write_cmd.py / sessions.py / prompt.py
    │   └── __init__.py            ← ArcShell composition + run loop
    ├── settings/                  ← loaders for settings/ files
    │   ├── commands.py            ← builtin-commands.json loader; visibility states
    │   ├── features.py            ← feature flag loader; visibility states
    │   └── cli_structure.py       ← cli-structure.yaml loader; verb_visible()
    ├── commands/
    │   ├── base.py                ← CommandDef, ExecutionContext, factories
    │   ├── registry.py            ← merger; match_command()
    │   ├── <domain>.py            ← setup/objects/security/network/identity/operations
    │   ├── resource_catalog.py    ← AUTO-GENERATED (do not edit)
    │   └── generated.py           ← catalog entry → feature-gated command
    ├── scripts/                   ← generators + smoke suite
    │   ├── smoke_test.py          ← 12-section test suite
    │   ├── CODE_MAP.md            ← method → line ranges (auto-regenerated)
    │   └── generate_*.py / docsupdate.py / panosupdate.py / commandupdate.py
    └── utils/formatter.py         ← Rich renderers
```

**Three-folder rule:** `app/` = code, `settings/` = user-editable config, `config/<user>/` = secrets. Never hard-code an asset path — import from `app/paths.py`.

---

## Command Metadata — Source-of-Truth Hierarchy

| Layer | Owns | When |
|---|---|---|
| 1. `CommandDef` in `app/commands/*.py` | handler, description, usage, scope, render, feature_flag | always |
| 2. `docs/commands/<slug>.md` front-matter | description + usage overrides | only when file exists |
| 3. `settings/features/` | `on` / `"dev"` / `"hidden"` / `off` per feature flag | gates visibility + execution |
| 4. `settings/builtin-commands.json` | visibility/display/help/configure_only etc. for shell builtins | builtins only |
| 5. `settings/command-structure.json` + `app/settings/command_structure.py` | field order + greedy parsing | curated write commands only |

**Canonical visibility check:** `_is_command_visible()` in `app/shell/help.py` — checks both `builtin-commands.json` state and feature flag, honouring `_dev_mode`. Dispatch, completion, and help ALL call this; never inline `is_enabled()` for visibility. `_is_command_available()` adds context gates on top.

---

## Visibility States

Two parallel systems, same four states:

**Feature flags** (`settings/features/*.json`):

| State | Normal `?` | Dev mode `?` | Executable |
|---|---|---|---|
| `"on"` | ✓ | ✓ | ✓ |
| `"dev"` | ✗ | ✓ | dev mode only |
| `"hidden"` | ✗ | ✓ | ✓ always |
| `"off"` | ✗ | ✗ | ✗ |

**Builtin commands** (`settings/builtin-commands.json` `visible:` field) — same table with `true`/`"dev"`/`"hidden"`/`false` as state names. Dev mode shows all non-`false` commands and bypasses `configure_only` filtering so all builtins appear in `?`.

**Verb groups** (`settings/cli-structure.yaml` `visible:` field) — controls whether a verb (show/test/…) appears in the COMMANDS section of bare `?`. Same states. Dev mode shows all non-`false` verbs.

`settings/builtin-commands.json` fields (all 7 required on every entry):
`visible` · `display` · `help` · `configure_only` · `hide_in_configure` · `onlogin` · `startup_hint`

---

## Generated Commands (~1,050)

Every OpenAPI operation → feature-gated command via `resource_catalog.py` + `generated.py`. All default **off** (`settings/features/`). Explicit commands shadow generated ones. No doc files — help is synthesized. PAN-OS op commands: `panos_<family>` flags, all off. Op commands with `scm_map` in `app/scripts/panos-curation.json` run via SCM async ops-jobs API; unmapped ops print `--remote` guidance.

### Feature-editor sync guarantee (keep this true)

The feature editor (browser `feature gui`) and the `feature`/`alias` CLI are **sync-by-construction** — new features flow into both with no editor changes:
- **Flags/commands:** `app/web/feature_server.py` and the CLI both read the live registry (`COMMANDS`) + `settings/features/*.json` at request time. Anything `docsupdate`/`commandupdate` adds appears in both surfaces automatically.
- **Human labels:** `generate_feature_flags.py` (in the `catalog rebuild` chain that `docsupdate` auto-runs) calls `augment_feature_labels()` to add any newly-discovered area to `settings/feature-labels.json` with a best-guess name, **preserving existing human edits** (edit-safe, like `_carry`). The shared `app/settings/feature_labels.py` renders those names in **both** the CLI (`feature show`/`info`/`area`) and the GUI.
- **Command structure:** `commandupdate`/`command-structure update` regenerate non-override entries; GUI/CLI read them live. User `override:true` entries (from the GUI editor) are preserved.
- **Storage:** everything the editor writes lives in `settings/` — `feature-labels.json`, `features/*.json`, `features/local.json` (`_scope_overrides`, `_disabled_areas`), `command-aliases.json`, `command-structure.json`, `builtin-commands.json` (personal aliases stay in per-user `preferences.json`). Every capability has a shared helper used by GUI **and** CLI **and** manual edits — never add a capability to only one surface.
- **Area disable is a real gate:** `_disabled_areas` (local.json) turns a whole category OFF — `_is_command_visible` (help.py) and the dispatch executability gate both check `cmd_def.category in shell._disabled_areas`, so disabled-area commands vanish from `?`/completion/help AND are unrunnable, and every editor section (Features, Command Structure, Advanced) excludes them. It is a master gate above per-feature flags (values preserved). Managed by `feature area <name> enable|disable`, the GUI Areas tab, or hand-editing — all via `load_disabled_areas`/`set_area_disabled`.
- **Unified GUI:** `feature gui` is one consistent SPA — top tabs (Features · Command Structure · Aliases · Built-ins · Advanced), a left sidebar of groups per section, a main pane of items, `#section/group` hash routing. Built-in visibility is edited through the same `load_command_visibility` the shell's `?`/dispatch use; file/area names come from the shared `feature_labels` layer (human-readable in GUI and CLI).

---

## Add a Command

```python
# app/commands/<domain>.py
'show bgp-peers': CommandDef(
    description='Show BGP peer summary',
    category='network',
    scope='folder',               # REQUIRED: 'folder' | 'device' | 'global'
    api_handler=show_handler('get_bgp_peers'),
    ssh_command='show routing protocol bgp peer',
    render='list',                # see docs/RENDER_CATALOG.md
    feature_flag='bgp_peers',     # add "bgp_peers": "dev" to settings/features/
),
```

1. Domain module mirrors SCM URI (setup/objects/security/network/identity/operations). New SCM method → one-line getter in `app/api/client.py`.
2. Explicit `scope=`. Registry, completion, help pick it up — no dispatcher changes.
3. Flag: `"your_flag": "dev"` while building, flip to `"on"` to ship.
4. Doc file only if you have prose beyond description/usage — otherwise help is synthesized.
5. New `render=` key → add formatter + `_render()` case + smoke section-7 call.
6. Run `python app/scripts/smoke_test.py --only 1,2,3` before commit.

**Scope rules:** SCM config → `"folder"`; TSG-wide → `"global"`; live device state → `"device"` (requires `cd <device>`). Never mark network *config* as `"device"`.

**Handler rules:** named module-level functions only (no lambdas); `require_scm(ctx)` / `require_device(ctx)` guards; `raise ValueError("Usage: …")` for bad args.

---

## Execution Model

| Mode | Trigger | Path |
|---|---|---|
| API | any command | `_dispatch` → `match_command` → `_execute_api` → handler → `_render` |
| SSH | `--remote`, `connect` | `_execute_remote` / interactive PTY |

- `SCMClient` raises on errors — never swallow into `[]`. 401 auto-reauthenticates once.
- **Writes are STAGED.** `set`/`delete`/`update` route through `_stage_write`; `commit` replays. `show config` lists the queue. `unstage <n>` removes one entry by index. `abandon` discards all. Never bypass staging.
- `commit confirmed [min]` — Junos-style auto-revert, cancelled by `commit confirm`. While the countdown runs, the prompt shows a `[CONFIRM: Xm Ys]` segment in red.

### Shell UX invariants (do not regress)

- `?` is Cisco-style progressive help: context-aware, three tiers GLOBAL / FOLDER / DEVICE + SHELL. In dev mode `?` shows the full command tree (all non-`false` commands + builtins) then appends the DEV SHELL section.
- **`?` must preserve the input buffer** — uses `run_in_terminal` in `_make_key_bindings`. Never use `validate_and_handle` for `?`.
- Every builtin must handle `<builtin> ?` — dispatch calls the handler with `["?"]`. See `terminal`, `feature`, `find` cases in `app/shell/dispatch.py`.
- Prompt: `arc:global >` · `arc:Production >` · `arc:fw01:device >` · configure `#` · dev shell `:dev`. Never show `:Shared`. While `commit confirmed` countdown is active, prompt appends `[CONFIRM: Xm Ys]` in red.
- Unambiguous prefix shorthand (`sh sec pol` → `show security policy`); ambiguous never auto-expands.
- `cd` never opens SSH; `connect` does.
- `cd ..` is context-aware: clears device if one is set; resets folder to Shared if no device is set; no-op at global. `cd folder ..` always resets to Shared regardless.
- `find command <text>` — sub-command `command` tab-completes; search text is free-form.
- Tab completion surfaces dev-gated commands with a `[dev mode]` meta hint so operators can discover them without entering dev mode.

### Dev Shell (`dev` command)

Type `dev` to enter (modal, prompt `:dev`). `exit` to leave. `dev on`/`dev off` for CI. In dev shell `?` falls through to normal help (full command tree) then shows the DEV SHELL menu at bottom.

| Dev shell command | LLM trigger | Script |
|---|---|---|
| `docs update [--scm\|--panos]` | `docsupdate` | `python app/scripts/docsupdate.py` — **auto-chains `catalog rebuild`** on success |
| `command-structure update [<cmd>]` | `commandupdate` | `python app/scripts/commandupdate.py` |
| `catalog rebuild` | — | `app/scripts/generate_*.py` (6 scripts, includes CODE_MAP regeneration + silent `arc cliup`) |
| `status` | — | health dashboard |

---

## SCM REST API

**Never guess an endpoint** — look it up in `app/scripts/API_INDEX.md`. Source of truth: https://pan.dev/scm/api/ — mirrored by `python app/scripts/docsupdate.py` (`app/scripts/scm-sources.json`; writes `CHANGES.md` + `MANIFEST.md`).

Gateways: objects/security/setup/network/identity/device at `api.strata.paloaltonetworks.com/config/<domain>/v1`; IAM at `api.sase.paloaltonetworks.com`; token at `auth.apps.paloaltonetworks.com/auth/v1/oauth2/access_token`.

After `docsupdate`: `catalog rebuild` runs automatically on success — it regenerates CODE_MAP, resource catalog, feature flags, field library, command docs, and API index. Then check `docs/scm-api/CHANGES.md`; removed/renamed endpoints → fix `app/api/client.py` + commands. New endpoints auto-become gated commands + flags + docs.

---

## Config, Auth, Security

- Config: `config/<os_username>/config.json` (0600) — non-sensitive only. Secrets in OS keychain. `arc auth configure` (wizard), `arc auth test`, `arc config generate`.
- Profiles: `account <name>` switches in-shell.
- Env vars: `SCM_BEARER_TOKEN`, `SCM_CLIENT_ID`, `SCM_CLIENT_SECRET`, `SCM_TSG_ID`, `ARC_SSH_USER`, `ARC_SSH_KEY`, `ARC_SSH_PASS`, `ARC_DEBUG=1`, `ARC_DEV_MODE=1`, `ARC_FEATURE_<NAME>=on|dev|off`.
- Never write secrets to config.json; `getpass` for secret prompts; `_mask()` when printing; catch specific exceptions.

---

## Validation — app/scripts/smoke_test.py

```bash
python app/scripts/smoke_test.py                 # full suite (no network)
python app/scripts/smoke_test.py --only 1,2,3    # syntax + imports + registry
python app/scripts/smoke_test.py --file <path>   # auto-selects sections
```

| Section | Covers | Run after changing |
|---|---|---|
| 1 / 2 | syntax, imports | any .py |
| 3 | registry integrity + catalog drift | `commands/*.py` |
| 4 | arg parser / command-structure | `command-structure.json` |
| 5 | token optimizations | `registry.py` |
| 6 | config types | `app/config.py` |
| 7 | formatter calls | `app/utils/formatter.py` |
| 8 | banner alignment (startup hints) | `settings/builtin-commands.json`, `prompt.py` |
| 9 | inline help alignment, completion | `completer.py`, `command_structure.py` |
| 10 | theme + doc validity | `theme.json`, `docs/commands/` |
| 11 | CODE_MAP freshness | any 300+ line file |
| 12 | command visibility (builtin + feature states) | `settings/commands.py`, `settings/features.py`, `builtin-commands.json` |
| 13 | configure/commit flow (offline) | `app/shell/configure.py`, `app/commands/operations.py`, `app/shell/navigation.py` |

Pre-commit runs 1–3 + regenerates `CODE_MAP.md`. Version `0.1.<commit-count>` auto-bumped — never hand-edit.

---

## Naming Conventions

- **Python `.py`** → underscores (`command_structure.py`)
- **All other files** → hyphens (`command-structure.json`, `cli-structure.yaml`)
- Leading underscores (`_base.py`, `_auth.py`) are intentional Python private-module convention.
- Every operator-configurable value lives in `settings/`. If data is hardcoded in `app/`, move it.

---

## Git & Workflow

- Commit to current branch (usually `main`). Conventional-commit messages.
- Trigger words: `gitp` = stage all + commit + push · `docsupdate` = pull pan.dev docs · `commandupdate` = update contextual ? help specs · `ck`/`ctx`/`wipe` = write/summarize/clear `SESSION.md`.

### Settings file change policy

`settings/` is user-editable. Before committing any `settings/` change, confirm whether to include it or roll back (`git checkout HEAD -- settings/`). Pre-commit hook warns on `settings/` changes.

**Tracked settings files:** `builtin-commands.json` · `cli-structure.yaml` · `command-structure.json` · `theme.json` · `banner.txt` · `goodbye.txt` · `command-aliases.json` · `app-variables.json` · `features/*.json`

---

## Debug — error text → files

| Error | Look in | Likely cause |
|---|---|---|
| `Unknown command` | `app/commands/<module>.py` COMMANDS dict | not registered / feature flag off |
| `HTTPStatusError 4xx/5xx` | `app/api/client.py` + `app/scripts/API_INDEX.md` | wrong path/param; expired token (401) |
| `AttributeError: no attribute 'get_X'` | `app/api/client.py` | client method missing |
| `KeyError` in `_render()` | `app/shell/execution.py` dispatch table | render= key has no formatter case |
| `require_scm` / `require_device` raises | `app/commands/base.py` + `scope=` | missing SCM config / no `cd <device>` |
| builtin not dispatched | `settings/builtin-commands.json` + `app/shell/dispatch.py` | not in JSON or no elif branch |
| tab completion wrong/empty | `app/shell/completer.py` | missing case / empty cache |
| builtin hidden unexpectedly | `settings/builtin-commands.json` `visible:` field | wrong state or `configure_only` misset |
| feature hidden unexpectedly | `settings/features/` | absent = off; `"dev"` needs dev mode |
| verb missing from `?` | `settings/cli-structure.yaml` `visible:` | not `true` or no entry (defaults visible) |
| theme colour ignored | `settings/theme.json` + THEME_KEYS | key not in ArcTheme |
| profile/keychain error | `app/config.py` | profile name mismatch; keychain read failed |

```text
debug:
file: <file you edited or command you ran>
error: <traceback / output>
context: <device set? folder? configure mode? profile? SCM connected?>
```
