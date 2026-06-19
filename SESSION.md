# Session Notes
<!-- Gitignored. Read by all agents at session start. Updated automatically. -->

## Current Work
**Goal:** Refactor — settings/ folder, JSON-first features, MVP, packet-tracer, docs/AGENTS.
**Branch:** main
**Status:** done (Phases 1, 2, 4) — Phase 3 (shell split) staged + documented in AGENTS.md

**Completed:**
- PHASE 1 ✅ settings/ folder (banner, goodbye, theme.json, cli-structure.yaml, features.json, README); app/paths.py; features JSON-first (dict, no dataclass); MVP defaults (8 on / 53 off); feature show ENABLED/DISABLED.
- PHASE 2 ✅ app/commands/packet_tracer.py — folder rule-base simulation (`packet-tracer` + `test security-policy-match`), --remote SSH fallback; docs page.
- PHASE 4 ✅ AGENTS.md structure rewrite + keyword system (settings/feature/theme/identity/packet-tracer keywords) + Phase-3 shell-split plan; README.dev.md + docs path fixes; features.md rewritten JSON-first.
- PHASE 3 ⏳ shell.py split into app/shell/ package — NOT done; precise plan committed in AGENTS.md (mixins, CODE_MAP line ranges). Next agent can execute cheaply.

**Validation:** 103/103 smoke checks; live shell verified (MVP commands, feature toggles, packet-tracer wired).

**Key facts for next session:**
- settings/ = user-editable (no code). config/<user>/ = secrets. app/ = core code.
- settings/features.json is THE feature on/off source of truth.
- app/paths.py holds all asset paths — never hard-code.

---

## Checkpoints
