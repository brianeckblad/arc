# ARC — Build-From-Scratch Prompt

> Paste everything below the line into a capable coding agent. It is a complete
> specification for recreating **ARC (Assisted Remote Console)** from nothing.
> It describes *what to build and why*, not line-by-line code — a good agent
> fills in the implementation. Build in the phase order given; each phase ends
> with a working, testable increment.

---

You are building **ARC (Assisted Remote Console)**: a PAN-OS-style interactive
CLI shell for Palo Alto Networks firewalls managed by **Strata Cloud Manager
(SCM)**. Network operators think in the firewall CLI (`show` / `set` / `commit`,
`?` help, Tab completion, configure mode, `| match`); ARC gives them that
console, but commands execute through **SCM REST APIs** by default, with SSH
passthrough (`--remote`, `connect`) only for data that truly requires a live
device. It is single-user, runs locally, and talks to one SCM tenant at a time.

## Non-negotiable design principles (these define ARC — honor them everywhere)

1. **API-first, SSH only when the data demands it.** Config, policy, objects,
   inventory, jobs, fleet logs → SCM API. Live operational state (BGP peer
   state, sessions, on-box logs) → SSH via `--remote`. When SCM cannot serve
   something, print the exact `--remote`/`connect` syntax — **never fake data,
   never say "translation pending."**
2. **Writes are staged locally, never sent directly.** In configure mode,
   `set`/`update`/`delete` are validated against SCM and queued in memory;
   nothing reaches SCM until `commit`. `abandon` discards the queue at zero
   cost. This lets a colleague commit elsewhere in the tenant without
   colliding, and makes exit-with-pending-changes a safe, explicit decision.
3. **One schema drives everything.** The command surface, help text, docs,
   feature flags, and field syntax are *generated* from the vendor's own
   OpenAPI specs + scraped CLI docs — not hand-maintained. Curated commands
   layer on top and always win. This is exactly how PAN-OS/Junos build their
   CLIs; ARC does it from the operator's side.
4. **Fail closed.** Every generated command is gated by a feature flag that
   defaults **off**. Operators enable what they need.
5. **Token-minimal for LLM development.** The repo is a hub-and-spoke: one hub
   doc routes any task to the smallest file that owns it. Large files carry a
   generated method→line-range map. Generators, not humans, maintain bulk data.
6. **The shell never writes to the repo at startup.** Config generation happens
   only via explicit dev scripts. A boot must leave `git status` unchanged.

## Tech stack

Python ≥3.11, `uv`-managed. Runtime deps: **Typer** (CLI entry), **prompt-toolkit**
(REPL + completion), **Rich** (all rendering), **httpx** (sync HTTP), **paramiko**
(SSH), **pydantic**, **keyring** (OS keychain for secrets), **platformdirs**.
Dev extras: `pytest`, `respx`/`pytest-httpx`, `ruff`. Entry point: `run.py` →
`python run.py`, plus a `arc` console script.

## Three-folder rule (enforce with a single paths module)

- `app/` — code only. Developers/agents edit here.
- `settings/` — user-editable assets, committed, **no code**: banner, theme,
  goodbye messages, feature-flag glossary, CLI structure, PAN-OS source URLs.
- `config/<os_username>/` — per-user, gitignored: `config.json` (non-secret:
  client_id, tsg_id, SSH user/port, profiles) + `preferences.json` (terminal
  prefs, aliases). Secrets (client_secret, bearer token, SSH password) live in
  the **OS keychain**, never on disk. Fail closed if keychain is unavailable.

Never hard-code an asset path; import from `app/paths.py`.

---

## Phase 1 — Config, auth, SCM client

- `app/config.py`: `ArcConfig`/`SCMConfig`/`SSHConfig` dataclasses; named
  profiles (`default` + others); load order env vars > keychain > config.json >
  defaults; `0600` file / `0700` dir; keychain read failure sets a flag the
  shell surfaces as a one-line startup warning (don't silently run with empty
  creds). Env vars: `SCM_CLIENT_ID/SECRET/TSG_ID`, `SCM_BEARER_TOKEN`,
  `ARC_SSH_USER/KEY/PASS`, `ARC_DEBUG`, `ARC_DEV_MODE`, `ARC_FEATURE_<NAME>`.
