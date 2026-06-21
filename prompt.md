# AI Build Prompt — Recreate ARC (Assisted Remote Console)

> Give this file to a capable coding agent. It is a complete, self-contained
> specification to build **ARC** from an empty repository: an interactive,
> vendor-CLI-style shell for Palo Alto Networks **Strata Cloud Manager (SCM)**
> that pulls its entire command surface, help, and documentation **from the
> live API specs**, with SSH passthrough for managed devices.
>
> Build it in the phases below, in order. After each phase, run the smoke test
> and do not proceed until it passes. Prefer small, well-named, documented
> functions. Write code a junior network engineer can safely modify.

---

## 0. Mission and Philosophy

Build **ARC** — an "assisted remote console". It presents a Cisco/PAN-OS-style
interactive shell. Familiar firewall/network commands (`show address`,
`set address ...`, `commit`, `show interface`, `show jobs`) are translated to
**SCM REST API** calls by default; an explicit `--remote` / `connect` path runs
commands over **SSH** on a managed device for live operational state.

Guiding principles (these shape every decision):

1. **The API is the source of truth.** Never hard-code the list of resources,
   endpoints, or object fields. Pull the OpenAPI specs from the vendor, parse
   them, and *generate* the command surface, the per-field metadata, and the
   reference docs. Adding a new vendor endpoint should require **zero** hand code.
2. **Three-folder separation.**
   - `app/` — Python application code only.
   - `settings/` — user-editable assets (no code): banner, theme, feature flags,
     command-argument order. A non-programmer customizes ARC here.
   - `config/<os_username>/` — per-user secrets handle (non-secret values only;
     real secrets go to the OS keychain). Never committed.
3. **Everything is context-aware.** No command runs in the wrong scope. The
   prompt, tab completion, `?` help, and dispatch all respect the active
   folder / device / mode.
4. **Single source of truth for help.** Each command's description, usage, and
   full help page live in one Markdown file with YAML front-matter. The shell
   reads it; there is no second place to edit.
5. **Token-efficient, junior-readable code.** Small mixin files, generated
   line-maps, a fast structural smoke test, and clear domain names.

---

## 1. Tech Stack (pin these)

| Layer | Choice |
|---|---|
| Language | Python ≥ 3.11 |
| Packaging | `uv` + `hatchling`; `pyproject.toml`; entry point `arc = "app.cli:run"` |
| CLI framework | Typer |
| Interactive REPL | prompt-toolkit (≥3) |
| Output rendering | Rich |
| HTTP client | httpx (sync, always with timeouts) |
| SSH | paramiko (≥3.4) |
| Validation | pydantic (v2) |
| Secrets | keyring (OS keychain) |
| Spec parsing (dev) | PyYAML |
| Lint/format | ruff (line length 100, target py311) |
| Dev/test | pytest, respx/pytest-httpx |

Runtime deps: `cryptography, httpx, keyring, paramiko>=3.4, platformdirs,
prompt-toolkit>=3, pydantic>=2, rich>=13, typer>=0.12`.
Dev extras: `pytest, pytest-httpx, respx, ruff, pyyaml`.

---

## 2. Repository Layout (target)

