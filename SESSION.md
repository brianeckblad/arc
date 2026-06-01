# Session Notes
<!-- Gitignored. Read by all agents at session start. Updated automatically. -->
<!-- Clear with: wipe | Clear and archive with: arc -->

## Current Work
**Goal:** configure mode for all write/change operations + CPI/AGENTS trigger simplification
**Branch:** main
**Status:** done

**Recent progress:**
- `app/shell.py` — added Cisco-style configure mode state with `#` prompt and `configure` / `conf` / `conf t` entry
- `app/shell.py` — enforced write guards: `folder create` and `commit` now require configure mode
- `app/shell.py` — moved CLI theme edits under `cli` subcommand (configure mode only)
- `app/shell.py` — `exit` now leaves configure mode first, preserving `e` shorthand behavior
- `app/shell.py` — fixed top-level tab completion display to show full command candidates (e.g. `configure`, `connect`) instead of suffix fragments (e.g. `f`)
- `app/shell.py` — removed explicit `conf` built-in visibility; `conf` now works only as shorthand expansion to `configure`, and `conf t` is no longer listed
- `app/shell.py` — startup `Loaded:` line now includes device health split: total devices plus `(x) connected (y) disconnected`
- `app/shell.py` — startup order updated: banner -> SCM connected/Loaded -> CLI quick-help (so status appears before command hints)
- `app/shell.py` — `Loaded:` line refined: removed folder count section and removed dim styling so no numbers appear dim
- `app/shell.py` — connection indicator updated: green `✓` on SCM connected, red `✗` when SCM is unavailable/not configured
- `app/shell.py` — `?` help now filters to currently executable commands only (no locked/unavailable entries; device commands hidden until device context exists; `commit`/configure-only actions gated by mode)
- `app/shell.py` — in configure mode, bare `?` now shows only configure-relevant commands (`commit`, `folder create`, `cli`, `exit/quit`) and hides read-only operational listings
- `app/shell.py` — prefix `?` help now collapses to next-token options globally (e.g. `show jobs ?` -> `all`, `id`; `show device ?` -> `<enter>`, `devices`, `snippets`) instead of dumping full matching command lines
- `app/shell.py` — bare tiered `?` now also collapses each scope to top-level next tokens (e.g. `show`) rather than printing full leaf command lists
- `app/shell.py` — bare tiered `?` refined to two-word stems (e.g. `show jobs`, `show device`) so help remains collapsed but still specific
- `app/shell.py` — configure-mode `?` now keeps read-only `show ...` stems visible alongside configure actions; `show folder` / `show folders` alias added to list folders from any mode
- `app/api/client.py` — folder APIs now filter `/folders` records to real container folders only (exclude `type: on-prem` device entries) so folder create parent selection never shows devices as folders
- `app/shell.py` — exit message now loads random lines from `app/goodbye.txt` instead of hardcoded `Goodbye.`
- `app/goodbye.txt` — added operator-themed goodbye message list (one line chosen at random per exit)
- `.github/copilot-instructions.md` + `AGENTS.md` — expanded senior readability standards to require brief function intent notes and grouped-variable documentation with a lightweight table pattern
- `.github/copilot-instructions.md` + `AGENTS.md` — added a mini good-vs-bad example showing function-intent docstrings and grouped state ownership notes
- `.github/copilot-instructions.md` + `AGENTS.md` — added explicit strict context-aware `?` help requirement and availability examples
- `dev/smoke_test.py` — synced builtin expectations with configure/cli command model
- `.github/copilot-instructions.md` + `AGENTS.md` — replaced `ucp`/`synca` with unified `cpi` trigger and updated `evala` sync semantics
- `.github/copilot-instructions.md` + `AGENTS.md` — updated configure command documentation to canonical `configure` command with shorthand note

**Key decisions:**
- Configure mode is the single gate for write/change operations in shell workflows
- Entering configure mode resets context to `arc:global #` for predictable mutation flow
- Keep `e -> exit` unambiguous by not introducing an `end` built-in alias

**Files in play:**
- `app/shell.py` — configure mode, prompt, write guards, `cli` command
- `dev/smoke_test.py` — builtin sync updates
- `.github/copilot-instructions.md` — trigger and configure-mode rule updates
- `AGENTS.md` — synced trigger and configure-mode rule updates

**Open questions / blockers:**
- none

---

## Current Work
**Goal:** ls folder + folder create — folder tree view and interactive folder creation
**Branch:** main
**Status:** done

