# ARC — Assisted Remote Console

ARC is a PAN-OS-style interactive CLI shell for Palo Alto Networks firewalls
managed by **Strata Cloud Manager (SCM)**. It gives network operators the
familiar `show` / `set` / `commit` workflow of a firewall console, but commands
execute through SCM REST APIs by default — with transparent SSH passthrough
(`--remote`, `connect`, `remote <device>`) for anything that truly needs live
device state.

Who it's for: network operators who think in CLI, teams that want one console
for a whole SCM tenant (config, policy, fleet logs, device recovery), and
anyone tired of clicking through the SCM web UI to change an address object.

## Quickstart

```bash
# install (uv-managed project)
uv pip install -e .
arc                      # or, without installing: python run.py

# first run — credentials (stored in the OS keychain, never in files)
arc auth configure       # wizard: client_id / client_secret / TSG / SSH
arc auth test            # 5-step connectivity + auth diagnostic
# or, inside the shell, type `setup` for the guided two-question wizard

# build the offline browser docs portal (run once after install, and after `docs update`)
arc cliup                # downloads vendor JS/CSS + bundles all docs → docs/index.html

# first commands
arc:global > show devices
arc:global > folder Production        # scope SCM calls to a folder
arc:Production > show address
arc:Production > cd fw-dallas-01      # device context (no SSH yet)
arc:fw-dallas-01:Production > ?       # context-aware inline help
```

Environment variables override everything: `SCM_CLIENT_ID`, `SCM_CLIENT_SECRET`,
`SCM_TSG_ID`, `SCM_BEARER_TOKEN`, `ARC_SSH_USER`, `ARC_SSH_KEY`, `ARC_DEBUG=1`.

## How each major feature works

### API-first execution, SSH when needed

Every command runs through SCM by default (`show security policy`,
`show address`, `show devices`). Live device state that SCM cannot serve is
never faked: the command either runs as a live-device operations job over
SCM's management tunnel, or prints the exact `--remote` / `connect` syntax to
run instead. `connect` / `remote <device>` open a true interactive SSH session
— ARC becomes a transparent byte pipe until you type `exit` on the device.

```text
show routing protocol bgp peer --remote    # SSH: one 2FA per device per session
```

### Configure mode + local staging → commit

All writes (`set` / `update` / `delete`) require configure mode (`configure`,
prompt ends in `#`) and are **staged locally, never sent directly**. Each write
is validated against SCM (names resolved, schemas checked) and queued; `show
config` lists the queue; SCM is untouched until you commit. Exiting configure
mode with staged changes forces a decision (commit / abandon / cancel). The one
exception: folder creation is immediate, so staged objects can target it.

```text
arc:global # set address web1 fqdn web1.example.com
✓ Validated and staged: set address web1  (1 pending)
arc:global # commit check          # re-validate the queue without applying
arc:global # commit watch          # apply + push, then follow the job live
arc:global # commit confirmed 5    # Junos-style: auto-revert in 5 min unless
arc:global # commit confirm        #   ...you confirm in time
arc:global # abandon               # discard the queue — SCM never touched
```

### Feature-flag glossary — `settings/features/`

Every command is gated by a flag in the per-domain glossary
(`settings/features/scm-<spec>.json`, `panos-ops.json`, `panos-config.json`).
Values: `true` (on), `"dev"` (hidden unless development mode), `false` (off);
a missing flag is off — fail closed. SCM resources get per-operation flags
(`show_address`, `create_address`, `update_objects`, `delete_objects`); PAN-OS
commands are gated per family (`panos_debug_ike`, `panos_config_rulebase`).

```text
feature show | feature find address | feature enable show_zone   # one session
dev                      # toggle development mode (reveals "dev" flags)
```

Permanent changes: edit the JSON and restart. CI: `ARC_DEV_MODE=1`,
`ARC_FEATURE_<NAME>=on|dev|off`.

### Generated command surface (~1,050 commands from OpenAPI)

Every operation in the pulled SCM OpenAPI specs becomes a feature-gated
command automatically (GET→`show`, POST→`set`, PUT/PATCH→`update`,
DELETE→`delete`) via `app/commands/resource_catalog.py` + `generated.py`.
All default **off** until an operator enables them. Hand-written commands with
the same name always win. Generated commands get help pages synthesized at
runtime — no doc stubs exist or should be created.

### Schema-driven field syntax for `set` commands

`app/scripts/generate_field_library.py` reads each POST request-body schema and gives
flat resources real CLI fields instead of raw JSON blobs — with Tab
completion, `?` hints, greedy no-quote parsing (ARC works out where a
multi-word value ends), and prompt-time validation: required fields, enum
choices, oneOf variant groups (address types), plus spec `pattern` and
`maxLength` checks before anything is staged.

```text
arc:global # set address my web host fqdn example.com    # no quotes needed
```

Curated commands opt in via the hand-written `settings/command-structure.json`
(field order only), which always wins over the generated catalog.

### PAN-OS command catalog — the full op tree, built in

The whole PAN-OS CLI hierarchy (show / clear / request / test / debug …) is
scraped from the official docs pages listed in `settings/panos-sources.json`
by `app/scripts/panosupdate.py` (diffable mirrors in `docs/panos-cli/`), then compiled
by `app/scripts/generate_panos_catalog.py` into `app/commands/panos_catalog.py`.
Enable families with `feature enable panos_<family>`. Three execution paths:

```text
show dns-proxy statistics all    # SCM ops-job over the device tunnel — no SSH, no 2FA
show routing protocol bgp peer   # unmapped → ARC prints the exact --remote syntax
show routing protocol bgp peer --remote   # SSH, typed tokens passed through losslessly
```

### Break-glass device recovery (with drift warning)