- `app/api/_auth.py`: ONE OAuth client-credentials flow (TSG-scoped token from
  `auth.apps.paloaltonetworks.com`). Everything that authenticates uses it.
- `app/api/client.py`: `SCMClient`. A single `_request(method, base_url, path,
  *, params, json)` core is the ONLY place HTTP happens. It: retries a 401 once
  by re-authenticating (loop, not recursion — a recording proxy swaps it at
  runtime); retries 429 up to 3× honoring `Retry-After` (cap 15s); returns
  `{}` on empty bodies. A `_list()` helper follows `limit`/`offset` pagination
  to fetch ALL items (50-page safety cap) — list getters must never silently
  truncate. Per-domain base URLs (objects/security/network/identity/setup/
  operations at `api.strata.paloaltonetworks.com/config/<domain>/v1`; IAM at
  `api.sase...`). Getters raise on error — **never** `except: return []`.
- `app/cli.py` (Typer): `arc` launches the shell; `arc auth configure/test/
  show/clear`, `arc config generate`, `arc scm get <path>` (raw passthrough),
  `arc cliup` (build offline browser docs bundle only — never write command docs).
- Validate: `arc auth test` runs a 5-step keychain/config/creds/auth/API
  diagnostic with actionable messages.

## Phase 2 — Command registry + curated commands

- `app/commands/base.py`: `CommandDef` dataclass — `description`, `category`,
  `scope` ("folder"|"device"|"global", **required, no default**), `api_handler:
  Callable(ctx, args)`, `ssh_command: str | Callable | None`, `render: str`,
  `feature_flag: str`, `usage: str`. `ExecutionContext` (`.scm .ssh .config
  .device .folder .tsg_id`). Guards `require_scm`/`require_device`. Factories
  `show_handler(scm_method, folder_scoped=True)` and `delete_handler(...)` so
  trivial handlers are declarative, not copy-paste.
- `app/commands/<domain>.py` (setup, objects, security, network, identity,
  operations, packet_tracer): each exports `COMMANDS: dict[str, CommandDef]`.
  Handlers are named module-level `def _x(ctx, args)` — **no lambdas**. Curated
  commands are the friendly, hand-tuned ones (`show address`, `show security
  policy`, `commit`, `packet-tracer`, live-device stubs, etc.).
- `app/commands/registry.py`: thin merger. `match_command(tokens)` does
  longest-prefix matching over all keys sorted by length desc; returns
  `(key, CommandDef, args)` and stashes `args["_remainder"]` (raw trailing
  tokens — needed later for lossless SSH passthrough). Merge order puts
  generated < PAN-OS < curated so curated always wins.
- Scope rules: SCM config → "folder" (handler passes `folder=ctx.folder`);
  TSG-wide inventory/jobs/commit → "global"; live device state → "device"
  (requires `cd <device>`, runs via SSH).

## Phase 3 — The interactive shell (mixin package)

`app/shell/` is `ArcShell` composed from one-concern-per-file mixins, all
importing a shared spine `_base.py` (`from app.shell._base import *`):

- `_base.py` — shared imports, constants, module helpers, `ShellState`
  (device, folder, tsg_id, configure_mode, caches + their load timestamps,
  `staged_ops`), auto-`__all__`.
- `dispatch.py` — `_dispatch(line)`: the router. Order: alias expansion (single
  pass) → `watch N` → pipe split → builtins → registry. Returns True to exit.
- `navigation.py` — `cd`/`folder`/`tsg`/`account`/`pwd` + cache refresh with a
  staleness TTL (a miss on a >5-min-old cache re-fetches once before erroring).
- `execution.py` — `_execute_api` (feature gate → configure-mode gate → scope
  gate → spinner → handler → `_render`; converts 401/403/404/network/ValueError
  into actionable messages), `_execute_remote` (SSH), `_render` (dispatch on
  `render=` key into formatter functions).
- `help.py` — the `?` system: context-aware inline help (only executable
  commands, next-token-only progressive display, three tiers GLOBAL/FOLDER/
  DEVICE + SHELL), `<cmd> help` → full docs, `help all` → dump. `find command
  keyword <text>` (PAN-OS syntax) searches ALL commands incl. disabled ones.
  The ONE canonical `_is_command_visible()` (flag + visibility) used by
  dispatch, completer, help alike; `_visible_command_keys()` cached (registry
  is ~4,800 keys), invalidated on flag/dev toggles.