```
arc/
├── README.md                  # user overview
├── README.dev.md              # developer guide + keyword dictionary (read first)
├── AGENTS.md / .github/copilot-instructions.md   # agent operating rules (synced)
├── SESSION.md                 # gitignored working memory for agents
├── pyproject.toml
├── run.py                     # dev entry: python run.py
├── settings/                  # USER-EDITABLE (committed; no code)
│   ├── README.md
│   ├── features.json          # on/dev/off switch per command (source of truth)
│   ├── banner.txt             # startup banner (Rich markup; ## = comment)
│   ├── goodbye.txt            # random exit lines
│   ├── theme.json             # CLI colour roles
│   ├── cli-structure.yaml     # verb descriptions, section labels, footer
│   └── command-structure.csv  # ORDER of fields per command (object,field,field,...)
├── config/
│   └── config.example.json    # template → config/<user>/config.json (gitignored)
├── dev/                        # generators + tests (not shipped to users)
│   ├── docsupdate.py     # pull+parse vendor specs (self-healing)
│   ├── scm_sources.json       # editable registry of spec/guide source paths
│   ├── generate_resource_catalog.py# specs → app/commands/resource_catalog.py
│   ├── generate_command_docs.py    # ensure front-matter + index + api-reference
│   ├── generate_api_index.py       # specs → dev/API_INDEX.md (compact endpoint table)
│   ├── generate_code_map.py        # large files → dev/CODE_MAP.md (method line ranges)
│   ├── scaffold.py            # scaffold a new command (handler+CommandDef+doc)
│   ├── smoke_test.py          # structural test suite (11 sections)
│   └── install_hooks.sh       # pre-commit hook installer
├── docs/                      # rendered by `help` inside ARC
│   ├── README.md usage.md architecture.md configuration.md
│   ├── commands/              # one <slug>.md per command (front-matter + body)
│   └── scm-api/               # mirror of vendor docs (pulled)
│       ├── specs/<category>.yaml + <category>.md
│       ├── guides/*.md
│       ├── index.md  MANIFEST.md  CHANGES.md
└── app/                       # CORE CODE
    ├── __init__.py            # __version__
    ├── paths.py               # ALL filesystem paths (single source of truth)
    ├── cli.py                 # Typer app: arc / arc auth / arc scm / arc docs
    ├── config.py              # ArcConfig/SCMConfig dataclasses, keychain, profiles
    ├── docs.py                # docs/ Markdown loader for help + browser opener
    ├── shell_catalog.py       # builtin command names + SHELL help rows
    ├── api/client.py          # SCMClient (REST only) — base URLs from specs
    ├── ssh/manager.py         # SSHManager (paramiko pool + interactive PTY)
    ├── utils/formatter.py     # Rich table/panel renderers (render= registry)
    ├── settings/              # loaders for settings/ files
    │   ├── theme.py command_help.py cli_structure.py features.py command_structure.py
    ├── commands/              # one module per SCM domain + shared base
    │   ├── base.py registry.py generated.py resource_catalog.py
    │   ├── setup.py objects.py security.py network.py identity.py
    │   ├── operations.py packet_tracer.py
    └── shell/                 # interactive REPL as a mixin package
        ├── __init__.py _base.py completer.py dispatch.py navigation.py
        ├── sessions.py execution.py help.py configure.py write_cmd.py prompt.py
```

---

## 3. The API-Driven Pipeline (the heart of ARC)

This is what makes ARC special. Implement it as four generators that run in
sequence (wire them all to a single `docsupdate` developer action).

### 3.1 Pull + parse specs — `dev/docsupdate.py`

- Source paths live in an **editable registry** `dev/scm_sources.json`, NOT
  hard-coded. It lists, per domain, the path to each OpenAPI spec and each
  conceptual guide doc in the vendor's public docs repo.
- Download raw specs/guides using **stdlib `urllib`** only, every call bounded by
  a timeout. (Markdown/diff generation may use PyYAML; if missing, still save raw
  specs and print the install hint.)
- **Self-healing discovery:** when a path 404s (vendors rename files often),
  search the live repo tree for the most likely replacement (by domain + filename
  similarity), update `scm_sources.json`, record the move under `relocations`,
  and retry. The tool must not fail with "file not found".
