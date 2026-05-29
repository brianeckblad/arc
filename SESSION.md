# Session Notes
<!-- Gitignored. Read by all agents at session start. Updated automatically. -->
<!-- Clear with: wipe | Clear and archive with: arc -->

## Current Work
**Goal:** Context-aware CLI help — 3-tier command visibility (global → folder → device)
**Branch:** main
**Status:** done

**Recent progress:**
- Implemented 3-tier contextual help display (global / folder / device) in `_cmd_help_contextual()`
- Help is now always context-aware (`?` at root shows tiers, not the full dump)
- `help all` still forces the unfiltered full reference
- `_context_annotation()` refactored: all folder-scope commands show `→ folder: X`, all device-scope show `→ device: X` when set
- Fixed `show interface` ssh_command: replaced inline lambda with named `_ssh_interface()` function
- Fixed `show device snippets` scope: `"device"` → `"global"` (handler validates name arg itself)
- `show jobs id` from previous session: scope `"global"`, real SCM API handler, `render="jobs"`

**Key decisions:**
- Commands organized by context tier in help (not by API category) — mirrors PAN-OS/Panorama CLI
- Folder-scope commands always available (Shared is a valid folder) but annotated with active folder name
- Device-scope commands shown dim with nav hint when no device; shown bright with device name when set
- `help all` remains as escape hatch for full unfiltered view

**Files in play:**
- app/shell.py — `_cmd_help()`, `_cmd_help_contextual()`, `_context_annotation()`
- app/commands/network.py — `_ssh_interface` named function
- app/commands/setup.py — `show device snippets` scope fix
- app/api/client.py — `get_job()` method (previous session)
- app/commands/operations.py — `show jobs id` real handler (previous session)

**Open questions / blockers:**
- none

---

## Current Work
**Goal:** show snippet <name> details — fetch and display configured objects within snippet
**Branch:** main
**Status:** done

**Recent progress:**
- Root cause: `GET /config/setup/v1/snippets/{id}` only returns metadata (name, id, variables, folders) — configured objects live in objects/security endpoints and must be fetched with `?snippet=<name>`
- Added `SCMClient.get_snippet_objects(snippet_name)` — queries 11 endpoints (addresses, address-groups, services, service-groups, tags, EDLs, security-rules, url-categories, application-filters, application-groups, log-forwarding) all with `?snippet=<name>`, returns only non-empty sections
- `_show_snippet_detail` now detects `details` as positional[1] and returns `{_render: snippet_detail_full, snippet: ..., objects: {...}}`  
- `format_snippet_detail` (metadata-only path) adds tip "show snippet <name> details → shows configured objects"
- `format_snippet_detail_full` renders header + variables + per-type tables with purpose-built renderers: addresses (type+value), address-groups (static/dynamic), services (proto+port), security-rules (from/source/to/dest/app/action with color), tags; generic fallback for unknown types
- `snippet_detail_full` render key added to shell.py dispatch

**Key decisions:**
- Two modes: `show snippet <name>` = fast metadata; `show snippet <name> details` = full with API calls to all object endpoints
- Per-endpoint failures silently swallowed in get_snippet_objects — 404/403 on a type means "none of that type in this snippet"
- Security rule action colored green/red in the table

**Files in play:**
- `app/api/client.py` — get_snippet_objects() added
- `app/commands/setup.py` — _show_snippet_detail: detects details flag, returns full payload
- `app/utils/formatter.py` — format_snippet_detail cleaned up + tip, format_snippet_detail_full + 6 section renderers
- `app/shell.py` — snippet_detail_full added to render dispatch

**Open questions / blockers:**
- none

---

## Previous Current Work
**Goal:** Full context-awareness audit — fix all gaps, encode rule in CPI
**Branch:** main
**Status:** done

**Audit results — every command and built-in checked:**

REGISTERED COMMANDS:
- `show devices` scope=global but was passing `folder=ctx.folder` to handler → FIXED (removed folder param — SCM devices API is TSG-wide, not folder-scoped)
- All other registered commands: scope declaration matches handler behavior ✓

SHELL BUILT-INS:
- `folder <name>`: was silently accepting any name even when folder cache populated → FIXED (validates against folders_cache; clears device context on folder switch)
- `cd`, `connect`, `remote`, `tsg`: fixed in previous session ✓
- `exit`, `pwd`, `help`, `?`, `docs`, `clear`, `ls`: correctly global/stateless ✓

