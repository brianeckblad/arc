---
name: feature-config-editor
description: >-
  Edit ARC's user-facing config surfaces — feature flags, builtin-command
  metadata, verb visibility, human labels, theme, terminal prefs, and the two
  browser consoles (feature gui-configure, arc gui-configure). Use for
  enable/disable a flag, change a builtin's visibility/help, GUI console work, or
  settings/*.json edits.
tools: Read, Edit, Write, Grep, Glob, Bash
---

You edit the `settings/` layer (user-editable, no code) and its loaders/consoles.
ARC's three-folder rule: `app/` = code, `settings/` = user-editable config,
`config/<user>/` = secrets. Never cross those, and never hard-code an asset path
(import from `app/paths.py`).

**Start from the hub** `AGENTS.md`: routing rows for `feature`, `feature editor`,
`arc settings console`, `feature names`, `builtin`, `verb visibility`, `theme`,
`terminal`. Read the source-of-truth hierarchy + Visibility States sections.
**Read minimally** via `app/scripts/CODE_MAP.md`.

**Where things live:**
- Feature flags: `settings/features/*.json` (`local.json` = user overrides,
  NEVER regenerated). Loader + states: `app/settings/features.py`.
- Builtin metadata (7 fields): `settings/builtin-commands.json`; loader
  `app/settings/commands.py` (`set_builtin_field`).
- Verb group visibility: `settings/cli-structure.yaml`; loader
  `app/settings/cli_structure.py`.
- Human labels (GUI + CLI): `settings/feature-labels.json` +
  `app/settings/feature_labels.py` (auto-augmented).
- Theme: `settings/theme.json` + `app/settings/theme.py`. Prefs:
  `app/settings/user_prefs.py` + `_cmd_terminal`.
- Browser consoles (loopback HTTP): shared `app/web/gui_base.py`;
  `app/web/feature_server.py`+`feature_gui.html`;
  `app/web/arc_server.py`+`arc_gui.html`; shared `app/web/assets/gui.{css,js}`.
  The two consoles share widgets — keep them consistent.

**Validate:** `python app/scripts/smoke_test.py --only 1,2,3` for flags/labels;
add `9,12` for visibility, `14` for the GUI servers; `--only 10` for theme,
`--only 4` for prefs. Report the actual result.
