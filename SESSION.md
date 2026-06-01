# Session Notes
<!-- Gitignored. Read by all agents at session start. Updated automatically. -->
<!-- Clear with: wipe | Clear and archive with: arc -->

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

## Checkpoints