CPI UPDATED:
- Added "Everything is context-aware by default" as the PRIMARY design rule
- Full enforcement table: cd/folder/tsg/remote validation, scope enforcement, global exceptions
- Rule: every new command/built-in must explicitly decide scope before merging

**Key decisions:**
- `show devices` is TSG-wide (global), not folder-scoped — SCM /devices endpoint returns all visible devices regardless of folder
- `folder` switch clears device context — a device cd'd to in one folder may not be relevant in another
- Empty cache = graceful fallback (SSH stub still allowed) — always show a message explaining why constraint is relaxed

**Files in play:**
- `app/commands/setup.py` — _show_devices: removed folder= param
- `app/shell.py` — _cmd_folder: validates against folders_cache, clears device context on switch
- `.github/copilot-instructions.md` — context-aware as primary rule, full enforcement table

**Open questions / blockers:**
- none

---

## Previous Current Work
**Goal:** TSG-level context awareness — cd/connect refuse invalid devices, tsg switch clears context
**Branch:** main
**Status:** done

**Recent progress:**
- `cd <device>`: when device cache is populated, refuses to create a stub — hard error with TSG name and device count. Only creates a stub when cache is empty (API unavailable)
- `remote <device>` / `connect`: same logic — refuses unknown device when cache populated, falls through to direct SSH only when cache is empty
- `tsg <id>`: now clears device and folder context before switching (both OAuth and bearer-token modes); refreshes caches after switch; warns explicitly when new TSG has 0 devices ("cd and device-scope commands unavailable here")
- `cd ..` output now includes TSG name for clarity
- All rollback on tsg switch failure restores device + folder too (was only restoring tsg_id)

**Key decisions:**
- Populated cache = authoritative — if the API returned a device list and the name isn't in it, it does not exist in this TSG
- Empty cache (API down) = fallback allowed — SSH by hostname/IP still works without SCM
- TSG switch always clears device/folder context — no stale cross-TSG references possible

**Files in play:**
- `app/shell.py` — _cmd_cd, _cmd_connect, _cmd_tsg all updated

**Open questions / blockers:**
- none

---

## Previous Current Work
**Goal:** Make all commands context-aware via explicit scope declaration on CommandDef
**Branch:** main
**Status:** done

**Recent progress:**
- Added `scope: CommandScope` field to `CommandDef` with three values: `"folder"`, `"device"`, `"global"`
- Added `require_device()` helper to base.py
- Annotated all 31 commands with correct scope:
  - DEVICE (19): all operations + network + test security-policy-match + show device snippets
  - FOLDER (8): address, address-group, service, tag, edl, security policy, url-categories, show snippets
  - GLOBAL (4): show devices, show device, show snippet, show snippets global
- `_execute_api` in shell.py enforces device scope before calling handler — gives clear actionable error with cd/--remote hint
- `_cmd_help_contextual` now splits commands into available-now vs needs-device; device-scope commands shown dim with hint
- `_cmd_help_full` shows [device]/[global] scope tags on every command
- Copilot instructions updated with scope table and updated checklist

**Key decisions:**
- Scope is declared on CommandDef, not checked in every handler — single enforcement point in _execute_api
- `"folder"` is the default but every CommandDef must still declare it explicitly (enforced by convention, documented in instructions)
- Device-scope commands still appear in help when no device selected — just visually dim with a note; they don't vanish

**Files in play:**
- `app/commands/base.py` — CommandScope type, scope field on CommandDef, require_device()
- `app/commands/setup.py` — scope annotations
- `app/commands/objects.py` — scope annotations  
- `app/commands/security.py` — scope annotations
- `app/commands/network.py` — scope annotations
- `app/commands/operations.py` — scope annotations
- `app/shell.py` — _execute_api enforcement, _cmd_help_contextual/full updated
- `.github/copilot-instructions.md` — scope table and updated checklist

**Open questions / blockers:**
- none

---

## Previous Current Work
**Goal:** Fix arg parser so bare names aren't treated as key/value pairs
**Branch:** main
**Status:** done

**Recent progress:**
- Root cause: `_parse_args` consumed any two adjacent tokens as key=value, so `show snippet My-Name details` produced `args = {'My-Name': 'details'}` — `args.get('name')` returned None → "Usage: show snippet <name>" error
- Fix: rewrote `_parse_args` with explicit `KEYWORD_PARAMS` set; only tokens in that set consume the next token as a named value; everything else goes to `_positional`
- Explicit `--flag` and `--flag value` handling preserved
- Verified: `show snippet <name> details`, `show snippet <name>`, `ping host <ip> count 3`, `test security-policy-match source <ip> destination <ip>`, `--remote` all parse correctly