- Write under `docs/scm-api/`:
  - `specs/<category>.yaml` (raw) + `specs/<category>.md` (a terminal-friendly
    per-endpoint listing that records path, summary, container scope
    folder|snippet|device, the request body schema + required fields, and nested
    `oneOf/anyOf` variants — e.g. address `ip_netmask | ip_range | ip_wildcard | fqdn`).
  - `guides/*.md` (every conceptual doc; curated names stable, new ones slugged).
  - `index.md`, `MANIFEST.md` (each spec's `servers[0].url` base URL + pull date),
    and `CHANGES.md` (added/removed endpoints per domain since last pull).
- Flags: `--check` (report drift, write nothing), `--list-remote`, `--no-mirror`,
  `--self-test` (offline tests for discovery + diff).
- After a successful pull, automatically run `generate_resource_catalog.py`,
  `generate_feature_flags.py`, `generate_command_docs.py`, and
  `generate_api_index.py`.

### 3.2 Generated endpoint coverage — `dev/generate_resource_catalog.py` + `app/commands/generated.py`

**Policy: every pulled SCM OpenAPI operation becomes generated command metadata,
feature-gated by default.**

- `generate_resource_catalog.py` reads every pulled OpenAPI spec and writes
  `app/commands/resource_catalog.py` entries for `GET`, `POST`, `PUT`/`PATCH`,
  and `DELETE` operations.
- `app/commands/generated.py` is a factory: `GET` becomes `show`, `POST` becomes
  `set`, `PUT`/`PATCH` becomes `update`, and `DELETE` becomes `delete`. Generic
  writes use `json|file <payload-or-path>` until a curated command adds friendly
  arguments.
- `generate_feature_flags.py` regenerates `settings/features.json`; existing flag
  states are preserved and newly discovered flags default `false`.
- Smoke test **fails** if the catalog drifts from the specs. Fix is just to re-run
  the generator.

### 3.3 Per-field metadata — the field library

The structured commands (e.g. `set address`) need to know each field's *kind*
(free value / fixed choice / optional keyword), the choice options, and a human
hint. Seed a **field library** in code (`app/settings/command_structure.py`)
keyed by `(object, field)` with a generic fallback by field name. Choices for
`set address type` come straight from the spec's `oneOf` variants. (Design it so
this could later be generated from the specs the same way the resource catalog is.)

### 3.4 Command docs — `dev/generate_command_docs.py`

- Each command's `docs/commands/<slug>.md` is the **single source of truth** for
  its help, beginning with YAML front-matter:
  `command, description, usage, feature_flag, category, scope, api`.
- The script idempotently ensures every registered command has front-matter
  (adding it without clobbering a human-edited body), and regenerates
  `docs/commands/index.md` and `docs/commands/api-reference.md`.
- `app/settings/command_help.py` reads the front-matter and applies
  `description`/`usage` onto each `CommandDef`, so inline `?` help and the full
  `help <command>` page come from the same file.

---

## 4. Configuration & Auth (`app/config.py`, `app/cli.py`)

- `ArcConfig` (with nested `SCMConfig`) is a dataclass loaded once at startup;
  env vars override the config file which overrides defaults.
- **Secrets go to the OS keychain** (`keyring`): bearer token, OAuth client
  secret, SSH password. The config file (`config/<os_username>/config.json`, mode
  0600, dir 0700) holds **non-sensitive** values only (client_id, tsg_id, SSH
  user/key path/port, default folder, active profile). If keychain storage fails,
  **fail closed** — save only non-sensitive config and tell the user to use
  keychain or temporary env vars.
- SCM auth: OAuth client credentials (`client_id`+`client_secret`+`tsg_id`,
  scoped `scope=tsg_id:<id>`) preferred; a pre-issued bearer token is the
  fallback. Token endpoint uses HTTP Basic.
- **Named profiles**: a `profiles` dict + `active_profile` field let multiple SCM
  service accounts coexist (e.g. read-only vs read-write). Keychain keys are
  profile-scoped (`<key>.<profile>`); the `default` profile uses historic
  non-suffixed keys. `arc auth configure --profile <name>` creates them; `account
  <name>` switches inside the shell. Migrate any legacy `~/.arc/config.json`
  automatically on first run.
- Typer CLI surface: `arc` (launch shell), `arc auth configure|show|test`,
  `arc scm ...`, `arc docs`. Secret prompts must use non-echoing input
  (`getpass`), never plain `input()`. A `_mask()` helper ensures secrets are
  never printed in clear.

Environment variables: `SCM_BEARER_TOKEN, SCM_CLIENT_ID, SCM_CLIENT_SECRET,
SCM_TSG_ID, ARC_SSH_USER, ARC_SSH_KEY, ARC_SSH_PASS, ARC_DEBUG, ARC_DEV_MODE`.

---

## 5. SCM Client (`app/api/client.py`)

- One `SCMClient` class. Base URLs are **constants taken from each spec's
  `servers[0].url`** (objects/security/setup/network/identity on
  `api.strata...`, IAM/tenancy on `api.sase...`, auth on `auth.apps...`). The same
  bearer token works on all.