When SCM is down, the PAN-OS **config** tree is available over SSH. The
`panos_config_recovery` family (mgmt IP/DNS/gateway, interfaces, panorama)
is on by default; everything else stays hidden until enabled. Every
device-local config command prints a **DRIFT WARNING** — SCM may overwrite
local changes on its next push. Finish with `commit --remote`.

### SLS fleet logs — `show log`

`show log traffic|threat|system` queries the tenant's Strata Logging Service
(`app/api/sls.py`) across **every** firewall forwarding logs — no device
context needed. Keyword filters, time windows, and a detail drill-down:

```text
show log traffic src 10.1.1.5 port 443 last 24h limit 50
show log detail 3                 # full record for row 3 of the last query
show log traffic --remote         # real-time tail on one device via SSH
```

### Config visibility & rollback

```text
show config running [<resource>]      # the running config version / one resource
show config versions [<id>]           # SCM config-version history
show config format set [<resource>]   # folder objects as replayable `set` lines
load config version <id> confirm      # rollback: load a version as candidate
```

(`show config` bare stays the staged-changes view in configure mode.)

### Output pipes — `| match`, `| except`, `| count`, `| json`, `| save`

Any output-producing command can be filtered PAN-OS-style; filters chain, and
`| save <file>` must come last:

```text
show devices | match PA-4 | count
show devices | json | save devices.json
```

### watch — re-run on an interval

```text
watch 10 show routing protocol bgp peer --remote   # every 10s, Ctrl-C stops;
                                                   # the SSH session is reused (no extra 2FA)
```

### Aliases, history, terminal preferences

Per-user, stored in `config/<user>/preferences.json`, loaded at launch:

```text
alias slt show log traffic     # define; then: slt | match deny
alias delete slt
history 50                     # last 50 commands, numbered (pipes work too)
terminal length 24             # pager; 0 = off (default)
terminal width 120             # 0 = auto-detect
terminal spinner off
```

### find — search everything, even disabled commands

```text
find command keyword nat       # PAN-OS style: searches ALL commands,
                               # including feature-disabled ones, and says
                               # which flag would enable each hit
```

### Tab completion — context-aware and live

Completion knows where you are: devices after `cd ` / `remote `, folders after
`folder `, TSGs after `tsg `, profiles after `account `, then usage-driven
argument slots. Curated `set` commands use structure-aware completion from
`settings/command-structure.json`. Name slots of `delete X` / `update X`
offer **existing object names fetched live from SCM** (cached ~60 s per
folder). `sh sec pol` expands unambiguous prefixes to `show security policy`.

### Help system

`?` is Cisco-style inline help: progressive, context-aware, only commands you
can actually run right now (GLOBAL / FOLDER / DEVICE / SHELL tiers).
`<command> help` or `help <command>` opens the full docs page; `help all` is
the unfiltered dump; `docs` opens the offline browser bundle.

### docsupdate — the self-maintaining pipeline

`python app/scripts/docsupdate.py` pulls every SCM OpenAPI spec + guide from pan.dev
(self-healing when pan.dev renames files), writes `docs/scm-api/` +
`CHANGES.md`, then chains all generators — resource catalog, field library,
PAN-OS mirrors + catalog, feature flags, command docs, API index — and
self-verifies with `app/scripts/smoke_test.py --only 1,2,3`. If Palo Alto ships a new
API resource, ARC learns it (as a gated command + flag + docs) on the next run.

## The three-folder rule

| Folder | Contains | Who edits |
|---|---|---|
| `app/` | code only | developers / agents |
| `settings/` | user-editable assets — no code (flags, banner, theme, structure) | anyone; edit + restart |
| `config/<os_username>/` | per-user secrets + preferences (gitignored; keychain-backed) | `arc auth configure` |

Never hard-code an asset path — import from `app/paths.py`.

## Project layout

| Path | What it is | README |
|---|---|---|
| `app/` | the application: CLI entry, shell, commands, API clients | [app/README.md](app/README.md) |
| `app/commands/` | command registry: curated + generated + PAN-OS CommandDefs | [app/commands/README.md](app/commands/README.md) |
| `app/shell/` | the interactive REPL, split into one-concern mixins | [app/shell/README.md](app/shell/README.md) |
| `app/settings/` | loaders for `settings/` files + the generated field catalog | [app/settings/README.md](app/settings/README.md) |
| `app/api/` | SCM REST client + SLS log-query client | [app/api/README.md](app/api/README.md) |
| `settings/` | operator-editable assets (flags, theme, banner, structure) | [settings/README.md](settings/README.md) |
| `app/scripts/` | generators, docsupdate, scaffolder, smoke suite | [app/scripts/README.md](app/scripts/README.md) |
| `docs/` | user-facing Markdown rendered by `help` + mirrored API specs | [docs/README.md](docs/README.md) |
| `config/<user>/` | secrets + terminal preferences (gitignored) | — |

## Development

Start with **[AGENTS.md](AGENTS.md)** — the hub, especially if you are an LLM.
It routes every task keyword to the one or two small files that own it: the
add-a-command recipe, the SCM gateway map, the validation matrix, and the
error→file debug table. Validate any change with:

```bash
python app/scripts/smoke_test.py            # full suite (~140 checks, no network)
```

**The token-optimization story in five lines:** AGENTS.md is a hub with small
spoke files (`docs/COMMAND_PATTERNS.md`, `app/scripts/API_INDEX.md`, …) so no one reads
a 2,500-line module to answer a question. `app/scripts/CODE_MAP.md` maps every method
in large files to exact line ranges — read the range, not the file. Keyword
routing ("say `render`, touch `formatter.py`") sends each task straight to its
owner. The result: humans and agents alike spend tokens on the change, not the search.