**Key decisions:**
- Keyword param allowlist is the right approach — PAN-OS CLI has a fixed grammar, not arbitrary key=value
- `details` after a snippet name is silently ignored (positional[1]) — no separate command needed since show snippet already returns full detail

**Files in play:**
- `app/commands/registry.py` — _parse_args rewritten with KEYWORD_PARAMS allowlist

**Open questions / blockers:**
- none

---

## Previous Current Work
**Goal:** Fix show snippets folder/device scoping — use folder record as authoritative source
**Branch:** main
**Status:** done

**Recent progress:**
- Root cause: `_snippets_for_folder` was filtering by a `folders[]` array on snippet list items — that field is absent on `/snippets` list responses (only present on detail responses)
- Fix: added `get_folders_full()` to SCMClient — fetches GET /config/setup/v1/folders and returns full records including their `snippets: [name, ...]` list
- Added `_snippet_names_for_folder(scm, folder_name)` helper in setup.py — looks up folder record and returns its snippet names as a set; handles both string and {name:} dict items defensively
- `_show_snippets` rewritten:
  - Device context: merges device.snippets[] + folder record's snippets[] (union, de-duped) — shows both device-level and folder-level attachments
  - Folder context (non-Shared): uses folder record's snippets[] list
  - Shared root: returns all snippets (no meaningful scoping at root)
- `show snippets global` unchanged — always returns everything

**Key decisions:**
- Folder record (GET /folders) is the authoritative source for folder→snippet membership
- Snippet list response does NOT reliably carry folder references — never filter on snippet.folders[]
- Device context merges both device AND folder snippets so operators see everything relevant

**Files in play:**
- `app/api/client.py` — get_folders_full() added
- `app/commands/setup.py` — _snippet_names_for_folder() helper, _show_snippets rewritten

**Open questions / blockers:**
- none

---

## Previous Current Work
**Goal:** Context-aware show snippets and context-aware ? help
**Branch:** main
**Status:** done

**Recent progress:**
- `show snippets` now scoped to context: device → device's snippets; non-Shared folder → snippets attached to that folder (filtered via snippet's `folders[]` array); Shared root → unscoped snippets only
- Added `show snippets global` command — always shows all snippets unfiltered
- `_snippets_for_folder()` helper does client-side filtering since /snippets API has no folder param
- `format_snippets_scoped()` new formatter: shows scope header, snippet table, hint footer as list of renderables
- `snippets_scoped` render key added to shell.py dispatch
- `?` / `help` is now context-aware: in device or non-Shared folder context it shows a shorter relevant menu; `help all` always shows the full list
- Context annotations added to `show ?` prefix matching — e.g. `show snippets ?` says what it will actually return
- `_print_shell_builtins()` extracted as shared helper used by both contextual and full help

**Key decisions:**
- Snippet-to-folder mapping is client-side (snippet objects have a `folders` array of {name:} dicts)
- `show snippets` → context-scoped; `show snippets global` → always all; both use `snippets_scoped` render key
- Context-aware help still shows shell builtins always; registered commands are filtered to prominent categories for the current context

**Files in play:**
- `app/commands/setup.py` — _show_snippets rewritten, _show_snippets_global added, COMMANDS updated
- `app/utils/formatter.py` — format_snippets_scoped() added
- `app/shell.py` — _cmd_help split into _cmd_help_contextual/_cmd_help_full/_print_shell_builtins; _cmd_context_help context annotations

**Open questions / blockers:**
- none

---

## Previous Current Work
**Goal:** Break commands/registry.py into domain modules mirroring SCM URI structure
**Branch:** main
**Status:** done

