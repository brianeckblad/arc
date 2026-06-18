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
python dev/update_scm_docs.py --check    # report drift/relocations, write nothing
python dev/update_scm_docs.py            # apply: download, self-heal moves, write CHANGES.md
```

- Source paths live in `dev/scm_sources.json` (editable registry).
- If a file 404s, the tool searches the live pan.dev tree and **auto-updates**
  the registry with the new path (recorded under `relocations`). You do not
  hand-edit paths unless discovery cannot find a match.
- If discovery fails for an item, open `dev/scm_sources.json` and fix that one
  path; re-run. Use `python dev/update_scm_docs.py --list-remote` to see live
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

### 3. Update affected ARC code

Only the **Removed** and **changed** endpoints require code action. Workflow:

1. For each removed endpoint, grep ARC for the path/handler:
   ```bash
   grep -rn "advanced-device-objects" app/api/client.py app/commands/
   ```
2. If ARC calls a removed/renamed path, update `app/api/client.py` (the URL)
   and any handler in `app/commands/<module>.py`.
3. For **Added** endpoints the user wants exposed, use the normal add-command
   flow (`dev/scaffold.py`, see `README.dev.md`) — that is a feature, not a docs fix.
4. Validate: `python dev/smoke_test.py --only 1,2,3`.

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
| Pull + self-heal | `python dev/update_scm_docs.py` |
| Dry-run report | `python dev/update_scm_docs.py --check` |
| List live spec paths | `python dev/update_scm_docs.py --list-remote` |
| Validate engine offline | `python dev/update_scm_docs.py --self-test` |
| Editable source paths | `dev/scm_sources.json` |
| Compact endpoint table | `dev/API_INDEX.md` |
| One domain's endpoints | `docs/scm-api/specs/<category>.md` |
| Conceptual guide | `docs/scm-api/guides/<name>.md` |

