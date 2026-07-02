# Docs Agent Mode — Playbook

A focused operating mode for an AI agent whose job is **only** the SCM
documentation lifecycle: pull the latest docs, help the user understand them,
and update ARC's API calls when pan.dev changes.

Keep this mode narrow. Do not refactor unrelated code while in docs mode.

---

## When to enter docs mode

The user says any of: `docsupdate`, `update docs`, `pull api docs`,
`docs agent`, `check api changes`, or asks "did the SCM API change?".

---

## The three jobs

### 1. Pull + self-heal (no manual path hunting)

```bash
python dev/docsupdate.py --check    # report drift/relocations, write nothing
python dev/docsupdate.py            # apply: download, self-heal moves, write CHANGES.md
                                         # → also auto-regenerates dev/API_INDEX.md
                                         # → regenerates app/commands/resource_catalog.py
                                         #   (100% coverage: every new list endpoint → a command)
                                         # → and runs dev/generate_command_docs.py (command-doc
                                         #   front-matter + docs/commands/index.md + api-reference.md)
```

## Coverage policy — generated and feature-gated

ARC generates command metadata for the pulled SCM OpenAPI operations. You never
hand-write boilerplate for every endpoint:

- `dev/generate_resource_catalog.py` reads every pulled OpenAPI spec and writes
  `app/commands/resource_catalog.py` entries for `GET`, `POST`, `PUT`/`PATCH`,
  and `DELETE` operations.
- `app/commands/generated.py` turns each catalog entry into a real, feature-gated
  command. `GET` becomes `show`, `POST` becomes `set`, `PUT`/`PATCH` becomes
  `update`, and `DELETE` becomes `delete`.
- `dev/generate_feature_flags.py` writes `settings/features.json`; new generated
  flags default to `false`, so generated commands stay hidden until intentionally
  enabled.
- This runs automatically inside `docsupdate`, so a new pan.dev endpoint becomes
  command metadata, docs, API-index rows, and feature flags with **zero** manual
  boilerplate.
- Smoke **section 3** fails if `resource_catalog.py` drifts from the specs — run
  `python dev/generate_resource_catalog.py`.

Curated explicit commands still win over generated commands when they share a key;
use curated handlers for high-priority commands that need friendly arguments,
custom rendering, or endpoint-specific request-body builders.

- Source paths live in `dev/scm_sources.json` (editable registry).
- If a file 404s, the tool searches the live pan.dev tree and **auto-updates**
  the registry with the new path (recorded under `relocations`). You do not
  hand-edit paths unless discovery cannot find a match.
- If discovery fails for an item, open `dev/scm_sources.json` and fix that one
  path; re-run. Use `python dev/docsupdate.py --list-remote` to see live
  spec paths.
- Every doc under `products/scm/docs/` is mirrored (curated names + any new
  doc auto-slugged). Use `--no-mirror` to pull only the curated set.

### 2. Read the change report + help the user

After a pull, read **`docs/scm-api/CHANGES.md`**. It lists, per domain:

- **Relocated source files** — pan.dev renamed/moved a spec.
- **Added** endpoints — new API surface ARC could expose.
- **Removed** endpoints — endpoints ARC may already call that no longer exist.

Summarize this for the user in plain language. For deeper questions, read the
specific spec at `docs/scm-api/specs/<category>.md` or a guide at
`docs/scm-api/guides/<name>.md`. Use `dev/API_INDEX.md` for a compact overview.

Each endpoint entry in `specs/<category>.md` now records the **deep schema
detail** ARC needs (not just the path):

- **Container scope** — `folder | snippet | device`: the SCM container the
  object lives in (config can live in a snippet or on a device, not only a
  folder). For `POST`/`PUT` this is `(in request body)`.
- **Body schema** + **Required fields**.
- **Type variants (oneOf/anyOf)** — the nested choice, e.g. an aggregate
  interface's `layer2 | layer3`, or an ethernet interface's
  `aggregate_group | tap | layer2 | layer3`.

When implementing a `set`/`update` command, read these to know which variant
fields and container the endpoint accepts.

### 3. Update affected ARC code

Only the **Removed** and **changed** endpoints require code action. Workflow:

1. For each removed endpoint, grep ARC for the path/handler:
   ```bash
   grep -rn "advanced-device-objects" app/api/client.py app/commands/
   ```
2. If ARC calls a removed/renamed path, update `app/api/client.py` (the URL)
   and any handler in `app/commands/<module>.py`.
3. For **Added** endpoints the user wants exposed, use the normal add-command
   flow (`dev/scaffold.py`, see `AGENTS.md` → Add a Command) — that is a feature, not a docs fix.
4. **Update the command's help in ONE place** — its `docs/commands/<slug>.md`
   front-matter (`description`, `usage`, `api`) and body. That single file feeds
   both the inline `?` help and the full `help <command>` page. Then run
   `python dev/generate_command_docs.py` to refresh the index + API reference.
5. Validate: `python dev/smoke_test.py --only 1,2,3,10`.

---

## Single source of truth — where each thing lives

| Concern | Owner (edit here) | Generated from it |
|---|---|---|
| Upstream API spec | `docs/scm-api/` (pulled — never hand-edit) | `dev/API_INDEX.md`, `CHANGES.md` |
| Command behavior | `app/commands/*.py` + `app/api/client.py` | — |
| Command help (short + long) | `docs/commands/<slug>.md` front-matter + body | `?` / `help` text, `index.md`, `api-reference.md` |

When Palo adds a feature to an existing API you touch **two** files: the code
(`client.py`/handler) and the one command doc. `?`, `help`, the command index,
and the API→command map all update from those.

---

## Guardrails

- Do not commit `dev/scm_sources.json` relocation churn without reading
  `CHANGES.md` first — a relocation means an upstream rename you should
  understand.
- Never invent endpoint paths. The only sources of truth are the pulled specs
  under `docs/scm-api/specs/` and `dev/API_INDEX.md`.
- Keep docs-mode edits scoped to: `dev/scm_sources.json`, `app/api/client.py`,
  the affected `app/commands/<module>.py`, and the matching `docs/commands/*.md`.
- Secrets never appear in docs or specs — do not paste tokens into examples.

---

## Quick reference

| Need | Command / file |
|---|---|
| See what changed | `docs/scm-api/CHANGES.md` |
| Pull + self-heal | `python dev/docsupdate.py` |
| Dry-run report | `python dev/docsupdate.py --check` |
| List live spec paths | `python dev/docsupdate.py --list-remote` |
| Validate engine offline | `python dev/docsupdate.py --self-test` |
| Editable source paths | `dev/scm_sources.json` |
| Compact endpoint table | `dev/API_INDEX.md` |
| Refresh command-doc front-matter + index/api-ref | `python dev/generate_command_docs.py` |
| One domain's endpoints | `docs/scm-api/specs/<category>.md` |
| Conceptual guide | `docs/scm-api/guides/<name>.md` |