**Recent progress:**
- `ls folder` — fetches folder hierarchy + devices, renders Rich tree with devices in their folder
- `folder create <name>` — interactive parent selection via numbered tree list, confirm, POST to SCM, refresh cache
- `app/api/client.py` — added `create_folder(name, parent)` to POST /config/setup/v1/folders
- `app/utils/formatter.py` — added `format_folder_tree(folders, devices)` using Rich Tree, `_folder_flat_list(folders)` for numbered selection menu
- `app/shell.py` — `_cmd_devices(args)` routes `ls folder` to `_cmd_ls_folder()`; `_cmd_folder` handles `create` subcommand; completer updated

**Key decisions:**
- Folder hierarchy from `parent` field on folder records; roots = folders whose parent is absent or not in the known set
- `ls folder` shows Rich Tree with device count + names inline on each folder node
- `folder create` shows numbered flat list with depth indentation so users navigate "above" (shorter path) or "below" (deeper) when picking parent
- Parent selection accepts both number and raw folder name
- Cache refreshed after folder creation so new folder appears in tab completion immediately

**Files in play:**
- `app/api/client.py` — create_folder()
- `app/utils/formatter.py` — format_folder_tree(), _folder_flat_list()
- `app/shell.py` — _cmd_ls_folder(), _cmd_folder_create(), dispatch + completer updates

**Open questions / blockers:**
- none

---

## Current Work
**Goal:** Two-mode help system — Cisco-style `?` inline + `<cmd> help` docs page
**Branch:** main
**Status:** done

**Recent progress:**
- Replaced single `?`/`help` handler with two focused modes
- `?` (bare or `show ?`) compact Cisco-style inline listing: one line per command, 3-tier GLOBAL/FOLDER/DEVICE sections, no Rich panels
- `<command> help` (trailing `help`) full docs page from `docs/` — e.g. `cd help`, `show address help`
- `help <topic>` still works (calls same `_cmd_help_docs`)
- `help all` full unfiltered dump (unchanged)
- Early dispatch intercept catches trailing `help` before any individual builtin handler
- Removed old `_cmd_help_contextual` and `_cmd_context_help` methods entirely
- Added `_cmd_help_inline`, `_cmd_help_docs` (new), updated `_cmd_help_full` and `_print_shell_builtins`
- CPI updated with two-mode help table

**Key decisions:**
- `?` is always the fast inline scan (Cisco muscle memory) — no panels, just lines
- `<cmd> help` is the manual page gateway — mirrors Cisco `?` + `show help` pattern
- The 3-tier GLOBAL/FOLDER/DEVICE structure is preserved in inline mode

**Files in play:**
- `app/shell.py` — _cmd_help_inline, _cmd_help_docs, _dispatch early help intercept, _print_shell_builtins
- `.github/copilot-instructions.md` — two-mode help table added

**Open questions / blockers:**
- none

---

## Current Work
**Goal:** Multi-account / named credential profiles — switch accounts without restarting ARC
**Branch:** main
**Status:** done

**Recent progress:**
- `app/config.py` — full profile system: `_DEFAULT_PROFILE`, `profile_name` on `ArcConfig`, `list_profiles()`, `get_active_profile()`, `set_active_profile()`, `delete_profile()`, profile-aware `load_config(profile=)` and `save_config(cfg, profile=)`, profile-scoped keychain keys, legacy backward compat
- `app/shell.py` — `_cmd_account()` built-in, tab completion for `account <name>`, `account` in dispatch, `_print_shell_builtins()` updated, `_print_banner()` shows active profile when multiple exist, `_cmd_pwd()` shows active profile, `_init_clients()` shows profile+tsg
- `app/cli.py` — `--profile` on `auth_login`, `auth_show` lists all profiles, `auth_clear --profile`, `auth_test --profile`, new `auth delete-profile` command
- `docs/commands/account.md` — new doc with usage, examples, typical workflow

**Key decisions:**
- Named profiles in config.json `profiles` dict + `active_profile` field (AWS CLI / kubectl pattern)
- Profile-scoped keychain keys: `scm.bearer_token.<profile>` — `default` profile uses legacy non-suffixed keys for full backward compat
- Existing single-profile configs auto-read as `default` profile; migrated to new format on first `save_config()`
- `account <name>` clears device + folder + TSG context (new creds = different scope) and persists active profile
- Rollback on switch failure keeps previous config/client active
- `pwd` always shows active profile name so operators always know which account they are on

**Files in play:**
- `app/config.py` — profile system
- `app/shell.py` — account command + UX updates
- `app/cli.py` — auth subcommands updated
- `docs/commands/account.md` — new doc

**Open questions / blockers:**
- none

---

## Current Work
**Goal:** Context-aware CLI help — 3-tier command visibility (global -> folder -> device)
**Branch:** main
**Status:** done