- Generic `get_config(domain, path, folder)` powers the auto-generated commands;
  explicit getters/setters for the hand-written commands. Always pass the active
  folder as `?folder=`. Always set timeouts. Raise a typed `SCMError`; never leak
  raw exception text or secrets to the user.
- `arc auth test` verifies which endpoints the current credentials can reach.

---

## 6. Command Registry Pattern (`app/commands/`)

- `base.py`: shared types only — `CommandDef` (fields: `description, category,
  scope, api_handler, ssh_command, render, feature_flag, usage`),
  `ExecutionContext` (`scm, ssh, config, device, folder, tsg_id`, plus `target` /
  `device_host` properties), and guards `require_scm` / `require_device` /
  `parse_kv_tail` / `merge_common_fields`. No handler logic here.
- Each domain module (`setup, objects, security, network, identity, operations,
  packet_tracer`) exports `COMMANDS: dict[str, CommandDef]`. Handlers are private
  module-level `def _handler(ctx, args)` — **never lambdas**, never in
  `registry.py`/`base.py`.
- `registry.py` is a **thin assembler**: merge all domain dicts (generated first),
  apply doc front-matter overrides, build `SORTED_COMMANDS` (longest key first)
  and `CATEGORIES`, and expose `match_command(tokens)`.
- **Scope** is mandatory on every `CommandDef`:
  - `"folder"` — config/policy/objects/network (passes `folder=ctx.folder`).
  - `"device"` — needs an active device (`cd <device>`); blocked otherwise.
  - `"global"` — TSG-wide (devices, jobs, commit, snippets).
- `render` is a string key into a dispatch table in the shell; add a matching
  renderer in `formatter.py` for new output shapes.
- **Live operational state** (CPU/mem, traffic logs, ping, live routing) is not in
  SCM — those commands return a clear message directing the operator to `--remote`
  (SSH). Never say "translation pending"; show the `--remote` usage.

Module → SCM URI mapping: setup `/config/setup/v1`, objects
`/config/objects/v1`, security `/config/security/v1`, network
`/config/network/v1`, identity `/config/identity/v1`; operations = jobs/commit
(SCM) + live device (SSH); packet_tracer = client-side rule-base simulation.

---

## 7. Structure-Aware Parsing & Completion (`app/settings/command_structure.py`)

This subsystem makes `set <object> ...` ergonomic for humans while mapping cleanly
to the API body. It is the single brain shared by the parser, the tab completer,
and the `?` help.

### 7.1 The user-facing file — `settings/command-structure.csv`

Dead simple, one line per command: the object then its fields in order.

```
# object,field,field,...
address,name,type,value,description,tag
```

Reorder a command by moving the field names. **Nothing else** lives here — no
kinds, choices, hints, or code. The loader maps `<object>` → `set <object>` and
resolves each field through the field library (§3.3). (Also accept a richer
`command-structure.json` as an advanced fallback when no CSV exists.)

### 7.2 Quote-free, greedy tokenization

Tokenize quote-aware (shlex with a safe fallback). A value with spaces *may* be
quoted but should not *need* to be — the app figures out where each field ends:

- A free **value** slot followed by a fixed **choice** slot absorbs words until a
  word matches one of the choices (so a multi-word name ends when the type keyword
  appears: `set address my web host fqdn x` → name = "my web host").
- The **last** positional value absorbs words until a known trailing keyword.
- A trailing **keyword** value absorbs words until the next known keyword.
- Quotes remain as the escape hatch for the rare value that contains a reserved
  word (a choice token, or `description`/`tag`).

Implement one shared `_walk(spec, tokens)` that returns `(assignments,
positionals, next_state)` and build three things on top of it:

- `parse(spec, remainder)` — used by `registry.match_command` for execution
  (greedy string handling; returns the same `_positional` + name/id/host shape the
  positional parser produces, so handlers are unchanged).
- `completion_options(spec, typed)` — used by the tab completer.
- `help_options(spec, typed)` — used by the `?` help (token/description/variable).

### 7.3 Completion behaviour (tab)

