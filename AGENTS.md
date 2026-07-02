# ARC — Agent Guide (the hub)

**ARC (Assisted Remote Console)** is a PAN-OS-style interactive shell for Palo
Alto firewalls managed by Strata Cloud Manager (SCM). Commands execute through
SCM REST APIs by default; live device state goes over SSH (`--remote`,
`connect`, `remote <device>`). SCM is the only API integration.

This file is the **single hub** for anyone (human or agent) working on ARC.
Read it, then follow the routing tables below to the one or two spoke files a
task needs. There is no other instruction file — `.github/copilot-instructions.md`
and `README.dev.md` were retired into this hub.

**Read minimally.** Never read a 300+ line file whole: look up the method's
line range in `dev/CODE_MAP.md` and read only that range. The tables below name
the smallest file that owns each concern.

---

## Task Routing — say a keyword, touch small files

| Keyword / task | Read | Edit | Validate |
|---|---|---|---|
| `network` / `security` / `objects` / `identity` / `setup` / `operations` commands | `docs/COMMAND_PATTERNS.md`, `dev/API_INDEX.md` (endpoint row) | `app/commands/<domain>.py` | `python dev/smoke_test.py --only 1,2,3` |
| `packet-tracer` (policy simulation) | `app/commands/packet_tracer.py` | same | `--only 1,2,3` |
| `render` (output/table changes) | `docs/RENDER_CATALOG.md` | `app/utils/formatter.py`, `_render()` in `app/shell/execution.py` | `--file app/utils/formatter.py` |
| `commanddef` (field reference) | `docs/COMMANDDEF_REFERENCE.md` | — | — |
| `shell` (REPL, dispatch, help UX) | `dev/CODE_MAP.md` → one range in `app/shell/<file>.py` | that one mixin file | `--file app/shell/<file>.py` |
| `catalog` (builtin names, SHELL help rows) | `app/shell_catalog.py` | same | `--file app/shell_catalog.py` |
| `feature` / `flag <name>` (turn commands on/dev/off) | `settings/features.json` | same (+ one `CommandDef.feature_flag`) | `--only 1,2,3` |
| `theme` (colours) | `settings/theme.json`, `app/settings/theme.py` | same | `--only 10` |
| `settings` (banner, goodbye, labels — no code) | `settings/` | `settings/banner.txt` etc. | `--only 7,8,9,10` |
| `argspec` (greedy `set <object>` parsing, slot completion) | `settings/command-structure.json`, `app/settings/command_structure.py` | same | `--only 4` |
| `auth` (credentials, profiles) | `app/config.py`, `app/cli.py` (auth group) | same | `--file app/config.py` |
| `scm-api` / `endpoint <resource>` | `dev/API_INDEX.md`; deep dive: `docs/scm-api/specs/<cat>.md` | `app/api/client.py` | full suite |
| `docsupdate` / docs agent | `dev/DOCS_AGENT.md` | run `python dev/docsupdate.py` | `--self-test` |
| `scaffold <cmd> <module>` | — | run `python dev/scaffold.py "<cmd>" <module>` | `--only 1,2,3` |
| `map` / `method <name>` (find code) | `dev/CODE_MAP.md` | — | — |
| `debug` | error table at the bottom of this file | files the error names | targeted smoke |

**Spoke files** (each replaces reading a large module):
`docs/COMMAND_PATTERNS.md` (minimal working command patterns) ·
`docs/RENDER_CATALOG.md` (all render= keys) ·
`docs/COMMANDDEF_REFERENCE.md` (CommandDef fields) ·
`dev/API_INDEX.md` (one line per SCM endpoint) ·
`dev/CODE_MAP.md` (method → line ranges, auto-regenerated) ·
`dev/DOCS_AGENT.md` (pan.dev docs pull playbook).

---

## Project Structure