- `completer.py` — Tab completion; devices/folders/TSGs/profiles/usage slots,
  and **dynamic object-name completion** (`delete address <TAB>` lists real
  addresses in the folder, cached 60s, negative-cache on failure).
- `configure.py` — configure mode, `cli` theme, `feature` flag mgmt, the setup
  wizard, and the whole staging engine (below).
- `write_cmd.py` — `set` parsing entry.
- `sessions.py` — `connect`/`remote` interactive PTY passthrough.
- `prompt.py` — prompt string (context tiers: `arc:global >`,
  `arc:Production >`, `arc:fw01:device #`; never show `:Shared`), banner,
  goodbye, `_styled`, `_help_cell` (graceful overflow for long keys).
- Unambiguous Cisco-style prefix expansion (`sh sec pol` → `show security
  policy`); ambiguous prefixes list matches instead of guessing.

## Phase 4 — Staging engine + commit family

The centerpiece. In configure mode, `_execute_api` routes writes to
`_stage_write` instead of executing:
- Run the command's real handler against a **recording SCMClient** where GETs
  pass through (so name→id resolution and existence checks genuinely validate)
  but POST/PUT/PATCH/DELETE are captured, not sent. Store `{command, args,
  folder, ops}` in `ShellState.staged_ops`.
- `show config` lists the queue. `commit` replays captured ops in order then
  pushes the candidate; a mid-replay failure keeps the rest staged and skips
  the push. `commit watch` polls the push job to completion. `commit check`
  re-runs validation against current SCM state (catches an object a colleague
  deleted). `commit confirmed [min]` captures the running config version, arms
  a timer, and auto-reverts (load old version + push) unless `commit confirm`
  arrives — Junos's safety net; exiting arc with a pending window forces a
  decision. `abandon` clears the queue (SCM never touched). Folder creation is
  the one immediate exception (staged objects may target the new folder).

## Phase 5 — Generated command surface (schema → commands)

- `dev/generate_resource_catalog.py`: read every pulled SCM OpenAPI spec, emit
  `app/commands/resource_catalog.py` (deterministic list of dicts: command,
  method, base_url, path, params, feature_flag `<resource>_read|_write`,
  category, spec). GET→show, POST→set, PUT/PATCH→update, DELETE→delete.
- `app/commands/generated.py`: turn each catalog entry into a feature-gated
  `CommandDef`. Generated `set` commands with flat bodies get real field syntax
  (below); the rest take `json|file <payload>`. Generated commands have **no
  doc file** — `help` synthesizes a page from the CommandDef.
- `dev/generate_field_library.py` → `app/settings/field_catalog.py`: from each
  POST request-body schema, emit CLI field specs (name/type/value slots, enum
  choices, `oneOf` variant groups like address types, `pattern`/`maxLength`).
  This powers Tab completion, `?` hints, greedy no-quote parsing, and
  prompt-time validation (`set cngfw tags web color red` → validates the color
  enum, canonicalizes casing, rejects bad input BEFORE staging).
- `app/settings/command_structure.py`: the arg-spec walker consumed by the
  registry parser, completer, and help. Merges the generated field catalog with
  a hand-written `settings/command-structure.json` (curated always wins).

## Phase 6 — PAN-OS full CLI catalog (scraped docs → commands)

- `settings/panos-sources.json`: user-editable registry of PAN-OS CLI-docs URLs
  (ops hierarchy, config hierarchy, per-version added/deleted pages).
- `dev/panosupdate.py`: fetch each page (plain-text CLI hierarchy in the HTML),
  extract command lines, write diffable mirrors to `docs/panos-cli/`.
- `dev/generate_panos_catalog.py` → `app/commands/panos_catalog.py`: normalize
  ~43k raw lines into ~4,500 command stems — trie-based enum collapse
  (`CHAP|PAP|…`), prefix folding, versioned tombstones from delta pages,
  Panorama-only branches tagged and filtered. `dev/panos_curation.json` holds
  overrides + `recovery_stems` (break-glass set) + `scm_map` (op stem → SCM
  ops-job).