- First Tab shows the menu (so single, non-inserting hints are visible); later
  Tabs cycle. A **required value slot never returns an empty result** — it shows a
  clear `Enter …` hint. Choice slots list the options with per-option hints.
  Optional keywords appear once positionals are filled.

---

## 8. Context-Sensitive Help (Cisco-style `?` / `??`)

- `?` is bound to **submit immediately** (no Enter). Pressing `?` a second time on
  the same unchanged prefix escalates to `??` (since an instant-submit `?` cannot
  type a literal double). Track `_last_q_prefix` to detect the repeat; reset it on
  any real command.
- `<command> ?` (brief): show **only the next syntax options** for the slot the
  operator is on, driven by `help_options` — fixed choices with descriptions, a
  user-supplied `<variable>` with its "Enter …" hint, or the trailing keywords.
  Render one per line, token column aligned, indented.
- `<command> ??` (full): show the full `help <command>` docs page.
- Worked example (the acceptance target):
  ```
  set address ?              → <name>      Enter a unique name for the address object
  set address web1 ?         → ip-netmask / ip-range / ip-wildcard / fqdn (with hints)
  set address web1 fqdn ?    → <value>     Enter the value for the chosen type
  set address web1 fqdn x ?  → description / tag
  ```
- Two-mode help overall: bare `?`/`help` = compact 3-tier context listing
  (GLOBAL / FOLDER / DEVICE / SHELL); `<command> help` / `help <topic>` = full docs
  rendered from `docs/`. Progressive collapse: prefix help shows only the next
  valid token(s), never a full dump.

---

## 9. The Shell (`app/shell/` mixin package)

`ArcShell` is composed from one-concern mixins so any behaviour lives in exactly
one small file:

- `_base.py` — shared spine: imports, constants, `ShellState`, `tokenize`,
  prompt-toolkit key bindings (`?`/`??`, Tab-shows-menu). Mixins do
  `from app.shell._base import *`.
- `completer.py` — `ArcCompleter` (context-aware; device/folder/tsg/profile name
  completion; structure-driven argument completion).
- `dispatch.py` — `_dispatch`: normalize, quote-aware tokenize, shorthand
  expansion, `?`/`??` routing, builtins, then registry.
- `navigation.py` — `cd` / `folder` / `tsg` / `account` / `pwd` + cache refresh.
- `sessions.py` — `connect` / `remote` interactive SSH (transparent PTY byte pipe;
  auth order: agent keys → configured key → default keys → keyboard-interactive
  (auto-fills stored password, surfaces 2FA) → password).
- `execution.py` — `_execute_api` / `_execute_remote` / `_render` (the render
  dispatch table). Enforce scope here (block device-scope without a device, write
  ops outside configure mode, `commit` only in configure mode).
- `help.py` — the `?` help system (inline/full/docs/context).
- `configure.py` — configure mode, `cli` theme ops, feature flags, hidden `dev`.
- `write_cmd.py` — `set` / `set folder` (create).
- `prompt.py` — prompt/banner/startup/goodbye/styling.

Built-ins handled before the registry: `cd, connect, remote, exit, pwd, folder,
folder create, tsg, account, configure, cli, ?, help, help <topic>, docs, clear`,
and a hidden `dev`. Unambiguous Cisco shorthand (`sh sec pol` → `show security
policy`) expands only when a token-prefix resolves to exactly one command.

### Prompt reflects context tier
`arc:global >` (no device, Shared) · `arc:Production >` (named folder) ·
`arc:fw01:device >` (device at Shared) · `arc:fw01:Production >`. Configure mode
uses `#`; development mode appends `:dev`. Never show `:Shared`.

### Configure mode owns all writes
`set` / `set folder` / `commit` / theme writes are blocked outside configure mode
with a clear message.

---

## 10. Feature Flags (`settings/features.json` + `app/settings/features.py`)

- JSON-first map; each flag is `true` (on for all), `"dev"` (hidden until
  development mode), or `false` (off). Keys starting with `_` are comments.
- A `CommandDef.feature_flag` gates a command in `?` help and at runtime.
- Development mode (hidden `dev` command, or `ARC_DEV_MODE=1`) reveals `"dev"`
  commands; prompt shows `:dev`. `feature enable|disable|dev <flag>` saves one
  flag to `settings/features.json`. Generated coverage commands are feature-gated
  and newly discovered flags default to `false`.