**Recent progress:**
- Implemented 3-tier contextual help display (global / folder / device) in `_cmd_help_contextual()`
- Help is now always context-aware (`?` at root shows tiers, not the full dump)
- `help all` still forces the unfiltered full reference
- `_context_annotation()` refactored: all folder-scope commands show folder, all device-scope show device when set
- Fixed `show interface` ssh_command: replaced inline lambda with named `_ssh_interface()` function
- Fixed `show device snippets` scope: "device" to "global" (handler validates name arg itself)
- `show jobs id` from previous session: scope "global", real SCM API handler, render="jobs"

**Key decisions:**
- Commands organized by context tier in help (not by API category) — mirrors PAN-OS/Panorama CLI
- Folder-scope commands always available (Shared is a valid folder) but annotated with active folder name
- Device-scope commands shown dim with nav hint when no device; shown bright with device name when set
- `help all` remains as escape hatch for full unfiltered view

**Files in play:**
- app/shell.py
- app/commands/network.py — _ssh_interface named function
- app/commands/setup.py — show device snippets scope fix
- app/api/client.py — get_job() method
- app/commands/operations.py — show jobs id real handler

**Open questions / blockers:**
- none

---

## Current Work
**Goal:** CLI theming, editable banner, and dev smoke-test relocation
**Branch:** main
**Status:** done

**Recent progress:**
- Moved startup banner content into `app/banner.txt` with Rich markup comments/colour guidance; root `banner.txt` removed
- Added `app/theme.py` + `app/cli_theme.json` for editable CLI colour roles
- Added `conf` / `configure` shell command with `conf show`, `conf color <key> <style>`, and `conf reset`
- Made `?` inline help use theme colours and fixed Rich markup alignment issues by replacing `[device]` / `[name]` with `<device>` / `<name>`
- Moved `smoke_test.py` to `dev/smoke_test.py`, updated pre-commit hook, and expanded smoke coverage to 82 checks
- Synced `.github/copilot-instructions.md` and `AGENTS.md` with smoke-test and help-system changes

**Key decisions:**
- No runnable code in repo root; developer scripts live under `dev/`, editable app assets live under `app/`
- `app/banner.txt` is the source of truth for banner spacing, colours, subtitle/legal text, and logo content
- Theme roles are stored in `app/cli_theme.json`; shell command `conf color` updates the file without requiring code edits
- Smoke tests now validate CLI alignment, builtin sync, theme files, banner location, imports, syntax, registry integrity, formatter basics, and config invariants

**Files in play:**
- `app/shell.py` — theme-aware inline help, `conf` command, banner path update, help alignment fixes
- `app/theme.py` — `ArcTheme`, `load_theme()`, `save_theme()`, `reset_theme()`, theme key registry
- `app/cli_theme.json` — editable default CLI theme roles
- `app/banner.txt` — editable Rich-markup startup banner
- `dev/smoke_test.py` — relocated and expanded smoke suite
- `.githooks/pre-commit` — runs `python3 dev/smoke_test.py --quiet`
- `.github/copilot-instructions.md` / `AGENTS.md` — updated workflow and maintenance guidance

**Open questions / blockers:**
- none; `python dev/smoke_test.py` currently passes 82/82

---

## Checkpoints

### 2026-06-01 — CLI theming + banner externalization + smoke-test relocation

**Branch:** main
**Status:** checkpoint saved

**Summary:**
- Externalized banner into `app/banner.txt`; banner owns all logo/subtitle/legal text, colour tags, and blank-line spacing.
- Added theme system in `app/theme.py` with editable `app/cli_theme.json`.
- Added shell configuration entry points: `conf`, `configure`, `conf show`, `conf color <key> <style>`, and `conf reset`.
- Updated `?` inline help to use theme roles and fixed misalignment caused by Rich interpreting `[device]` / `[name]` as markup.
- Moved root `smoke_test.py` to `dev/smoke_test.py`; no runnable code remains in root from this work.
- Updated pre-commit hook to run `python3 dev/smoke_test.py --quiet` before version bump.
- Synced CPI and `AGENTS.md` previously; both include smoke-test guidance and help-system rules.

**Validation:**
- `python dev/smoke_test.py` → `ALL OK 82/82 checks passed`

**Changed/untracked files at checkpoint:**
- Modified: `.githooks/pre-commit`, `.github/copilot-instructions.md`, `AGENTS.md`, `app/shell.py`
- Added/untracked: `app/banner.txt`, `app/cli_theme.json`, `app/theme.py`, `dev/smoke_test.py`

**Next suggested step:**
- Review CLI theme UX in a live shell (`arc`, then `?`, `conf show`, `conf color command_name bold green`, `?`, `conf reset`) before committing.