- `app/commands/panos_generated.py`: op commands run an SCM ops-job when mapped
  (live device data over SCM's management tunnel — no SSH, no 2FA), else print
  `--remote` guidance; SSH passthrough re-emits `args["_remainder"]` verbatim.
  Config commands are break-glass: SSH via a scripted `configure`-mode channel
  with a mandatory DRIFT WARNING; all off except a curated `panos_config_recovery`
  family. All op families default off (~125 `panos_<family>` flags).

## Phase 7 — SLS fleet logs, config visibility, UX batch

- `app/api/sls.py`: `SLSClient` (Strata Logging Service query API — async job
  POST → poll → results). `show log traffic|threat|system` query across the
  whole tenant with `src/dst/port/rule/app/last/limit` filters; `show log
  detail <n>` for full records; `--remote` kept as the real-time single-device
  path (SLS lags minutes). SQL built with proper value-escaping.
- `app/commands/config_view.py`: `show config running/versions`, `show config
  format set [<resource>]` (dump folder config as replayable set commands by
  inverting the field-catalog payload map), `load config version <id> confirm`
  (rollback with a preview unless confirmed).
- Output pipes in dispatch: `| match`/`except`/`count`/`json`/`save <file>`
  (regex, case-insensitive; `save` strips ANSI, must be last op). **Never call
  it grep** — the idiom is `| match`.
- `watch [N] <command>` (re-run on interval, reuses pooled SSH → one 2FA),
  `history [n]`, `alias` (persisted in preferences.json, single-pass expansion),
  `terminal length/width/spinner` (per-user pager prefs; no terminal-size
  auto-detect — `length 0` = no paging, the default).

## Phase 8 — Feature-flag glossary

`settings/features/` — one small JSON file per domain (`scm-<spec>.json`,
`panos-ops.json`, `panos-config.json`; curated flags live beside their spec
siblings). Values `true`/`"dev"`/`false`; missing = off. SCM resources get
`<resource>_read`/`_write` pairs; PAN-OS gets per-family flags. A "dev" flag is
hidden until development mode (hidden `dev` command / `ARC_DEV_MODE`).
`dev/generate_feature_flags.py` regenerates the directory, preserving existing
states, routing each flag to its owning file. `feature show|find|enable|disable|
dev` manage them at runtime and persist to the right file.

## Phase 9 — Docs, generators, validation

- `docs/`: user manual rendered in-shell by `help <topic>` (`usage.md`,
  `architecture.md`, `configuration.md`), plus `docs/commands/*.md` — ONLY
  hand-written command pages (generated commands synthesize help; never create
  stubs). `docs/scm-api/` holds pulled specs.
- Spoke docs for token efficiency: `COMMAND_PATTERNS.md`, `RENDER_CATALOG.md`,
  `COMMANDDEF_REFERENCE.md`, `dev/API_INDEX.md` (one line per endpoint),
  `dev/CODE_MAP.md` (method→line-range for large files, generated).
- `AGENTS.md` — **the hub**: a keyword→files routing table (say "network" /
  "logs" / "feature" → the one or two files that own it), project structure,
  the source-of-truth hierarchy, add-a-command recipe, validation matrix,
  debug table. One instruction file, not three.
- `dev/docsupdate.py` orchestrates the pull + regeneration chain: pull SCM
  specs (self-healing source registry) → resource catalog → field library →
  PAN-OS pull + catalog → feature flags → command docs → API index → then
  self-verify with smoke sections 1-3. Adding a new API version is: add a URL,
  run docsupdate.
- `dev/smoke_test.py`: ~11 section structural test suite (syntax, imports,
  registry integrity + catalog drift, arg parser + pipes + prefs, config types,
  formatters, banner/help alignment, feature-file JSON validity + all flags
  resolve, theme, code-map freshness). Fast, no network. Pre-commit hook runs
  sections 1-3 and refreshes CODE_MAP. `dev/generate_command_docs.py` prunes
  stub docs and regenerates the index; `dev/scaffold.py` stubs a new command.

## Definition of done

- `python run.py` launches; boot leaves `git status` unchanged.
- `python dev/smoke_test.py` all green.
- A new SCM API version flows in with only a URL edit + `docsupdate`.
- Every generated command is off by default; curated commands shadow generated.
- No command ever fakes device data; writes never touch SCM before `commit`;
  `| match` (never grep) is the filter vocabulary.
- One hub doc (`AGENTS.md`) routes any dev task to the smallest owning file;
  large files have a generated line-range map; a folder README explains how to
  change files in that folder.

Build it phase by phase, keeping the smoke suite green at each step.