---

## 11. Theming & Settings (`settings/` + `app/settings/`)

- `theme.json` → `ArcTheme` (Rich style strings) for help/prompt/banner colours;
  editable via `cli color <key> <style>` in configure mode or by hand.
- `banner.txt` / `goodbye.txt` (Rich markup; `##` lines are comments).
- `cli-structure.yaml` → verb descriptions, section labels, help footer, configure
  banner.
- `app/paths.py` is the **only** place filesystem paths are defined; never
  hard-code an asset path elsewhere.

---

## 12. Rendering (`app/utils/formatter.py`)

- Rich `Table`/`Panel` renderers, keyed by the `render` string on each
  `CommandDef`, dispatched in `execution.py._render`. Provide a generic
  list-table fallback (used by all auto-generated `show <resource>` commands) plus
  specific renderers (system info panel, jobs table, security policy table, etc.).

---

## 13. Developer Tooling (must build these)

- `dev/smoke_test.py` — fast, no network/mocks. Eleven sections: syntax
  (py_compile all of `app/`), imports, registry integrity (no lambdas, required
  fields, scope set, resource-catalog drift), arg parser shapes, config invariants,
  formatter smoke calls, banner column alignment, inline-help/builtin-catalog
  alignment, theme wiring, command-doc front-matter coverage, and `CODE_MAP.md`
  freshness. Supports `--only N,...` and `--file <path>` to run just the relevant
  sections. Runs in the pre-commit hook.
- `dev/generate_code_map.py` → `dev/CODE_MAP.md` — method→line-range map for files
  ≥ ~300 lines, so agents read only the needed range. Smoke checks it for drift.
- `dev/generate_api_index.py` → `dev/API_INDEX.md` — compact endpoint table replacing
  reading raw specs.
- `dev/scaffold.py` — generate a new command's handler stub + `CommandDef` + doc.
- `dev/install_hooks.sh` — install a pre-commit hook that auto-refreshes generated
  maps and runs the smoke test.

---

## 14. Security Requirements (non-negotiable)

- Validate at boundaries; authorize server-side; fail closed.
- Never `str(e)` raw exceptions into user/JSON output; never log secrets/tokens.
- No `eval`/`exec`/shell interpolation; subprocess only with `shell=False`; all
  network I/O has timeouts.
- Secrets only in keychain or temporary env vars — never in `config.json`, never
  in shell profiles. Non-echoing prompts for all secret entry.
- SSH uses `AutoAddPolicy` (acceptable in controlled net-ops; document that host
  keys are not verified). `ARC_DEBUG=1` enables full tracebacks — document the risk.

---

## 15. Coding Standards

- PEP 8/257; type hints on public functions; format with ruff; imports at module
  top (except documented deferred cases); catch specific exceptions; no import-time
  side effects; no global mutable state; context managers for resources; functions
  do one thing (≤ ~50 lines); meaningful domain names (avoid `data`/`temp`/
  `result`); prefer stdlib/comprehensions; pin dependencies; develop in a venv.
- Each non-trivial function gets a 1–3 sentence docstring (purpose, inputs/outputs,
  side effects). Document **groups** of related state with a short table, not every
  variable. Clarity beats cleverness.

---

## 16. Agent Operating Aids (build these too)

- `AGENTS.md` and `.github/copilot-instructions.md` — kept in sync — holding the
  architecture, command-registry rules, SCM gateway map, security baseline, and
  domain keywords for scoped work.
- `README.dev.md` — a keyword dictionary + recipes (add a command, fix a renderer,
  debug table) so routine work needs minimal context.
- `SESSION.md` — gitignored working memory: read at session start, updated after
  each meaningful unit of work, so a dropped connection resumes cleanly.

---

## 17. Build Order (do in this sequence; smoke-test between phases)

1. **Skeleton:** `pyproject.toml`, `app/paths.py`, `app/__init__.py`, `run.py`,
   `app/config.py` (keychain + profiles), a minimal `app/cli.py` that launches an
   empty prompt-toolkit loop. Smoke sections 1–2 green.