```
arc/
├── run.py / pyproject.toml        ← dev entry point (python run.py); uv-managed
├── AGENTS.md                      ← this hub
├── settings/                      ← USER-EDITABLE, no code: features.json (command
│                                    on/dev/off), banner.txt, goodbye.txt, theme.json,
│                                    cli-structure.yaml, command-structure.json,
│                                    commands.json (per-command visibility)
├── config/<os_username>/          ← per-user secrets file (gitignored; keychain-backed)
├── dev/                           ← generators + smoke suite (see Validation below)
├── docs/                          ← user-facing Markdown rendered by `help <topic>`
│   ├── commands/                  ← hand-written command pages ONLY (+ generated
│   │                                index.md, api-reference.md). Commands without a
│   │                                file get help synthesized from the registry.
│   └── scm-api/                   ← pulled pan.dev specs + guides (docsupdate)
└── app/                           ← CODE ONLY
    ├── cli.py                     ← typer entry: arc / arc auth / arc config / arc scm
    ├── paths.py                   ← single source of truth for asset paths
    ├── config.py                  ← ArcConfig + profiles + keychain secrets
    ├── docs.py                    ← help-topic renderer (+ synthesize_command_help)
    ├── api/client.py              ← SCMClient: _request() core + per-domain wrappers
    ├── ssh/manager.py             ← paramiko pool (agent → key → password → 2FA)
    ├── shell_catalog.py           ← builtin names + SHELL help rows (edit first)
    ├── shell/                     ← REPL as mixins, one concern per file:
    │   ├── _base.py               ← spine: shared imports/constants/helpers/ShellState
    │   ├── dispatch.py            ← _dispatch(): parse + route every input line
    │   ├── navigation.py          ← cd / folder / tsg / account / pwd + caches
    │   ├── execution.py           ← _execute_api/_execute_remote/_render + API errors
    │   ├── help.py                ← ? help (visibility checks live here)
    │   ├── completer.py           ← tab completion
    │   ├── configure.py / write_cmd.py / sessions.py / prompt.py
    │   └── __init__.py            ← ArcShell composition + run loop
    ├── settings/                  ← loaders for settings/ + docs front-matter
    ├── commands/
    │   ├── base.py                ← CommandDef, ExecutionContext, guards,
    │   │                            show_handler()/delete_handler() factories
    │   ├── registry.py            ← thin merger; match_command()
    │   ├── <domain>.py            ← setup/objects/security/network/identity/
    │   │                            operations/packet_tracer command modules
    │   ├── resource_catalog.py    ← AUTO-GENERATED endpoint catalog (do not edit)
    │   └── generated.py           ← factory: catalog entry → feature-gated command
    └── utils/formatter.py         ← Rich renderers (_simple_table + specials)
```

**Three-folder rule:** `app/` = code (developers/agents), `settings/` = user-editable
assets (anyone, no code), `config/<user>/` = secrets (via `arc auth configure`).
Never hard-code an asset path — import from `app/paths.py`.

---

## Command Metadata — Source-of-Truth Hierarchy

One command, five metadata layers. Higher layers override lower. Know which
layer owns what before editing anything:

| Layer | Owns | When it applies |
|---|---|---|
| 1. `CommandDef` in `app/commands/*.py` | everything: handler, description, usage, scope, render, feature_flag | always — the base truth |
| 2. `docs/commands/<slug>.md` front-matter | description + usage overrides | only when that file exists (hand-written pages) |
| 3. `settings/features.json` | on / `"dev"` / off per feature flag | gates visibility + execution |
| 4. `settings/commands.json` | per-command visibility bool | rarely used; hides individual commands |
| 5. `settings/command-structure.json` + `app/settings/command_structure.py` | field order + greedy parsing for curated `set <object>` | curated write commands only |

**The canonical visibility check** is `ArcShell._is_command_visible()`
(app/shell/help.py) — feature flag + commands.json. Dispatch, prefix expansion,
fuzzy suggestions, tab completion, and help ALL use it; never inline a bare
`is_enabled()` check for command visibility. `_is_command_available()` adds
context gates (device scope, configure mode) on top for `?` rendering.