**Recent progress:**
- Created `app/commands/base.py` — shared types only: CommandDef, ExecutionContext, require_scm(), translation_pending()
- Created `app/commands/setup.py` — /config/setup/v1: devices, snippets (5 commands)
- Created `app/commands/objects.py` — /config/objects/v1: addresses, services, tags, EDLs (5 commands)
- Created `app/commands/security.py` — /config/security/v1: security-rules, url-categories, policy-match (3 commands)
- Created `app/commands/network.py` — SSH operational: interfaces, routing, zones, HA (7 commands)
- Created `app/commands/operations.py` — SSH operational: system, jobs, logs, ping, commit (10 commands)
- Rewrote `app/commands/registry.py` as thin assembler — imports domain COMMANDS dicts, merges, exposes match_command()
- Added format_tags() and format_edl_list() to formatter.py
- Added tags, edl_list, url_categories render keys to shell.py dispatch table
- Updated .github/copilot-instructions.md and AGENTS.md with new structure, module table, and updated command-adding checklist
- Runtime test: 30 commands, 5 categories, prefix matching correct

**Key decisions:**
- Module layout mirrors SCM URI prefix structure: setup/objects/security + network/operations for SSH-only ops
- base.py = types only (no handlers); registry.py = assembler only (no handlers)
- All existing public imports (CommandDef, ExecutionContext, match_command, COMMANDS, CATEGORIES) still work from registry.py — shell.py unchanged

**Files in play:**
- `app/commands/base.py` — new
- `app/commands/setup.py` — new
- `app/commands/objects.py` — new
- `app/commands/security.py` — new
- `app/commands/network.py` — new
- `app/commands/operations.py` — new
- `app/commands/registry.py` — rewritten as assembler
- `app/utils/formatter.py` — added format_tags, format_edl_list
- `app/shell.py` — added tags/edl_list/url_categories render keys
- `.github/copilot-instructions.md` — updated project structure + command pattern docs
- `AGENTS.md` — synced

**Open questions / blockers:**
- none

---

## Previous Current Work
**Goal:** show snippet detail — render all fields including variables and extra sections
**Branch:** main
**Status:** done

**Recent progress:**
- `format_snippet_detail` in `formatter.py` now returns a list of Rich renderables instead of a single Table
- First table: identity/metadata (name, id, type, prefix, shared-in, description, labels, folders)
- Second table: Variables (name, type, default, description) — shown only when present
- Additional tables: any other structured API fields not in the skip-set (e.g. config elements)
- `_render()` in `shell.py` updated to iterate a list of renderables when renderer returns one
- `docs/commands/show-snippet.md` updated to describe the multi-table output

**Key decisions:**
- No separate `show snippet details` command needed — the existing `show snippet <name>` now renders everything
- Returning a list from the formatter is clean; the render dispatch handles both list and single-renderable returns

**Files in play:**
- `app/utils/formatter.py` — format_snippet_detail rewritten
- `app/shell.py` — _render() list-renderable support
- `docs/commands/show-snippet.md` — updated

**Open questions / blockers:**
- none

---

## Previous Current Work
**Goal:** Folder context as core CPI component — always shown in prompt
**Branch:** main
**Status:** done

**Recent progress:**
- Prompt now always shows active SCM folder: `arc:Shared >` at root, `arc:PA-VM-01:Shared >` in device context
- Added `folder` style (bold ansigreen) to PROMPT_STYLE alongside `device` (yellow) and `arc` (cyan)
- `folder` with no args now shows full available folder list with active marker (mirrors `tsg` UX)
- `folder ..` / `folder /` resets to Shared (mirrors `cd ..` for devices)
- `_cmd_pwd` highlights folder with color and explains it scopes all API calls
- `_cmd_cd` clear message now includes current folder for context
- Banner and help text updated to note folder is always in prompt

**Key decisions:**
- Folder is always visible — it is the primary SCM API scope, so operators must always know it
- Prompt format: `arc:<folder> >` or `arc:<device>:<folder> >` — folder is rightmost, closest to the cursor

**Files in play:**
- `app/shell.py` — _prompt(), PROMPT_STYLE, _cmd_folder(), _cmd_pwd(), _cmd_cd(), banner, help

**Open questions / blockers:**
- none

---

## Previous Current Work
**Goal:** Move config from Application Support to project config/<username>/ and add arc auth test
**Branch:** main
**Status:** done

**Recent progress:**
- CONFIG_DIR/CONFIG_FILE now resolves to `<project_root>/config/<os_username>/config.json`
- Legacy `~/Library/Application Support/arc/config.json` silently checked as fallback on first load
- platformdirs import made optional/try-except in config.py (still used by shell.py for HISTORY_FILE)
- `config/*/` added to .gitignore; `config/config.example.json` kept tracked
- Added `arc auth test` command: checks keychain, config file, SCM credentials, SCM auth, live API call (IAM tenants → folders fallback); exits 1 on failure