2. **SCM client + auth:** `app/api/client.py` with base-URL constants, OAuth +
   bearer, `get_config`, `SCMError`; `arc auth configure/show/test`.
3. **Spec pipeline:** `dev/scm_sources.json`, `dev/docsupdate.py` (pull +
   self-heal + specs/guides/index/manifest/changes), then `generate_api_index.py`.
4. **Coverage:** `generate_resource_catalog.py` → `resource_catalog.py`;
   `commands/base.py`, `commands/registry.py`, `commands/generated.py`. Now every
   folder-scoped `show <resource>` exists. Add `formatter.py` generic list table.
5. **Shell core:** `app/shell/` mixins — prompt/dispatch/execution/navigation +
   `ArcCompleter` + `shell_catalog.py`. Context-aware prompt, scope enforcement,
   tab completion of command names + device/folder caches.
6. **Help system:** `docs.py`, `generate_command_docs.py`, `command_help.py`; two-mode
   help; bare `?` tiers; `<command> help`.
7. **Explicit commands:** hand-write the domain commands that need shaping
   (objects/security/network/identity/operations/setup/packet_tracer), each with a
   doc front-matter file. Explicit wins over generated.
8. **Structured writes:** `command_structure.py` (CSV loader + field library +
   `_walk`/`parse`/`completion_options`/`help_options`), wire into
   `registry.match_command` (parse), the completer, and `?` help. Greedy quote-free
   parsing; `set`/configure mode.
9. **Context-sensitive `?`/`??`** per §8; `Enter …` hints per §7.3.
10. **Settings & polish:** `features.json` + loader + `dev` mode; `theme.json` +
    `cli` ops; banner/goodbye/cli-structure; SSH `connect`/`remote` PTY.
11. **Tooling & docs:** full `smoke_test.py` (11 sections), `generate_code_map.py`,
    `scaffold.py`, pre-commit hook; write `README.md`, `README.dev.md`, `AGENTS.md`.

---

## 18. Acceptance Criteria

- `python dev/smoke_test.py` passes (all sections), with no network or auth.
- Running `docsupdate` (i.e. `python dev/docsupdate.py`) pulls specs, survives
  a renamed source path by self-healing, writes `CHANGES.md`, and regenerates the
  resource catalog + command docs. A brand-new folder-scoped endpoint becomes a
  working `show <resource>` command with **no hand-written code**.
- In the shell:
  - The prompt reflects context tier; `?` lists only valid, in-scope next options;
    `<command> ?` is context-sensitive per §8; `<command> ??` shows full help.
  - `set address ?` walks name → type (choices) → value → description/tag; a
    required value shows an `Enter …` hint, never an empty menu.
  - `set address my web host fqdn api.example.com description primary edge node`
    parses correctly **without quotes**.
  - Write commands are blocked outside configure mode; device-scope commands are
    blocked without a device; live-state commands point to `--remote`.
  - Secrets never touch `config.json`; `arc auth show` masks them.
- Adding a normal command requires only: a domain handler + `CommandDef`, a doc
  front-matter file, an optional renderer, and (if structured) one CSV line — no
  dispatcher/completer/registry edits.

---

## 19. One-Paragraph Summary (if you only read this)

Build a Typer + prompt-toolkit + Rich interactive shell for Palo Alto SCM whose
**entire command surface and help are generated from the vendor's OpenAPI specs**:
a self-healing spec puller writes a local mirror and a resource catalog; a factory
turns OpenAPI operations into feature-gated `show` / `set` / `update` / `delete`
commands; hand-written commands add shaping where needed; each command's help is one
front-matter Markdown file; a tiny curated per-command CSV defines only field *order* while
a code-side field library (seeded from spec `oneOf`s) supplies kinds/choices/hints;
a single `_walk` drives quote-free greedy parsing, structure-aware tab completion,
and Cisco-style `?`/`??` context help; secrets live in the OS keychain with named
profiles; everything is context-aware (folder/device/mode); user-editable assets
live under `settings/`; and a fast 11-section smoke test plus generated code/API
maps keep it all honest.
```