**Generated commands** (~1,050): every pulled OpenAPI operation becomes a
feature-gated command via `resource_catalog.py` + `generated.py`
(GET→show, POST→set, PUT/PATCH→update, DELETE→delete). All default **off** in
`settings/features.json` — fail-closed until an operator enables them. Explicit
commands with the same key shadow generated ones (merged last in registry.py).
Generated commands have **no doc file** — `help <cmd>` synthesizes a page from
the CommandDef (`app/docs.py synthesize_command_help`). Never create doc stubs.

---

## Add a Command

```python
# app/commands/<domain>.py — trivial list/delete? use the factories:
'show bgp-peers': CommandDef(
    description='Show BGP peer summary',
    category='network',
    scope='folder',                          # REQUIRED — 'folder' | 'device' | 'global'
    api_handler=show_handler('get_bgp_peers'),
    ssh_command='show routing protocol bgp peer',   # str or named Callable(args)->str
    render='list',                           # key into _render(); see docs/RENDER_CATALOG.md
    feature_flag='bgp_peers',                # optional gate; add to settings/features.json
),
# anything with real logic (filtering, payloads, multiple calls) gets a named
# module-level handler: def _show_x(ctx: ExecutionContext, args: dict) -> Any
```

1. Pick the domain module (mirrors the SCM URI: setup, objects, security,
   network, identity, operations). New SCM method needed? Add a one-line
   getter to `SCMClient` using `self._request(...)` / `_get_<domain>(...)`.
2. Add the `CommandDef` with **explicit `scope=`**. Registry, tab completion,
   and help pick it up automatically — no dispatcher changes.
3. Feature-flag it: `"your_flag": "dev"` in `settings/features.json` while
   building; flip to `true` to ship. (`dev` command / `ARC_DEV_MODE=1` reveals
   dev-flagged commands; `feature enable|disable|dev <flag>` toggles one session.)
4. Doc file only if you have something to say beyond description/usage —
   otherwise help is synthesized. If you add `docs/commands/<slug>.md`, give it
   the front-matter block (`command`, `description`, `usage`, `category`, `scope`).
5. New `render=` key? Add the formatter (`_simple_table` fits most tables), a
   `_render()` dispatch case, and a smoke section-7 call.
6. `python dev/smoke_test.py --only 1,2,3` (full suite before commit).

Scope rules: SCM config (objects/policy/network) → `"folder"` (handler passes
`folder=ctx.folder`); TSG-wide inventory/jobs/commit → `"global"`; live device
state (logs, resources, ping) → `"device"` (requires `cd <device>`, runs via
SSH). Never mark network *config* as `"device"` — it's SCM data.

Handler rules: named module-level functions only (no lambdas — smoke enforces);
guards `require_scm(ctx)` / `require_device(ctx)` from base.py; raise
`ValueError("Usage: …")` for bad args — `_execute_api` renders it as a friendly
message. `ExecutionContext` fields: `.scm .ssh .config .device .folder .tsg_id`.

---

## Execution Model

| Mode | Trigger | Path |
|---|---|---|
| API (default) | any command | `_dispatch` → `match_command` → `_execute_api` → handler → `_render` |
| SSH | `--remote <device>`, `remote <device>`, `connect` | `_execute_remote` / interactive PTY |

- Errors: `SCMClient` raises (`httpx.HTTPStatusError` etc.) — never swallow into
  `[]`. `_execute_api` converts 401/403/404/network errors into actionable
  operator messages. Keep it that way.
- Live operational state is not in SCM: those commands print a clear
  "requires live device state — use `--remote`" message, never "translation pending".
- Configure mode (`configure`, prompt `#`) owns all writes: `set`/`delete`/
  `update`/`commit`/`folder create`/`cli` are blocked outside it.
