# `app/scripts/` — Developer Tooling & Generators

Everything in this folder is **build-time / maintenance tooling**. None of it
ships to end users or is imported by the running app (`app/`). It keeps ARC's
command surface, help, and reference docs **generated from the vendor docs**
(SCM OpenAPI specs + PAN-OS CLI hierarchy pages) rather than hand-maintained,
and keeps the codebase honest via the smoke suite.

## TL;DR — what runs what

```
docsupdate  →  python app/scripts/docsupdate.py
                 │  (pulls + mirrors the pan.dev SCM specs/guides, self-healing)
                 ├─► generate_resource_catalog.py → app/commands/resource_catalog.py
                 ├─► generate_field_library.py    → app/settings/field_catalog.py
                 ├─► panosupdate.py               → docs/panos-cli/*.txt mirrors
                 ├─► generate_panos_catalog.py    → app/commands/panos_catalog.py
                 ├─► generate_feature_flags.py    → settings/features/*.json
                 ├─► generate_command_docs.py     → docs/commands front-matter + index + api-reference
                 ├─► generate_api_index.py        → app/scripts/API_INDEX.md
                 └─► smoke_test.py --only 1,2,3   (self-verify: registry still loads)

pre-commit hook (.git/hooks/pre-commit, installed by app/scripts/install_hooks.sh)
                 ├─► generate_code_map.py  → app/scripts/CODE_MAP.md  (when app/*.py staged)
                 └─► smoke_test.py --quiet

manual / on-demand
                 ├─► scaffold.py "show bgp routes" network    (new command stub)
                 ├─► test_sls.py                              (SLS unit tests, offline)
                 └─► generate_code_map.py                     (after big edits)
```

`docsupdate.py` is the orchestrator: after a successful pull it chains the
generators above (in that order, via subprocess) and finishes with a smoke
self-verify. It does **not** run `generate_code_map.py` — that belongs to the
pre-commit flow.

## Scripts

| Script | What it does | Run by | Outputs |
|---|---|---|---|
| **`docsupdate.py`** | Pulls every SCM OpenAPI spec + conceptual guide from pan.dev's GitHub, **self-heals** renamed source paths (updates `settings/scm-sources.json`, records `relocations`), writes the mirror + `CHANGES.md`/`MANIFEST.md`, then chains all generators + smoke verify. `--check`, `--list-remote`, `--self-test` (offline tests). | `docsupdate` trigger / manual | `docs/scm-api/**` + everything downstream |
| **`panosupdate.py`** | PAN-OS sibling of docsupdate: pulls the pages in `settings/panos-sources.json`, extracts CLI command lines (conservative — ambiguous lines are quarantined, never guessed), writes diffable mirrors + `docs/panos-cli/CHANGES.md`. | `docsupdate.py`; manual | `docs/panos-cli/*.txt` |
| **`generate_resource_catalog.py`** | Every spec operation → generated command metadata (GET→show, POST→set, PUT/PATCH→update, DELETE→delete) with a deterministic feature flag. | `docsupdate.py`; manual; `--check` in smoke §3 | `app/commands/resource_catalog.py` |
| **`generate_field_library.py`** | POST request-body schemas → real CLI field syntax for generated `set` commands (ordered args, variant groups, `pattern`/`maxLength` validation metadata). | `docsupdate.py`; manual | `app/settings/field_catalog.py` |
| **`generate_panos_catalog.py`** | Compiles the `docs/panos-cli/` mirrors + `panos-curation.json` into the PAN-OS command catalog (deterministic 7-pass normalization; deletions become version tombstones). | `docsupdate.py`; manual | `app/commands/panos_catalog.py` |
| **`generate_feature_flags.py`** | Regenerates the `settings/features/` glossary (one file per domain: `scm-<spec>.json`, `panos-ops.json`, `panos-config.json`; `curated.json` only as a normally-empty fallback). Existing values preserved; new flags default `false`. Absorbs + removes a legacy single `features.json`. | `docsupdate.py`; manual | `settings/features/*.json` |
| **`generate_command_docs.py`** | Refreshes front-matter on **existing** command docs, prunes boilerplate stubs, rebuilds the command index + API reference. Never creates per-command stub files — undocumented commands get help synthesized at runtime. | `docsupdate.py`; manual | `docs/commands/*.md`, `index.md`, `api-reference.md` |
| **`generate_api_index.py`** | Condenses all pulled specs into one compact endpoint table so agents never read raw YAML. | `docsupdate.py`; manual | `app/scripts/API_INDEX.md` |
| **`generate_code_map.py`** | AST-parses every ≥300-line file under `app/` into a method → line-range map. | pre-commit hook; manual; freshness checked by smoke §11 | `app/scripts/CODE_MAP.md` |
| **`smoke_test.py`** | Structural test suite, 14 sections (syntax, imports, registry, arg parser, token opts, config, formatter, banner, inline-help alignment, theme+docs, code-map freshness, command visibility, configure/commit flow, browser consoles + new commands). No network. `--only N,…`, `--file <path>`. | pre-commit hook; manual after any `app/` change | exit 0/1 |
| **`test_sls.py`** | Offline unit tests for `app/api/sls.py` + the `show log` commands (fake HTTP transport). | manual | exit 0/1 |
| **`scaffold.py`** | New command boilerplate: handler stub + `CommandDef` snippet + doc file from one line. | manual | stub under `app/commands/` + `docs/commands/` |
| **`install_hooks.sh`** | Installs the pre-commit hook (CODE_MAP refresh + smoke). Run once per clone. | manual (once) | `.git/hooks/pre-commit` |

## Data & generated files in `app/scripts/`

| File | Kind | Source of truth? | Notes |
|---|---|---|---|
| `settings/scm-sources.json` | data (editable) | **yes** | Registry of pan.dev spec/guide paths (lives in `settings/`, not here); docsupdate self-updates it on renames. Hand-edit only when discovery can't find a moved file. |
| `panos-curation.json` | data (editable) | **yes** | PAN-OS catalog knobs: token overrides, recovery stems, `scm_map` (op command → SCM ops-job). Edit, then rerun `generate_panos_catalog.py`. |
| `API_INDEX.md` / `CODE_MAP.md` | generated | no | Don't hand-edit; smoke enforces CODE_MAP freshness. |
| `DOCS_AGENT.md` | doc | n/a | Playbook for the `docsupdate` docs-agent workflow. |

## Common tasks

```bash
python app/scripts/docsupdate.py                 # full refresh (self-healing) + all generators
python app/scripts/docsupdate.py --check         # report drift, write nothing
python app/scripts/smoke_test.py                 # full suite
python app/scripts/smoke_test.py --only 1,2,3    # syntax + imports + registry
python app/scripts/smoke_test.py --file app/commands/network.py   # auto-selects sections
python app/scripts/scaffold.py "show bgp routes" network --scope folder --render list
python app/scripts/panosupdate.py && python app/scripts/generate_panos_catalog.py   # PAN-OS only
python app/scripts/generate_code_map.py          # after moving methods in a 300+ line file
bash app/scripts/install_hooks.sh                # one-time hook install
```

## Outputs that live outside `app/scripts/` (intentional — they ship with ARC)

- `app/commands/resource_catalog.py`, `app/commands/panos_catalog.py`,
  `app/settings/field_catalog.py` — AUTO-GENERATED; never hand-edit.
- `settings/features/*.json` — generated structure; **flag values** are the
  operator's to edit.
- `docs/commands/*.md` front-matter + `index.md` + `api-reference.md`;
  `docs/scm-api/**`; `docs/panos-cli/**`.
