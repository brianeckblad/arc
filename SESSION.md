# Session Notes
<!-- Gitignored. Read by all agents at session start. Updated automatically. -->

## Current Work
**Goal:** Refactor — move user-customizable assets to a `settings/` folder, make features JSON-driven, set an MVP feature set, add a Cisco-ASA-style packet-tracer, break up monolithic shell.py, refresh docs + AGENTS.md.
**Branch:** main
**Status:** in-progress

**Plan (phased, each validated with `python dev/smoke_test.py`):**
- PHASE 1: create `settings/` folder; move banner/goodbye/theme/cli-structure there; features JSON-first (`settings/features.json` = source of truth); MVP defaults (most off).
- PHASE 2: add `packet-tracer` (Cisco-ASA alias of test-security-policy-match), context-aware.
- PHASE 3: split `app/shell.py` (2843 lines) into `app/shell/` package via mixins.
- PHASE 4: docs cleanup + AGENTS.md rewrite (new structure + keyword system).

**Key decisions:**
- `settings/` (repo root, committed) = ALL user-editable assets. `config/<user>/config.json` = secrets only.
- `settings/features.json` = on/off source of truth; valid flags derived from registry; missing flag → False.
- MVP ON: show devices, show address, show security policy, show snippets/snippet/device snippets, cd folder, test-security-policy-match / packet-tracer.

**Files in play:** app/theme.py, app/cli_structure.py, app/features.py, app/shell.py, dev/smoke_test.py, settings/*

---

## Checkpoints