- Context: `cd <device>` sets `ShellState.device`; `folder <name>` sets the
  `?folder=` param for all SCM calls; `tsg <id>` re-scopes auth and clears
  device/folder/caches (`_reset_tenant_context`).

### Shell UX invariants (do not regress)

- `?` is Cisco-style inline help: context-aware (only executable commands),
  progressive (next valid tokens only, not full command dumps), three tiers
  GLOBAL / FOLDER / DEVICE + SHELL. `<command> help` opens full docs;
  `help all` is the unfiltered dump.
- Prompt encodes context: `arc:global >` · `arc:Production >` ·
  `arc:fw01:device >` · `arc:fw01:Production >` · configure mode ends with `#`.
  Never show `:Shared` (it's the default state).
- Unambiguous token-prefix shorthand (`sh sec pol` → `show security policy`);
  ambiguous prefixes never auto-expand.
- Tab completion is context-aware (devices after `cd `/`remote `, folders after
  `folder `, TSGs after `tsg `, profiles after `account `, usage-driven argument
  slots). Structure-aware completion via `settings/command-structure.json`
  overrides usage-string walking for curated `set <object>` commands, with
  greedy no-quote parsing of free-text fields.
- `cd` never opens SSH; `connect`/`remote` do (true transparent PTY).
- Availability gates: device-scoped commands hidden without a device;
  `commit` only in configure mode; hard error for unknown device/folder when
  the cache is populated (graceful free-form fallback only when SCM is down).

---

## SCM REST API

**Never guess an endpoint.** Look it up in `dev/API_INDEX.md` (one line per
endpoint), or the mirrored spec `docs/scm-api/specs/<category>.md`. Source of
truth: https://pan.dev/scm/api/ — mirrored locally by `python dev/docsupdate.py`
(self-healing source registry `dev/scm_sources.json`; writes `CHANGES.md` +
`MANIFEST.md`). `MANIFEST.md` records each spec's base URL; `SCMClient` URL
constants must match it.

Gateways (one OAuth bearer token works on all): objects/security/setup/network/
identity/device at `api.strata.paloaltonetworks.com/config/<domain>/v1`;
IAM + tenancy at `api.sase.paloaltonetworks.com`; token endpoint
`auth.apps.paloaltonetworks.com/auth/v1/oauth2/access_token`
(client-credentials, `scope=tsg_id:<id>`; parent-TSG tokens can read children).

After `docsupdate`: read `docs/scm-api/CHANGES.md`; removed/renamed endpoints →
fix `app/api/client.py` + commands; it auto-reruns `generate_resource_catalog.py`,
`generate_feature_flags.py`, `generate_command_docs.py`, `generate_api_index.py`
so new endpoints become gated commands + flags + docs automatically.

---

## Config, Auth, Security

- Config file: `config/<os_username>/config.json` (0600) — **non-sensitive only**
  (client_id, tsg_id, SSH user/key path/port, profiles, active_profile).
  Secrets live in the OS keychain (profile-scoped keys `scm.<field>.<profile>`);
  env vars override everything. `arc auth configure` (wizard), `arc auth test`
  (5-step diagnostic), `arc config generate` (starter file).
- Named profiles: `account <name>` switches in-shell; `arc auth configure
  --profile <name>` creates.
- Env vars: `SCM_BEARER_TOKEN`, `SCM_CLIENT_ID`, `SCM_CLIENT_SECRET`,
  `SCM_TSG_ID`, `ARC_SSH_USER`, `ARC_SSH_KEY`, `ARC_SSH_PASS`, `ARC_DEBUG=1`
  (tracebacks), `ARC_DEV_MODE=1`, `ARC_FEATURE_<NAME>=on|dev|off`.
- Security invariants: never write secrets to config.json (fail closed if
  keychain unavailable); `getpass` for secret prompts; `_mask()` when printing
  credentials; SSH host keys are intentionally not verified (managed-device
  fleet — documented trade-off); catch specific exceptions, never bare
  `except Exception: return []` in the client.
- General Python/security standards: `docs/agent-patterns/python-standards.md`,
  `docs/agent-patterns/security-checklist.md`.

---

## Validation — dev/smoke_test.py

Run after every change to `app/`; full suite before commit (pre-commit hook runs
sections 1–3 and auto-regenerates `dev/CODE_MAP.md`; install once with
`bash dev/install_hooks.sh`).

```bash
python dev/smoke_test.py                    # full suite (~140 checks, no network)
python dev/smoke_test.py --only 1,2,3       # syntax + imports + registry
python dev/smoke_test.py --file <path>      # auto-selects relevant sections
```

| Section | Covers | Run after changing |
|---|---|---|
| 1 / 2 | syntax, imports | any .py |
| 3 | registry integrity + catalog drift | commands/*.py (drift fix: `python dev/generate_resource_catalog.py`) |
| 4 | arg parser / command-structure | registry parsing, command-structure.json |
| 5 | config types | app/config.py |
| 6 | formatter calls | new renderer → add a call here |
| 7 | banner alignment | prompt.py `_print_startup_help` (update `_BANNER_LINES`) |
| 8 | builtins ↔ catalog ↔ help sync | shell_catalog.py |
| 9 | structure completion + context help | completer / command_structure |
| 10 | theme + descriptions + doc validity | theme, docs/commands front-matter |
| 11 | CODE_MAP freshness | any 300+ line file (`python dev/generate_code_map.py`) |

Version is `0.1.<commit-count>` from `app/__init__.py` — never hand-edit
(optional bumper hook: `docs/dev-versioning.md`).

---

## Git & Workflow

- Commit directly to the current branch (usually `main`); create branches only
  when the user asks. Simple conventional-commit messages without nested quotes
  (multi-line via `git commit -F <file>`).
- User trigger words: `gitp` = stage all + commit + push · `docsupdate` = pull
  pan.dev docs + follow `dev/DOCS_AGENT.md` · `ck`/`ctx`/`wipe` = write /
  summarize / clear the `SESSION.md` scratch notes (gitignored session memory).
- Keep diffs small and focused; match existing naming and style; comments
  explain *why* (constraints, trade-offs), not *what*.
- Write for a junior engineer learning network operations: obvious control
  flow, domain names (`listing_status` not `data`), 1–3-sentence docstrings on
  non-trivial functions.

---

## Debug — error text → files

| Error | Look in | Likely cause |
|---|---|---|
| `Unknown command` | `app/commands/<module>.py` COMMANDS dict | not registered / feature flag off |
| `HTTPStatusError 4xx/5xx` | `app/api/client.py` + `dev/API_INDEX.md` | wrong path/param; expired token (401) |
| `AttributeError: no attribute 'get_X'` | `app/api/client.py` | client method missing |
| `KeyError` in `_render()` | `app/shell/execution.py` dispatch table | render= key has no formatter case |
| `require_scm` / `require_device` raises | `app/commands/base.py` + `scope=` | missing SCM config / no `cd <device>` |
| builtin not dispatched | `app/shell_catalog.py` + `app/shell/dispatch.py` | name not in catalog or no elif branch |
| tab completion wrong/empty | `app/shell/completer.py` | missing case / empty cache |
| feature hidden unexpectedly | `settings/features.json` | flag missing (absent = off) or `"dev"` outside dev mode |
| theme colour ignored | `settings/theme.json` + THEME_KEYS | key not in ArcTheme |
| profile/keychain error | `app/config.py` | profile name mismatch; keychain read failed |

Bug report template (lets an agent read only what it needs):

```text
debug:
file: <file you edited or command you ran>
error: <traceback / output>
context: <device set? folder? configure mode? profile? SCM connected?>
```
