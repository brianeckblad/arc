# `dev/` — Developer Tooling & Generators

Everything in this folder is **build-time / maintenance tooling**. None of it
ships to end users or is imported by the running app (`app/`). It exists to keep
ARC's command surface, help, and reference docs **generated from the vendor API
specs** rather than hand-maintained, and to keep the codebase honest.

> **Why these live in `dev/` and not `docs/scripts/`:** `docs/` is *content*
> rendered by ARC's help system; these are *programs*. They also resolve the repo
> root via `Path(__file__).parent.parent` — moving them one level deeper would
> break every generated path. `dev/` is the conventional, discoverable home for
> tooling. The dependency map below is the "what does what" you were looking for.

---

## TL;DR — what runs what

```
docsupdate  →  python dev/docsupdate.py
                 │  (pulls + parses the vendor OpenAPI specs, self-healing)
                 ├─► dev/generate_api_index.py        → dev/API_INDEX.md
                 ├─► dev/generate_resource_catalog.py → app/commands/resource_catalog.py
                 └─► dev/generate_command_docs.py     → docs/commands/*.md front-matter
                                                    + docs/commands/index.md
                                                    + docs/commands/api-reference.md

pre-commit hook (.git/hooks/pre-commit, installed by dev/install_hooks.sh)
                 ├─► python dev/generate_code_map.py  → dev/CODE_MAP.md  (when app/*.py staged)
                 └─► python dev/smoke_test.py --quiet

manual / on-demand
                 ├─► python dev/scaffold.py "show bgp routes" network   (new command stub)
                 ├─► python dev/generate_code_map.py                         (after big edits)
                 └─► python dev/extract_variants.py                     (ad-hoc spec analysis)
```

**Key fact:** `docsupdate.py` is the orchestrator. It calls
`generate_api_index.py`, `generate_resource_catalog.py`, and `generate_command_docs.py` (in that
order, via subprocess) after a successful pull. It does **not** call
`generate_code_map.py` or `smoke_test.py` — those belong to the pre-commit flow.

---

## Scripts

| Script | What it does | Run by | Outputs |
|---|---|---|---|
| **`docsupdate.py`** | Orchestrator for `docsupdate`. Pulls every NGFW OpenAPI spec + conceptual guide from the vendor's public GitHub repo, **self-heals** renamed source paths (searches the live tree, updates `scm_sources.json`, records the move), and writes the local mirror. Then chains the three generators below. | `docsupdate` trigger / manual | `docs/scm-api/specs/*.yaml` + `*.md`, `guides/*.md`, `index.md`, `MANIFEST.md`, `CHANGES.md` |
| **`generate_api_index.py`** | Condenses all pulled specs into one compact endpoint table so agents don't read raw YAML. | `docsupdate.py`; manual | `dev/API_INDEX.md` |
| **`generate_resource_catalog.py`** | Reads `docs/scm-api/specs/ngfw-*.yaml`, finds every folder-scoped list `GET`, subtracts endpoints already covered by an explicit `show` command (via each doc's front-matter `api:`), and writes the remainder. The factory in `app/commands/generated.py` turns each into an always-on `show <resource>` command. **100% NGFW coverage with zero hand code.** | `docsupdate.py`; manual; `--check` in smoke §3 | `app/commands/resource_catalog.py` |
| **`generate_command_docs.py`** | Ensures every registered command has YAML front-matter in `docs/commands/<slug>.md` (adds it without clobbering a human-edited body), then rebuilds the command index + API reference. Front-matter is the single source of truth for `?`/`help`. | `docsupdate.py`; manual; `--check` in smoke §10 | `docs/commands/*.md`, `index.md`, `api-reference.md` |
| **`generate_code_map.py`** | Maps method → line-range for files ≥ ~300 lines so agents read only the needed range. | pre-commit hook (when `app/*.py` staged); manual after big edits; drift-checked by smoke §11 | `dev/CODE_MAP.md` |
| **`smoke_test.py`** | Fast structural test suite (11 sections: syntax, imports, registry integrity, arg parser, config, formatter, banner, inline-help/builtin alignment, theme, command-doc coverage, code-map freshness). No network/auth/mocks. Supports `--only N,…` and `--file <path>`. | pre-commit hook; manual (run after any `app/` change) | exit 0/1 |
| **`scaffold.py`** | Generates a new command's handler stub + `CommandDef` entry + doc file from one line. | manual | new files under `app/commands/` + `docs/commands/` |
| **`install_hooks.sh`** | Installs the git pre-commit hook (auto-refresh `CODE_MAP.md` + run smoke). Run once per clone. | manual (once) | `.git/hooks/pre-commit` |
| **`extract_variants.py`** | **Ad-hoc, not wired into any flow.** One-off helper that lists `oneOf`/`anyOf` type variants across the specs — used originally to decide which `set` commands need subtype docs. Safe to delete; kept as an occasional diagnostic. | manual only | stdout |

## Data & generated files in `dev/`

| File | Kind | Source of truth? | Notes |
|---|---|---|---|
| `scm_sources.json` | data (editable) | **yes** | The registry of spec/guide source paths. `docsupdate.py` reads it and auto-updates it when a path moves (records `relocations`). Hand-edit if discovery can't find a renamed file. |
| `API_INDEX.md` | generated | no | By `generate_api_index.py`. Don't hand-edit. |
| `CODE_MAP.md` | generated | no | By `generate_code_map.py`. Don't hand-edit; smoke §11 enforces freshness. |
| `DOCS_AGENT.md` | doc | n/a | Playbook for the `docsupdate` "docs agent" workflow. |

---

## Common tasks

```bash
# Refresh the API reference + regenerate coverage commands + command docs
python dev/docsupdate.py            # full run (self-healing)
python dev/docsupdate.py --check    # report drift, write nothing
python dev/docsupdate.py --list-remote   # print live spec paths

# Validate the app after editing app/
python dev/smoke_test.py                 # full suite
python dev/smoke_test.py --only 1,2,3    # syntax + imports + registry
python dev/smoke_test.py --file app/commands/network.py   # auto-selects sections

# Add a new command
python dev/scaffold.py "show bgp routes" network --scope folder --render list

# After moving/renaming methods in a 300+ line file
python dev/generate_code_map.py

# One-time: install the pre-commit hook
bash dev/install_hooks.sh
```

---

## Outputs that live outside `dev/`

These generators write into the app/docs tree (that is intentional — the outputs
ship with ARC; only the generators are dev-only):

- `app/commands/resource_catalog.py` ← `generate_resource_catalog.py` (auto-generated; do not hand-edit)
- `docs/commands/*.md`, `index.md`, `api-reference.md` ← `generate_command_docs.py`
- `docs/scm-api/**` ← `docsupdate.py`
- `dev/API_INDEX.md`, `dev/CODE_MAP.md` ← their generators