**Key decisions:**
- Project-local config path uses os username as subdirectory (matches user request: config/<username>/)
- Legacy path migration is silent (debug log only) — no banner nag unless user runs arc auth login
- auth test does not require SSH device context; tests what is actually configured

**Files in play:**
- `app/config.py` — CONFIG_DIR/CONFIG_FILE path change, legacy fallback
- `app/cli.py` — auth test command added
- `.gitignore` — config/*/ added
**Branch:** main
**Status:** done

**Recent progress:**
- Added `tsg` built-in to `ArcShell` — shows or changes the active TSG ID
- `ShellState.tsg_id` seeds from `ArcConfig.scm.tsg_id` at startup
- OAuth flow: `tsg <id>` re-authenticates automatically with new TSG scope
- Bearer-token flow: TSG context is recorded in state; token is used as-is
- `pwd` now shows active TSG; tab after `tsg ` completes with configured TSG
- `ExecutionContext.tsg_id` exposed so API handlers can inspect TSG if needed
- Created `docs/commands/tsg.md`; added entry to `docs/commands/index.md`

**Key decisions:**
- Fail closed on OAuth re-auth: state rolls back to previous TSG on error
- `import copy` placed inline with deferred-import comment (avoids importing at module level for a rare code path)

**Files in play:**
- `app/shell.py` — ShellState, ArcShell._cmd_tsg(), _cmd_pwd(), _make_context(), _cmd_help(), completer
- `app/commands/registry.py` — ExecutionContext.tsg_id field
- `docs/commands/tsg.md` — new doc
- `docs/commands/index.md` — entry added

**Recent progress:**
- Hardened `app/config.py`: secrets are never written to `config.json`; keychain write failures save only non-sensitive config then raise `ConfigSecurityError`; config dir/file permissions enforced as 0700/0600 where supported
- Hardened `app/cli.py`: secret prompts now use `getpass`; `arc auth login` prompts for SSH password for password+2FA workflows; keychain failure message is fail-closed and points to env vars
- Updated config docs/templates to discourage long-lived secrets in shell profiles and remove plaintext secret placeholders
- Created/updated `.github/copilot-instructions.md` and `AGENTS.md` with fail-closed ARC credential storage rules

**Key decisions:**
- Fail closed: no fallback path may persist bearer tokens, client secrets, or SSH passwords to disk
- Environment variables are allowed for temporary shells/CI/secret-manager wrappers only; docs now discourage storing long-lived secrets in shell startup files
- Existing legacy plaintext config values may be read for migration, but the next save strips them from disk; if keychain is unavailable they must be supplied again via env vars

**Files in play:**
- `app/config.py` — keychain helpers, updated load/save, clear_keychain()
- `app/cli.py` — auth login/show/clear updates
- `docs/configuration.md`, `docs/config-{osx,win,nix,generate}.md` — user-facing secure setup docs
- `.github/copilot-instructions.md`, `AGENTS.md` — security design rules for future agents

---

## Previous Work
**Goal:** Context-sensitive `?` help — prompt restores prefix after help display
**Branch:** main
**Status:** done

**Recent progress:**
- `_pending_default` field on ArcShell stores the prefix typed before `?`
- `run()` passes it as `default=` to next `PromptSession.prompt()` call so buffer is pre-filled


**Goal:** Pull in all SCM NGFW API documentation from pan.dev into ideas/scm-ngfw/
**Branch:** main
**Status:** done

**Recent progress:**
- Downloaded 15 OpenAPI YAML specs directly from pan.dev GitHub (PaloAltoNetworks/pan.dev, branch master)
- Generated Markdown endpoint reference from each YAML spec (endpoint-per-heading format)
- Total: 794 endpoints across 8 NGFW categories + 5 Cloud NGFW categories
- Script lives at /tmp/download_ngfw_specs.py if a re-run is needed

**Key decisions:**
- Used GitHub raw YAML specs (not pan.dev HTML scraping) — JS-rendered pages had no real API content
- Raw YAML kept alongside .md so ARC command implementations can reference exact request/response schemas

**Files in play:**
- ideas/scm-ngfw/index.md — master index
- ideas/scm-ngfw/ngfw-{device,identity,network,objects,operations,security,setup}.yaml/.md
- ideas/scm-ngfw/cloudngfw-{identity,objects,operations,security,setup}.yaml/.md
- ideas/scm-ngfw/*device-onboarding*.yaml/.md

---

## Checkpoints
