# Agent Operational Guidelines

**Instructions for AI agents working on this project**

> **Source of truth:** This file is synced from
> [`.github/copilot-instructions.md`](.github/copilot-instructions.md),
> which GitHub Copilot reads automatically at the start of every session.
> Use `update cpi` to update this file and Copilot instructions together.

## Quick Navigation

| I need to... | Read this |
|--------------|-----------|
| Add a command | Command Registry Pattern + domain keyword ([network], [security], [objects], [setup], [operations]) |
| Fix formatting output | `app/utils/formatter.py` + [formatter] keyword |
| Update shell help/prompts | `app/shell.py` + [shell] keyword |
| Add SCM API endpoint | SCM Gateway Map section + `app/api/client.py` + [scm-api] keyword |
| Update docs | `docs/` + Documentation Strategy section |
| Run validation | `python dev/smoke_test.py` |
| Review coding standards | `docs/agent-patterns/` (python, javascript, security) |
| Understand token optimization | ARC Domain Keywords + Token-Efficient Development Patterns sections |

---

<!--
  ╔══════════════════════════════════════════════════════════════════╗
  ║  PART 1 — GENERAL WORKFLOW                                       ║
  ║  Reusable rules that apply to any project.                       ║
  ║  Copy this section verbatim to bootstrap a new repo.             ║
  ╚══════════════════════════════════════════════════════════════════╝
-->

## Session Memory - READ FIRST EVERY SESSION

AI agents have no memory between conversations, and connections time out. To
bridge that, this repo keeps a `SESSION.md` file at the repo root that every
agent reads at the start of every session and updates automatically as work
progresses. The file persists until the user explicitly clears it, so a
reconnect or new session picks up exactly where the last one left off.

**File:** `SESSION.md` (repo root, gitignored — local working memory only)

### At the start of every session

1. Use the `read_file` tool to read `SESSION.md`.
2. If it has a **Current Work** block, summarize it in 2–3 lines so the user
   can confirm the context before starting new work.
3. If the file is empty or missing, proceed normally — do not create it yet.

### Automatic session maintenance (no trigger needed)

The agent must keep `SESSION.md` current **without being asked**:

- **After completing any significant unit of work** — feature added, bug fixed,
  decision made, file edited — append or update the **Current Work** block.
- **Before any risky or multi-step operation** — write the current state first
  so a timeout mid-operation leaves a recoverable record.
- **On reconnect** — read the file, confirm context with the user, then continue.

The goal: if the connection drops at any moment, the next session can read
`SESSION.md` and resume without the user re-explaining anything.

### Trigger phrases the user can say

Short forms are the primary triggers. Longer natural-language forms still work.

| User says | Agent does |
|-----------|------------|
| `ck` / `checkpoint` / `save context` / `remember this` | Append a full dated checkpoint entry to `SESSION.md` using the entry template below. |
| `ctx` / `show context` / `recall` / `what were we doing` | Read `SESSION.md` and summarize recent entries. |
| `wipe` / `clear memory` / `start fresh` / `forget everything` | Truncate `SESSION.md` (keep the header template), confirm what was cleared. |
| `arc` / `archive memory` | Move all session entries to `SESSION.archive.md`, then clear. |
| `gitp` / `git push` / `commit and push` | Stage all changes (`git add -A`), commit with a generated message, push to `origin/main`, then print the server update command (see below). |
| `cpi` / `update cpi` / `update copilot instructions` / `update instructions` | Review what was built or decided and update both `.github/copilot-instructions.md` and `AGENTS.md` so they stay in sync. Confirm what changed in each file. |
| `evala` / `evaluate agents` / `evaluate instructions` | Evaluate AI instruction files for clean general vs app-specific separation, then ensure `.github/copilot-instructions.md` and `AGENTS.md` are synced. |
| `agi` / `read agent instructions` / `read copilot instructions` | Read `.github/copilot-instructions.md` and `AGENTS.md` in full, then confirm they have been loaded into context. |
| `docsupdate` / `update docs` / `pull api docs` | Pull the latest provider API/reference specs from the upstream source and regenerate the project's local reference docs. For ARC this runs `python dev/docsupdate.py` (see the SCM Gateway Map section). Confirm which specs changed. |

A short trigger (`ck`, `ctx`, `wipe`, `arc`, `gitp`, `cpi`, `evala`, `agi`, `docsupdate`) is a command only when it is the
entire user message. Inside a longer sentence, treat it as normal text.

### SESSION.md structure

```markdown
# Session Notes
<!-- Gitignored. Read by all agents at session start. Updated automatically. -->
<!-- Clear with: wipe | Clear and archive with: arc -->

## Current Work
**Goal:** one line describing what is being worked on right now.
**Branch:** (git branch name)
**Status:** in-progress | blocked | done

**Recent progress:**
- bullet — what was just completed
- bullet — next up

**Key decisions:**
- bullet (or "none yet")

**Files in play:**
- path/to/file — why

**Open questions / blockers:**
- bullet (or "none")

---

## Checkpoints

<!-- Full dated entries appended here by `ck` / auto-checkpoint -->
```

### `gitp` — Stage, Commit, Push, and Print Update Command

When the user says `gitp` (or any natural-language equivalent):

1. Run `git add -A` to stage all changes.
2. Inspect `git diff --staged --stat` to summarize what changed.
3. Write a conventional-commit message (no internal quotes) describing the changes.
4. Commit using the simple `-m` form (or the `/tmp/msg.txt` file method for multi-line messages).
5. Push to `origin/main`.
6. Print the server update command so the user can copy-paste it (update this for your project):

```bash
cd deployment && ansible-playbook playbooks/update.yml --vault-password-file ~/.vault_pass
```

### `cpi` — Update Copilot + Agent Instructions Together

When the user says `cpi` / `update cpi` (or natural-language equivalent):

1. Read `.github/copilot-instructions.md` and `AGENTS.md`.
2. Apply required instruction updates to `.github/copilot-instructions.md`.
3. Apply the same updates to `AGENTS.md` so content stays aligned.
4. Keep the `AGENTS.md` header (`# Agent Operational Guidelines`) and opening source-of-truth note intact.
5. Confirm exactly what changed in each file.

### `evala` — Evaluate Agent Instructions for General/App Separation

When the user says `evala` (or any natural-language equivalent):

1. Read `.github/copilot-instructions.md`, `AGENTS.md`, and any other local agent instruction files.
2. Identify rules that are in the wrong layer:
   - General engineering, security, design, workflow, or deployment-hardening practices sitting in app-specific sections.
   - App names, file paths, cloud resources, exact commands, architecture diagrams, product/domain language, or app-only helper names sitting in reusable general sections.
3. Move generalizable practices into **Part 1 — General Workflow**.
4. Move project-only facts into **Part 2 — App-specific**.
5. Remove duplicates, stale rules, and contradictions while preserving useful project facts.
6. Ensure `.github/copilot-instructions.md` and `AGENTS.md` end in sync after the move.
7. Confirm what moved from app-specific → general, what moved from general → app-specific, what was removed, and that both files were synced.

### Proactively offer to checkpoint when

- A non-trivial decision was just made (architecture, library choice, abandoned approach).
- The user is about to switch tasks or branches.
- A long debugging session just resolved.

---

## IDE Diagnostic False Positives — Known Noise

Before acting on any IDE diagnostic, identify its category.

### Authoritative validators

| Context | Real validator | IDE diagnostics |
|---------|---------------|-----------------|
| Python | `python3 -m py_compile file.py` | Mostly trustworthy, except Flask note below |
| JS inside `.html` | `node --check extracted-js.js` | **High noise — do not chase** |

### False positive categories (do NOT fix these)

| Category | IDE message | Why it's false |
|----------|-------------|----------------|
| **JS template literals** | `Unused constant x` / `Expression expected` / `Closing '}' expected` | Variables used inside `${x}` are invisible to the HTML parser |
| **Flask route returns** | `Expected type 'Response', got 'tuple[Response, int]'` | `(jsonify(...), 400)` IS correct Flask — JetBrains can't infer the union type |
| **SVG self-closing tags** | `Empty tag doesn't work in some browsers` | `<path/>`, `<circle/>`, `<rect/>` are valid HTML5/SVG |
| **onclick-wired params** | `Unused parameter x` | Functions called by HTML `onclick` — IDE can't see the caller |
| **Missing label** | `Missing associated label` | Hidden inputs and internal state fields don't need visible labels |
| **throw in try/catch** | `'throw' of exception caught locally` | Intentional re-throw pattern for error propagation |

**Key rule:** `node --check` passing clean means JS is correct. IDE template errors in `.html`
files are noise from the HTML parser misreading JS — ignore them.

---

## Shell Command Safety - CRITICAL

### Never Output Jinja2 Braces Through the Terminal

The zsh shell interprets `{{ }}` as glob patterns. Commands that output Jinja2 content will hang or produce empty output.

```bash
# BAD - causes empty output or hangs
cat file_with_jinja.yml
grep "pattern" file_with_jinja.yml

# GOOD - use the read_file / grep_search tools instead (they bypass the shell)
# GOOD - if terminal is required, use Python:
python3 -c "print(open('file.yml').read()[:500])"
```

### Never Use Unquoted Heredocs with Dynamic Content

```bash
# BAD - shell interprets {{ }} and $vars, causes heredoc> hang
cat > file.yml << EOF
name: "{{ app_name }}"
EOF

# GOOD - single-quote the delimiter
cat > file.yml << 'EOF'
name: "{{ app_name }}"
EOF

# BEST - use Python or the insert_edit_into_file tool to write files
```

### Prefer Non-Terminal Tools

| Task | Use This | Not This |
|------|----------|----------|
| Read a file | `read_file` tool | `cat` / `head` / `tail` in terminal |
| Search in file | `grep_search` tool | `grep` in terminal |
| Write / edit a file | `insert_edit_into_file` or `replace_string_in_file` tool | `cat > file << EOF` in terminal |
| Verify edits applied | `read_file` tool | `cat file` in terminal |

### If Terminal Hangs (no output, or dquote> / heredoc> / quote>)

1. **Do NOT keep waiting** - it will not recover
2. **Run a new terminal command** - the tool starts a fresh session
3. **Switch to a non-terminal tool** to accomplish the task

### Ansible Playbooks

- Run with `isBackground: true` and retrieve output with `get_terminal_output` for long-running playbooks
- Pipe short playbook runs through `2>&1` to capture all output

---

## Git Branching Rules

**Default: do not create feature branches.** Commit directly to whatever branch
the user is currently on (typically `main`). The user controls branching
strategy — only create a branch when the user explicitly asks for one.

If you genuinely believe a branch is warranted (large refactor, risky
multi-step change), **ask before creating it** — do not create one preemptively.

---

## Git Commit Rules

```bash
# ALWAYS - simple messages, no internal quotes
git commit -m "docs: add deployment guide"
git commit -m "fix: correct IAM role permissions"

# NEVER - nested quotes cause dquote> hangs
git commit -m "docs: add 'comprehensive' guide"

# FOR COMPLEX MESSAGES - use file method
cat > /tmp/msg.txt << 'EOF'
feat: multi-line commit message

- Detail one
- Detail two
EOF
git commit -F /tmp/msg.txt && rm /tmp/msg.txt
```

---

## General Python Coding Standards

See `docs/agent-patterns/python-standards.md` for detailed examples.

**Key rules:** never `str(e)` in JSON responses; all imports at module level (except `# Deferred:` cases); initialize before `try`; use Pythonic style (PEP 8/257); prefer named callables over `lambda`; type hints on public functions; format with `black`/`isort`; catch specific exceptions first; no side effects at import; no global mutable state; use context managers (`with`); fail fast/raise early; functions do one thing (≤50 lines); meaningful names (avoid `data`, `temp`, `result`); prefer built-ins/stdlib; prefer comprehensions; pin dependencies; use virtual environments.
- **Meaningful names** — avoid generic names like `data`, `temp`, `result`, `stuff`, `info`; name things by what they represent in the domain.
- **Prefer built-ins and stdlib** — reach for `collections.Counter`, `collections.defaultdict`, `itertools.chain`, `functools` before writing equivalent loops.
- **Prefer comprehensions** — use list/dict/set comprehensions over equivalent `for` loops that build a collection, when the result is readable.
- **Pin dependencies** — lock exact versions in `requirements.txt`; use `pip-audit` to check for CVEs before each deployment.
- **Virtual environments** — always develop inside a `venv`; never install project dependencies into the system Python.

---

## General JavaScript Coding Standards

See `docs/agent-patterns/javascript-standards.md` for detailed examples.

**Key patterns:** modal/pending-state single-owner lifecycle (confirm owns snapshot → execute → cleanup); declare related state variables together; use registry arrays for grouped DOM operations.

---

## General Coding Workflow

- Start from clear requirements; if scope is ambiguous, propose small options before implementing.
- Prefer small, focused edits that preserve existing behavior unless a change is requested.
- Keep naming and structure consistent with the current codebase.
- Highlight risks, assumptions, and missing data explicitly instead of silently guessing.
- Optimize for maintainability: straightforward code paths, minimal side effects, clear data ownership.


---

## Senior Engineering Standards — Senior-Quality Code, Junior-Readable

Write code the next developer can safely modify, even if they are new to the
project. Senior-quality code is simple, explicit, tested, and boring in the best
way.


- **Clarity beats cleverness** — prefer obvious control flow over compressed tricks.
- **Name by domain meaning** — use names that explain what a value represents, not its type (`listing_status`, not `data`).
- **Explain why, not what** — comments should capture decisions, constraints, tradeoffs, and non-obvious edge cases.
- **Keep public APIs predictable** — functions should validate inputs, return consistent shapes, and document side effects.
- **Make errors actionable** — include enough context for logs/debugging without leaking secrets or internals to users.
- **Minimize hidden coupling** — avoid magic globals, implicit file paths, import-time state, and order-dependent behavior.
- **Prefer boring dependencies** — choose stdlib or already-present libraries unless a new dependency clearly pays for itself.
- **Leave the code easier to review** — small diffs, focused functions, no unrelated formatting churn.
- **Teach through structure** — when code has a pattern, extract a helper or registry so junior devs can follow one example.
- **Explain function intent briefly** — each non-trivial function should have 1-3 sentences describing purpose, inputs/outputs, and side effects.
- **Document variable groups, not every variable** — when related state variables work together, add a short block-level note or table describing ownership and lifecycle.

### Quick readability pattern for stateful code

Use this lightweight table style when a function or module has multiple related
state values:

| Group | Owns | Meaning | Updated by |
|---|---|---|---|
| Pending action state | `pending_*` fields | Tracks current user-confirm flow | confirm/cancel handlers |
| Device context | `device`, `folder`, `tsg_id` | Active execution scope for API/SSH | `cd`, `folder`, `tsg` commands |

Keep entries short; this is a navigation aid, not full API documentation.

### Mini example — function intent + grouped state note

```python
# BAD — no intent, unclear state ownership
def run(ctx, args):
    x = None
    y = None
    ...

# GOOD — brief function intent + grouped state context
def run(ctx: ExecutionContext, args: dict) -> None:
    """Execute a folder-scoped action and print a user-facing status line.

    Inputs: execution context and parsed command args.
    Side effects: updates pending action state and writes to console output.
    """
    # Pending action state: owned by confirm/cancel flow in this command path.
    pending_action = None
    pending_target = None
    ...
```

### Definition of done for code changes

- Requirements are satisfied with the smallest maintainable change.
- Edge cases and failure paths are handled intentionally.
- Relevant validators/tests were run, or the reason they cannot run is stated.
- Security checklist is satisfied: input validation, authorization, secrets/logging, dependency risk.
- New or changed behavior is discoverable through names, docstrings, UI copy, or docs.

---

## General Secure Coding Baseline — All Apps

See `docs/agent-patterns/security-checklist.md` for detailed examples.

**Core rules:** threat-model before coding; validate at boundaries; authorize server-side; keep secrets out of code; sanitize logs; avoid dangerous primitives (`eval`, `exec`, shell interpolation); use safe subprocess calls (`shell=False`); use timeouts for I/O; fail closed; prefer least privilege; audit dependencies; handle destructive actions carefully.

---

## Web App Security — General Rules

See `docs/agent-patterns/security-checklist.md` for detailed examples and Flask/Python-specific patterns.

**Quick reference:** never leak internals in errors; never log sensitive material; never hardcode secrets; session cookies must be HttpOnly/Secure/SameSite; TOTP enrollment requires password; validate all input (type, length, range); sanitize file uploads (`secure_filename()`); confine paths (`Path.resolve()` + `is_relative_to()`); emit security headers (CSP, HSTS, X-Frame-Options); rate-limit auth endpoints; audit dependencies before deployment.

---

## Nginx / Reverse Proxy Hardening

Apply these rules whenever deploying a web app behind Nginx (or any reverse proxy).

### Never duplicate security headers

The reverse proxy is the single source of truth for `X-Frame-Options`,
`X-Content-Type-Options`, `Referrer-Policy`, `Content-Security-Policy`, and
`Strict-Transport-Security`. If the app also emits them, browsers receive duplicate
values and CSP/HSTS behavior becomes unpredictable. Pick one layer; emit from the other
layer only in development.

### server_tokens off — every server block

```nginx
# BAD — only on the HTTPS block; HTTP block still leaks nginx/1.24.0 (Ubuntu)
server { listen 80; ... }  # no server_tokens here
server { listen 443 ssl; server_tokens off; ... }

# GOOD — every block that can respond to a request
server { listen 80; server_tokens off; return 301 https://$host$request_uri; }
server { listen 443 ssl; server_tokens off; ... }
```

### Remove the default site

```bash
rm /etc/nginx/sites-enabled/default
```

The default Ubuntu Nginx site answers unmatched `Host` headers and leaks version info.
Remove it during setup — it is safe to remove on any dedicated app host.

### HTTP → HTTPS redirect

Every HTTP request must redirect to HTTPS. The redirect server block needs
`server_tokens off` (see above) and nothing else:

```nginx
server {
    listen 80;
    server_name example.com;
    server_tokens off;
    return 301 https://$host$request_uri;
}
```

### Rate zones

Define Nginx rate zones for at minimum two tiers:

```nginx
# In http { } block
limit_req_zone $binary_remote_addr zone=login:10m rate=5r/m;
limit_req_zone $binary_remote_addr zone=api:10m   rate=60r/m;
```

Apply the tighter `login` zone to `/login`, `/register`, `/reset-password`, and any
MFA verification endpoint. Apply `api` to the general app location.

### Proxy timeout alignment

Set `proxy_read_timeout` and `proxy_send_timeout` to just above the app/Gunicorn
timeout — not several minutes longer. If Gunicorn times out at 120 s, set proxy
timeouts to 125–130 s so failures surface predictably to the client.

### client_max_body_size

Align `client_max_body_size` with the app's `MAX_CONTENT_LENGTH`. If they differ,
Nginx will silently drop oversized bodies before Flask can return a helpful error.

---

<!--
  ╔══════════════════════════════════════════════════════════════════╗
  ║  PART 2 — ARC (project-specific)                                 ║
  ║  Rules, architecture, and patterns specific to this codebase.    ║
  ║  Do not copy to other projects without review.                   ║
  ╚══════════════════════════════════════════════════════════════════╝
-->

## ARC — Assisted Remote Console

**ARC** is an assisted remote console for Palo Alto Networks SCM and PAN-OS environments.
It provides a PAN-OS-style interactive shell that routes supported commands through SCM REST APIs
by default, with optional SSH passthrough for managed devices.

ARC is SCM-only for API integrations. The command vocabulary intentionally mirrors familiar
firewall / network-operations commands, and API mode translates those commands to SCM REST calls
as implementations are added. Device-local execution is handled through SSH only.

---

### ARC Coding Workflow

- Start from clear requirements; if scope is ambiguous, propose small options before implementing.
- Prefer small, focused edits that preserve existing behavior unless a change is requested.
- Keep naming and structure consistent with the current codebase.
- **Always run `python dev/smoke_test.py` after any change to `app/`.** It covers syntax, imports, registry integrity, arg parser, config types, formatter, CLI banner alignment, inline-help alignment, and theme wiring in one pass.
- Highlight risks, assumptions, and missing data explicitly instead of silently guessing.
- Optimize for maintainability: straightforward code paths, minimal side effects, clear data ownership.
- **Write as if the reviewer is a junior engineer learning network operations and firewall workflows.** Keep implementation details concrete, and make control flow easy to map to operator intent.

#### smoke_test.py — maintenance rules

`smoke_test.py` lives at `dev/` and runs automatically in the pre-commit hook.

| Trigger | Required action |
|---------|----------------|
| New command added to a `COMMANDS` dict | No change needed — registry tests auto-discover it |
| New formatter function added | Add a minimal call in **section 6** of `dev/smoke_test.py` |
| CLI banner lines changed (`_print_banner` in `shell.py`) | Update `_BANNER_LINES` in **section 7** of `dev/smoke_test.py` — the test will catch mismatches and print exactly what to change |
| New module added under `app/` | No change needed — syntax and import tests auto-discover it |
| New `SCMConfig` / `ArcConfig` field with invariant | Add a case in **section 5** of `dev/smoke_test.py` |
| New theme key added to `ArcTheme` | Add a display label to `THEME_KEYS` in `app/settings/theme.py`; add to **section 9** if there is an invariant |
| Builtin command added/removed in `_print_shell_builtins` | Update `_BUILTIN_NAMES` in **section 8** of `dev/smoke_test.py` — the test will catch mismatches |

The test is intentionally lightweight — no mocking, no network, no auth. It validates structure and wiring, not API behavior.

---

### Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.11+ |
| Package manager | [uv](https://github.com/astral-sh/uv) |
| CLI framework | Typer |
| Shell REPL | prompt-toolkit |
| Output rendering | Rich |
| HTTP client | httpx (sync) |
| SSH | paramiko |
| Data validation | pydantic |
| Config storage | `~/.arc/config.json` + env vars |

---

### Project Structure

```
arc/
├── README.md                       ← project overview linking to docs/
├── pyproject.toml                  ← uv-managed project config
├── run.py                          ← dev entry point (python run.py)
├── config/
│   └── config.example.json         ← credential template (copy to ~/.arc/config.json)
├── dev/
│   └── smoke_test.py               ← developer smoke suite (run: python dev/smoke_test.py)
├── docs/                           ← user-facing Markdown rendered by ARC help
│   ├── README.md                   ← help overview
│   ├── usage.md                    ← user workflows
│   ├── architecture.md             ← user-readable architecture
│   ├── configuration.md            ← credential/configuration guide
│   ├── commands/                   ← one Markdown file per shell/registered command
│   └── scm-api/                    ← SCM NGFW reference (pulled by `docsupdate`; excluded from cliup bundle)
│       ├── index.md                ← spec + guide index
│       ├── MANIFEST.md             ← base URLs + sources (gateway-map source of truth)
│       ├── specs/                  ← OpenAPI per-domain: <category>.yaml + <category>.md
│       └── guides/                 ← conceptual pan.dev docs (auth, roles, scope, …)
└── app/
    ├── __init__.py                 ← package version
    ├── banner.txt                  ← startup banner (Rich markup; ## lines are comments)
    ├── cli.py                      ← typer app: arc / arc auth / arc scm / arc docs
    ├── cli_theme.json              ← editable CLI colour roles (edited via `configure` + `cli color`)
    ├── config.py                   ← ArcConfig dataclasses + load_config() / save_config()
    ├── docs.py                     ← docs/ Markdown loader for `help <topic>` and browser opener
    ├── shell.py                    ← ArcShell REPL (prompt_toolkit)
    ├── settings/                    ← loaders for the user-editable settings/ directory
    │   ├── theme.py                 ← ArcTheme dataclass + load/save/reset helpers
    │   ├── features.py              ← reads settings/features.json → dict
    │   ├── cli_structure.py         ← loader for settings/cli-structure.yaml
    │   └── command_help.py          ← reads docs/commands/*.md front-matter → per-command description + usage
    ├── api/
    │   └── client.py               ← SCMClient (REST only)
    ├── ssh/
    │   └── manager.py              ← SSHManager (paramiko connection pool)
    ├── commands/
    │   ├── base.py                 ← CommandDef, ExecutionContext, require_scm(), require_device(), translation_pending()
    │   ├── registry.py             ← thin assembler: merges all domain COMMANDS, exposes match_command()
    │   ├── setup.py                ← /config/setup/v1  — devices, snippets, folders
    │   ├── objects.py              ← /config/objects/v1 — addresses, services, tags, EDLs
    │   ├── security.py             ← /config/security/v1 — security-rules, url-categories
    │   ├── network.py              ← /config/network/v1 — interfaces, routing, zones, HA
    │   └── operations.py           ← jobs, commit (SCM); system resources, logs, ping (SSH/--remote only)
    └── utils/
        └── formatter.py            ← rich Table/Panel renderers for all output types
```

#### Command module layout — mirrors SCM URI structure

Each module under `app/commands/` maps to one SCM API domain or operational group:

| Module | SCM URI prefix | Commands |
|--------|---------------|----------|
| `setup.py` | `/config/setup/v1` | devices, snippets, folders |
| `objects.py` | `/config/objects/v1` | addresses, address-groups, services, tags, EDLs |
| `security.py` | `/config/security/v1` | security-rules, url-categories, policy-match test |
| `network.py` | `/config/network/v1` | interfaces, zones, routing, HA |
| `operations.py` | `/config/setup/v1` + live-device | jobs, commit (SCM); system resources, logs, ping (SSH via --remote) |

`base.py` contains only shared types (`CommandDef`, `ExecutionContext`) and utility functions (`require_scm`, `require_device`, `translation_pending`). No handler logic goes in `base.py`.

`registry.py` is a **thin assembler only** — it imports each module's `COMMANDS` dict, merges them, builds `SORTED_COMMANDS` and `CATEGORIES`, and exposes `match_command()`. No handler logic goes in `registry.py`.

**When adding a new SCM endpoint family**, create `app/commands/<domain>.py`, add the base URL constant and `_get_<domain>()` helper to `SCMClient`, and add the module to the merge block in `registry.py`. Nothing else needs to change.

---

### ARC Domain Keywords — For Scoped Agent Work

When an agent needs to work on a specific domain or feature area, use these keywords in your prompt to scope the context efficiently:

| Keyword | Scope | Key Files | Use When |
|---------|-------|-----------|----------|
| `network` | Network config commands | `app/commands/network.py`, `docs/scm-api/specs/network.md` | Adding/fixing interface, zone, routing, or HA commands |
| `security` | Security policy commands | `app/commands/security.py`, `docs/scm-api/specs/security.md` | Working on security-rules, URL categories, profiles |
| `objects` | Address/service objects | `app/commands/objects.py`, `docs/scm-api/specs/objects.md` | Adding address, service, tag, or EDL commands |
| `setup` | Device/folder/snippet mgmt | `app/commands/setup.py`, `docs/scm-api/specs/setup.md` | Device inventory, folder ops, snippet management |
| `operations` | Jobs, commit, live device | `app/commands/operations.py`, `docs/scm-api/specs/operations*.md` | Commit operations, job tracking, live device commands |
| `formatter` | Output rendering | `app/utils/formatter.py` | Adding new table/panel renderers |
| `shell` | REPL, help, completion | `app/shell.py`, `app/settings/theme.py` | Shell UX, prompts, help system, theming |
| `auth` | Authentication/credentials | `app/cli.py` (auth commands), `app/config.py` | Profile management, credential storage |
| `scm-api` | SCM REST integration | `app/api/client.py`, `docs/scm-api/` | Adding new SCM API endpoints |

**Usage pattern:**
- "Add support for BGP peer listing [network]" → Agent reads network.py, network.md spec
- "Fix security policy table rendering [formatter]" → Agent reads formatter.py only
- "Add OAuth refresh [auth]" → Agent reads cli.py auth commands, config.py

**Token savings:** Using a keyword prevents the agent from reading all 5 domain modules + full AGENTS.md when only 1-2 files are relevant.

---

### Token-Efficient Development Patterns

When working on ARC as an agent, follow these patterns to minimize token usage:

#### Read selectively using domain keywords
- Use `[domain]` keywords (network, security, objects, setup, operations) to scope file reads
- Read `docs/scm-api/specs/<domain>.md` for API reference instead of full OpenAPI YAML
- Check `docs/commands/<command>.md` for existing command docs before exploring code

#### Leverage existing infrastructure
- **Command registry pattern:** Add commands by creating entries in domain module's `COMMANDS` dict
- **No dispatcher changes needed:** Registry auto-merges; tab completion auto-picks up new commands  
- **Argument parsing is automatic:** Use `KEYWORD_PARAMS` for named args, positional for the rest
- **Don't reinvent formatters:** Check `formatter.py` for existing table/panel builders before writing new ones

#### Reuse before creating
- Before writing a new SCM API method, check if `app/api/client.py` already has a similar getter
- Before adding a formatter, check if an existing one can be parameterized
- Before writing table construction code, use existing table builder patterns

#### Prefer targeted smoke tests
- Run `python dev/smoke_test.py` after changes — it's fast and covers 86+ checks
- Add a formatter call to section 6 if you added a new renderer
- Add a builtin to `_BUILTIN_NAMES` if you added a shell command
- Don't run full integration tests unless the change affects API calls

#### Minimize doc reading for simple changes
- For typo fixes, argument tweaks, or one-line changes: read only the target file
- For new commands following existing patterns: read one example command in the same domain
- For shell UX changes: read only the relevant section of `app/shell.py` (use line ranges)

---

### Documentation Strategy

Agent instructions (`.github/copilot-instructions.md` and `AGENTS.md`) are **not** the user manual.
They hold design language, architecture constraints, coding patterns, command-registry rules,
and app requirements that agents need while editing code.

User-facing documentation lives in `docs/` as Markdown. ARC reads that folder at runtime through
`app/docs.py` and renders docs inside the CLI with Rich Markdown:

| CLI input | Documentation source |
|-----------|----------------------|
| `help usage` | `docs/usage.md` |
| `help architecture` | `docs/architecture.md` |
| `help configuration` | `docs/configuration.md` |
| `help commands` | `docs/commands/index.md` |
| `help show system info` | `docs/commands/show-system-info.md` |
| `help remote` | `docs/commands/remote.md` |
| `docs` | Opens `docs/README.md` in the default browser |

When adding or changing a user-visible command, update both the command registry and the matching
Markdown doc in `docs/commands/`. Keep docs concise and formatted for terminal rendering.

---

### Execution Modes

ARC routes every command through a two-mode dispatch in `ArcShell._dispatch()`:

| Mode | Trigger | Mechanism |
|------|---------|-----------|
| **API** (default) | Any command without `--remote` | `SCMClient` REST API |
| **SSH** | `--remote`, `remote <device>`, or `connect` | `SSHManager` runs commands on the device |

**SCM API covers all configuration commands** — objects, security policy, network config (interfaces,
zones, routing, HA), jobs, commit, and device inventory. Every config command that ARC exposes runs
against the SCM REST API by default.

**Live operational state** (CPU/memory, traffic logs, live routing table, ping, software check) is
**not stored in SCM**. These commands return a clear message directing the operator to use `--remote`
for SSH execution against the device. Never use "translation pending" language — instead say clearly
that the command requires live device state and show the `--remote` usage.

Device context is set by `cd <device>` and stored in `ShellState.device`. SCM folder context is stored
in `ShellState.folder` and passed as the `?folder=` query parameter on SCM calls.

---

### Command Registry Pattern

eEvery supported command lives in one of the domain modules under `app/commands/`.
Each module exports a `COMMANDS: dict[str, CommandDef]` dict. `registry.py` merges them.

```python
# In app/commands/objects.py (or whichever domain module owns this command)
def _show_bgp_peers(ctx: ExecutionContext, args: dict) -> Any:
    scm = require_scm(ctx)
    return scm.get_bgp_peers(folder=ctx.folder)

COMMANDS: dict[str, CommandDef] = {
    ...
    'show bgp peers': CommandDef(
        description='Show BGP peer summary',
        category='network',
        scope='folder',                      # 'folder' | 'device' | 'global'
        api_handler=_show_bgp_peers,         # Callable(ctx: ExecutionContext, args: dict) -> Any
        ssh_command='show routing protocol bgp peer',  # str or Callable(args: dict) -> str
        render='raw',                         # key into ArcShell._render() dispatch table
    ),
}
```

#### Command scope — declared on every CommandDef

| scope | Meaning | When to use |
|-------|---------|-------------|
| `"folder"` | Scoped to `ctx.folder`. Handler passes `folder=ctx.folder` to SCM. | All config/policy/objects/network commands — anything stored in SCM at the folder or snippet level. Default. |
| `"device"` | Requires active device context (`cd <device>`). ARC blocks execution with a clear error if no device is selected. | Per-device operational info that SCM stores (system info, logs). Live-device commands that need `--remote`. |
| `"global"` | No context filtering. Returns TSG-wide data regardless of folder or device. | `show devices`, `show jobs all/id`, `show snippet`, `show snippets global`, `show device snippets` (takes name arg), `commit`. |

**Scope assignment rules:**
- Network config (interfaces, zones, routing, HA) → `"folder"` — these are stored in SCM at folder/snippet level
- SCM inventory + jobs + commit → `"global"` — TSG-wide, no folder/device required
- Live operational state (resources, logs, ping, software check) → `"device"` — need a device context for `--remote` targeting
- Do NOT assign `"device"` scope to network config commands; they are configuration, not live device state

**Rules for adding commands:**

- Handler function must be a private module-level `def _handler_name(ctx, args)` in the correct domain module — never an inline lambda, never in `registry.py` or `base.py`.
- Import `require_scm` and `require_device` from `app.commands.base`. Import `translation_pending` only if genuinely needed (it exists for legacy SSH-only stubs).
- Every new `CommandDef` **must** declare `scope=` explicitly — do not rely on the default.
- `ssh_command` must be a named function or a plain string — **never an inline lambda**.
- `api_handler` receives `ExecutionContext` (`.scm`, `.ssh`, `.device`, `.folder`, `.target`, `.device_host`) and an `args` dict parsed from the remainder tokens after the matched command prefix.
- `ssh_command` is a plain string for static commands, or a `Callable(args) -> str` for commands that embed dynamic arguments (e.g. `ping host <ip>`).
- `render` is a string key into the dispatch table in `ArcShell._render()`. Add a renderer in `formatter.py` for new output types.
- After adding an entry to a domain module's `COMMANDS`, tab completion picks it up automatically.

**Adding a command — checklist:**

1. Identify or create the right domain module (`setup.py`, `objects.py`, `security.py`, `network.py`, `operations.py`).
2. Write `_handler(ctx, args)` in that module.
3. Add `CommandDef` entry with explicit `scope=` to that module's `COMMANDS` dict.
4. Add or update `docs/commands/<command-slug>.md` so `help <command>` works.
5. Add renderer in `formatter.py` if needed; add dispatch case in `ArcShell._render()`.
6. Run `python smoke_test.py` — registry tests auto-pick up the new command; add a formatter call to section 6 if a new renderer was added.
7. Smoke-test interactively: `printf 'help your new command\nyour new command\nexit\n' | arc`.

---

### Config Pattern

`ArcConfig` is a dataclass read once at startup in `cli.main()`:

```python
from app.config import load_config
cfg = load_config()   # env vars override ~/.arc/config.json values
```

Config hierarchy (later overrides earlier): `~/.arc/config.json` → environment variables.

SCM auth supports either `SCM_BEARER_TOKEN` or OAuth client credentials
(`SCM_CLIENT_ID`, `SCM_CLIENT_SECRET`, `SCM_TSG_ID`). Bearer token takes precedence.

Never read config inside the registry or formatter. Pass `ArcConfig` through `ExecutionContext`
if a handler needs it.

---

### Client Initialization

Clients are built once in `ArcShell.__init__()` and stored as instance attributes:

- `self._scm` — `SCMClient` or `None`
- `self._ssh` — `SSHManager` (always present; connections are deferred per device)

SCM is not required to start the shell. ARC only fails when an API command requires SCM and no SCM
credentials are configured. SSH commands can still run when SSH credentials/device reachability exist.

---

### Shell Built-in Commands

Handled directly in `ArcShell._dispatch()` before the registry is consulted:

| Command | Behavior |
|---------|----------|
| `cd <device>` | Change Device in SCM — fuzzy-matches hostname / serial / IP. **Tab** after `cd ` lists all managed devices. |
| `remote <device>` | SSH to Device — opens an interactive SSH session on the named device (also sets device context). **Tab** after `remote ` lists all managed devices. |
| `connect` | SSH to Device — opens an interactive SSH session on the current `cd` device. |
| `exit` | Exit ARC — closes all connections and quits. |
| `ls` / `devices` | List managed devices under the current folder and refresh the device cache. |
| `pwd` | Print current device, SSH credential status, and active SCM folder. |
| `folder <name>` | Set `ShellState.folder` (used by all SCM API calls). **Tab** after `folder ` lists available SCM folders. |
| `configure` | Enter configure mode. Prompt changes to `#` (for example `arc:global #`). |
| `cli` | Configure-mode CLI theme operations. `cli show`, `cli color <key> <style>`, `cli reset`. |
| `?` / `help` | Print the full command reference. |
| `help <topic>` | Render Markdown from `docs/` inside the CLI. |
| `docs` | Open `docs/README.md` in the default browser. |
| `clear` | Clear the terminal. |
| `--remote` | Not listed as a shell command. It appears only as a completion suffix while typing a registered command and runs that one command remotely. |

---

### CLI Theme System

ARC's colour roles are stored in `app/cli_theme.json` and loaded at shell startup into `ArcTheme` (defined in `app/settings/theme.py`). Every colour value is a Rich markup style string (e.g. `"cyan"`, `"bold yellow"`, `"dim"`).

**Theme keys:**

| Key | Default | Controls |
|-----|---------|----------|
| `command_name` | `cyan` | Command names in `?` help output |
| `section_header` | `bold yellow` | Section headers (GLOBAL / FOLDER / DEVICE / SHELL) |
| `section_header_locked` | `dim bold` | DEVICE section header when no device is active |
| `description` | *(empty — plain)* | Description text beside commands |
| `description_dim` | `dim` | Dim/secondary text and context annotations |
| `banner_logo` | `bold cyan` | Default style tag written into `app/banner.txt` |
| `banner_subtitle` | `dim` | Default style tag for subtitle line in `app/banner.txt` |

**Editing colours:**
- **In-shell:** `configure` then `cli color <key> <style>` — saved immediately to `app/cli_theme.json`
- **Direct file edit:** open `app/cli_theme.json` and change any value
- **Reset:** `configure` then `cli reset` — restores all keys to defaults

**`app/banner.txt`** is the single source of truth for the startup banner. It contains Rich markup tags directly (e.g. `[bold cyan]...[/bold cyan]`). Lines starting with `##` are comments stripped before printing. Add a blank line for spacing, a legal notice, or change the logo colour — all without touching Python code.

**Rules for adding a new theme key:**
1. Add the field to `ArcTheme` in `app/settings/theme.py` with a default value.
2. Add a display label to `THEME_KEYS` in `app/settings/theme.py`.
3. Use `self._styled(text, self._theme.<key>)` wherever the colour is applied in `shell.py`.
4. Add a case in **section 9** of `dev/smoke_test.py` if there is an invariant to check.
5. Run `python dev/smoke_test.py` to verify.

---

### Shell UX Design — Key Principles

These are the canonical interaction patterns for ARC. All future shell features must follow these rules.

#### Two-mode help system — Cisco-style inline vs full docs

ARC has two distinct help modes:

| Trigger | Mode | Behavior |
|---------|------|----------|
| `?` (bare) | Cisco inline | Compact 3-tier listing — one line per command, no panels |
| `show ?` | Cisco inline | All `show *` commands with one-liner descriptions |
| `help` (bare) | Cisco inline | Same as bare `?` |
| `cd help` | Full docs | Renders `docs/commands/cd.md` for the command before `help` |
| `show address help` | Full docs | Renders docs page for `show address` |
| `help <topic>` | Full docs | Renders docs by topic name |
| `help all` | Full dump | Unfiltered complete reference |

**`?` is always the quick inline reference — never show elaborate panels for bare `?`.**

**Strict context-aware rule:** `?` must only list commands that are executable in the current context and mode.
Do not show unavailable/locked commands in the inline list.

**Progressive collapse rule:** prefix help must show only the next valid token(s), not a full dump of matching command strings.
Examples: `show jobs ?` -> `all`, `id`; `show device ?` -> `<enter>`, `snippets`, `devices`.
This applies to bare tiered `?` too: each tier should show top-level next tokens (for example `show`, `commit`) rather than full leaf command lines.

The inline `?` output is organized in three tiers with plain section headers:

| Tier | Label | Commands shown |
|------|-------|----------------|
| **Tier 1 — GLOBAL** | `GLOBAL` | All `scope="global"` commands |
| **Tier 2 — FOLDER** | `FOLDER [<name>]` | All `scope="folder"` commands with active folder annotation |
| **Tier 3 — DEVICE** | `DEVICE [<name>]` bright / `DEVICE [locked]` dim | All `scope="device"` commands |
| **SHELL** | `SHELL` | Built-in navigation commands |

Footer line always shown: `<command> help  → docs  |  help all → full reference`

`help all` bypasses tiers and shows the full unfiltered reference.

Availability examples:
- `scope="device"` commands appear only when a device is selected
- `commit` appears only in configure mode
- `folder create <name>` and `cli ...` appear only in configure mode
- In configure mode, bare `?` shows configure workflow commands plus read-only `show ...` navigation stems
- In configure mode, bare `?` shows only configure-relevant commands (for ARC this means configure workflow commands, not full read-only operational listings)

#### Prompt reflects context tier

The prompt uses four forms that tell the operator exactly which tier they are operating in:

| Context state | Prompt | Notes |
|---|---|---|
| No device, Shared folder | `arc:global >` | Root / global tier — dim cyan label |
| No device, named folder | `arc:Production >` | Folder tier — green folder name |
| Device set, Shared folder | `arc:fw01:device >` | Device tier at Shared — yellow device + dim cyan label |
| Device set, named folder | `arc:fw01:Production >` | Device + specific folder — yellow device + green folder |

**Rule:** Never show `:Shared` in the prompt. Shared is the default/unset state — replace it with
the context tier label (`:global` or `:device`). Only show a folder name when it is a meaningful
non-Shared folder that the operator explicitly navigated to.

#### Everything is context-aware by default

**This is the primary design rule.** No command, built-in, or navigation gesture should silently accept invalid context or produce results from the wrong scope.

| Context constraint | Enforcement |
|---|---|
| `cd <device>` when cache populated | Hard error if device not in TSG device list — never create a stub |
| `folder <name>` when cache populated | Hard error if folder not in TSG folder list |
| `tsg <id>` switch | Always clears device + folder context; refreshes all caches; warns if new TSG has 0 devices |
| `remote <device>` / `connect <device>` | Same as `cd` — refuses unknown device when cache populated |
| Commands with `scope="device"` | `_execute_api` blocks execution and shows actionable error before calling handler |
| Commands with `scope="folder"` | Handler uses `ctx.folder`; always scoped to the active folder |
| Commands with `scope="global"` | Handler ignores `ctx.folder`/`ctx.device`; returns TSG-wide data |

**Explicitly global commands** (declared `scope="global"`): `show devices`, `show device`, `show device snippets`, `show snippet <name>`, `show snippets global`, `show jobs all`, `show jobs id`, `commit`, `exit`, `pwd`, `tsg`, `help`, `?`, `docs`, `clear`.

**Exception — empty cache:** When the SCM API is unavailable and the device/folder cache is empty, fall back gracefully (allow SSH stub for `cd`, allow free-form folder name). Document this in the fallback message so the operator knows why the constraint is relaxed.

When adding any new built-in or registered command, explicitly decide its scope and enforce it. Do not add a command and leave scope as an afterthought.

#### Configure mode owns all write/change operations

ARC uses a Cisco-style configure mode for mutating operations.

| Rule | Enforcement |
|---|---|
| Enter configure mode | `configure` switches prompt to `#` (`conf` resolves to `configure` via shorthand expansion) |
| Write operations outside configure mode | Must be blocked with a clear message |
| `folder create <name>` | Allowed only in configure mode |
| `commit` | Allowed only in configure mode |
| CLI theme writes (`cli color`, `cli reset`) | Allowed only in configure mode |

Use `exit` to leave configure mode and return to the normal prompt.

#### Tab completion is context-aware

| User types | Tab shows |
|-----------|-----------|
| `cd ` | All managed device names (from SCM cache) |
| `remote ` | All managed device names |
| `connect ` | All managed device names (supported shortcut; canonical help shows `connect`) |
| `folder ` | All SCM folder names |
| `help ` | Docs topics and registered command names |
| `show sy` | All matching ARC command prefixes |
| `show system info --` | `--remote` suffix for running that single command remotely |

Device and folder caches are populated at startup when SCM is configured. Both caches refresh on `ls` / `devices`.

#### Unambiguous shorthand (Cisco-style)

ARC accepts token-prefix shorthand when (and only when) the prefix resolves to exactly one command.

| User input | Result |
|-----------|--------|
| `e` | Runs `exit` (unique match) |
| `q` | Runs `quit` (unique match) |
| `sh sec pol` | Runs `show security policy` |
| `d` | **No expansion** (ambiguous: `docs` vs `devices`) |

Rules:
- Expansion applies to shell built-ins and registered command keys.
- Matching is token-wise prefix (`sh sec pol` → `show security policy`).
- Ambiguous prefixes are never auto-expanded.
- Tab completion remains available; shorthand-on-Enter is an additional convenience.

#### Interactive SSH model

`connect` and `remote <device>` open a true interactive PTY session. ARC authenticates
using stored credentials (keychain + 2FA), then hands the terminal directly to the device.

You are ON the device — every keystroke goes to it; every byte from the device is written
to your terminal. ARC is a transparent byte pipe; no interception, no logging, no command
dispatch. The session ends when you type `exit` on the device; the ARC prompt reappears
automatically.

Authentication order:
1. SSH agent keys
2. Configured key file (`arc auth login --ssh-key`)
3. Default key files (`~/.ssh/id_ed25519`, `id_rsa`, `id_ecdsa`)
4. Keyboard-interactive (auto-fills stored password from keychain, surfaces 2FA prompts)
5. Plain password fallback

#### `?` is the canonical help trigger

`?` and `help` are identical for the short command reference. `help <topic>` opens full docs from `docs/`.

#### `pwd` always shows credential status

`pwd` shows device name, serial, IP, and active SCM folder. SSH credential status is shown
at connection time, not in `pwd`.

#### `cd` never starts an SSH session

`cd` only changes the SCM/API device context. To open an interactive SSH session, use `connect`
for the current device or `remote <device>` for a named device. Do not list `cd ..` / `cd /` in
help output; they may remain accepted as quiet convenience aliases.

#### Folder context applies to all SCM calls

The active folder (`ShellState.folder`, default `Shared`) is passed as the `?folder=` query parameter
on every SCM REST call. Change it with `folder <name>` + Tab.

---

### SCM REST API — Gateway Map

**Source of truth for all SCM API information: https://pan.dev/scm/api/**

Never guess or invent SCM API paths, parameters, or base URLs.  Always look up
the correct endpoint in the pan.dev OpenAPI specs before implementing or
changing any API call.  The pan.dev GitHub source for all specs is:
  `https://github.com/PaloAltoNetworks/pan.dev/tree/master/openapi-specs/scm/`

**Local reference set:** ARC ships a mirror of the SCM NGFW docs under
`docs/scm-api/` — `specs/<category>.yaml` (raw OpenAPI) + `specs/<category>.md`
(consolidated endpoint listing), `guides/*.md` (conceptual pan.dev docs:
getting started, access tokens, service accounts, roles, scope, platform
configuration), plus `index.md` and a `MANIFEST.md` that records each spec's
`servers[0].url` base URL and pull date.  Refresh it with the `docsupdate`
trigger (`python dev/docsupdate.py`).  `MANIFEST.md` is the source of
truth this gateway-map table mirrors — if they disagree, re-run `docsupdate`
and update this table from the manifest.  This reference set is excluded from
the `arc cliup` browser bundle (it is developer/agent material, not user help).

SCM gateways come from the `servers[0].url` field in each OpenAPI spec.  The
same OAuth bearer token works on all of them.  Confirmed base URLs (from the
last `docsupdate` pull):

| Category | Base URL (`servers[0].url`) | pan.dev spec |
|----------|----------|--------------|
| **Objects** (addresses, address-groups, services, tags, EDLs, …) | `https://api.strata.paloaltonetworks.com/config/objects/v1` | `openapi-specs/scm/config/ngfw/objects/objects_v1.3_feb.yaml` |
| **Security** (security-rules, url-categories, decryption, profiles, …) | `https://api.strata.paloaltonetworks.com/config/security/v1` | `openapi-specs/scm/config/ngfw/security/security-services-R2-2026.yaml` |
| **Setup** (devices, folders, snippets, labels, jobs, commit/push, …) | `https://api.strata.paloaltonetworks.com/config/setup/v1` | `openapi-specs/scm/config/ngfw/setup/config-setup-feb-v1.yaml` |
| **Network** (interfaces, zones, routing, HA, …) | `https://api.strata.paloaltonetworks.com/config/network/v1` | `openapi-specs/scm/config/ngfw/network/network-services-R2-2026.yaml` |
| **Operations** (config jobs, push) | `https://api.strata.paloaltonetworks.com/config/operations/v1` | `openapi-specs/scm/config/ngfw/operations/config-operations-march.yaml` |
| **Operations (R2)** (live operational ops) | `https://api.strata.paloaltonetworks.com/operations/v1` | `openapi-specs/scm/config/ngfw-operations/operations-R2-2026.yaml` |
| **Device settings** | `https://api.strata.paloaltonetworks.com/config/device/v1` | `openapi-specs/scm/config/ngfw/device/device-settings_April.yaml` |
| **Identity** | `https://api.strata.paloaltonetworks.com/config/identity/v1` | `openapi-specs/scm/config/ngfw/identity/identity-services-march.yaml` |
| **Device onboarding** | `https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1` | `openapi-specs/scm/config/ngfw/setup/device-onboarding/device-onboarding-updated.yaml` |
| **IAM** (service accounts, access policies, roles) | `https://api.sase.paloaltonetworks.com` | `openapi-specs/scm/iam/ServiceAccounts.yaml` |
| **Tenancy** (TSGs, tenant hierarchy) | `https://api.sase.paloaltonetworks.com` | `openapi-specs/scm/tenancy/TenantServiceGroup.yaml` |
| **Authentication** (OAuth token endpoint) | `https://auth.apps.paloaltonetworks.com` | `openapi-specs/scm/auth/AuthService.yaml` |

Key paths (always verify current spec before using):

```
# Authentication
POST https://auth.apps.paloaltonetworks.com/auth/v1/oauth2/access_token
  body: grant_type=client_credentials&scope=tsg_id:<TSG_ID>
  auth: HTTP Basic (client_id:client_secret)

# Objects
GET  https://api.strata.paloaltonetworks.com/config/objects/v1/addresses?folder=Shared
GET  https://api.strata.paloaltonetworks.com/config/objects/v1/address-groups?folder=Shared
GET  https://api.strata.paloaltonetworks.com/config/objects/v1/services?folder=Shared
GET  https://api.strata.paloaltonetworks.com/config/objects/v1/tags?folder=Shared

# Security
GET  https://api.strata.paloaltonetworks.com/config/security/v1/security-rules?folder=Shared&position=pre
GET  https://api.strata.paloaltonetworks.com/config/security/v1/url-categories?folder=Shared

# Setup (devices, folders — no folder param needed for devices)
GET  https://api.strata.paloaltonetworks.com/config/setup/v1/devices
GET  https://api.strata.paloaltonetworks.com/config/setup/v1/folders
GET  https://api.strata.paloaltonetworks.com/config/setup/v1/jobs
GET  https://api.strata.paloaltonetworks.com/config/setup/v1/jobs/{id}
POST https://api.strata.paloaltonetworks.com/config/setup/v1/config-versions/candidate:push

# Network config (verify exact paths at pan.dev/scm/api/)
GET  https://api.strata.paloaltonetworks.com/config/network/v1/ethernet?folder=Shared
GET  https://api.strata.paloaltonetworks.com/config/network/v1/aggregate-ethernet?folder=Shared
GET  https://api.strata.paloaltonetworks.com/config/network/v1/loopback-interfaces?folder=Shared
GET  https://api.strata.paloaltonetworks.com/config/network/v1/zones?folder=Shared
GET  https://api.strata.paloaltonetworks.com/config/network/v1/routing/static-routes?folder=Shared
GET  https://api.strata.paloaltonetworks.com/config/network/v1/virtual-routers?folder=Shared
GET  https://api.strata.paloaltonetworks.com/config/network/v1/ha?folder=Shared

# Tenancy — list child TSGs
GET  https://api.sase.paloaltonetworks.com/tenancy/v1/tenant_service_groups/{tsg_id}/operations/list_children
GET  https://api.sase.paloaltonetworks.com/tenancy/v1/tenant_service_groups
```

**Token scope:** Every OAuth token is scoped to a specific TSG (`scope=tsg_id:<id>`).
Tokens scoped to a parent TSG can read data across child TSGs.
Use `arc auth test` to verify which endpoints are accessible with the current credentials.

---

### `docsupdate` — Refresh the SCM API Reference from pan.dev

When the user says `docsupdate` (or `update docs` / `pull api docs`):

1. Run `python dev/docsupdate.py`. It downloads the current NGFW OpenAPI
   specs (objects, security, setup, network, operations, device, identity,
   device-onboarding) plus auth, tenancy, and IAM service-accounts, and the
   conceptual SCM guide docs (getting started, access tokens, service accounts,
   roles, scope, platform configuration, release notes) directly from the
   pan.dev GitHub repo (`PaloAltoNetworks/pan.dev`, master).
2. The script writes, under `docs/scm-api/`: `specs/<category>.yaml` +
   `specs/<category>.md`, `guides/*.md`, `index.md`, and `MANIFEST.md`.
   `docs/scm-api/` is excluded from the `arc cliup` browser bundle.
3. Markdown/manifest generation needs PyYAML (a dev extra). If it is missing,
   the script still saves raw specs + guides and prints the install hint
   (`uv pip install -e '.[dev]'`).
4. After a successful pull, compare `docs/scm-api/MANIFEST.md` against the
   **SCM REST API — Gateway Map** table above. If a base URL or spec filename
   changed, update that table (and `app/api/client.py` URL constants if a
   gateway moved). Confirm to the user which specs changed.

Helper flags: `python dev/docsupdate.py --list-remote` prints the live
spec tree on pan.dev; `--check` reports drift without writing files. When
pan.dev renames a dated spec file, update the matching entry in the `SPECS`
dict at the top of `dev/docsupdate.py`.

---

### Environment Variables

| Variable | Description |
|----------|-------------|
| `SCM_BEARER_TOKEN` | Pre-issued SCM bearer token |
| `SCM_CLIENT_ID` | SCM OAuth client ID |
| `SCM_CLIENT_SECRET` | SCM OAuth client secret |
| `SCM_TSG_ID` | Tenant Services Group ID |
| `ARC_SSH_USER` | Default SSH username (default: `admin`) |
| `ARC_SSH_KEY` | Path to SSH private key |
| `ARC_SSH_PASS` | SSH password when not using key auth |
| `ARC_DEBUG` | Set to `1` for verbose tracebacks on errors |

---

### Security Notes for ARC

- Secrets (`SCM_BEARER_TOKEN`, `SCM_CLIENT_SECRET`, `ARC_SSH_PASS`, and config equivalents) are stored only in the OS keychain or supplied as temporary environment variables. ARC must never write secrets to `config.json`.
- `~/.arc/config.json` / platform config path stores non-sensitive values only (`client_id`, `tsg_id`, SSH user/key path/port, default folder) and must be written with owner-only permissions (`0700` directory, `0600` file where supported).
- If keychain storage fails, fail closed: save only non-sensitive config, do not persist secrets to disk, and tell the user to use keychain access or temporary environment variables.
- `arc auth login` must use non-echoing prompts for secrets (`getpass` / hidden input). Never collect tokens, client secrets, or SSH passwords with plain `input()`.
- Avoid documenting long-lived secrets in shell profiles (`~/.zshrc`, `~/.bashrc`, PowerShell profile). Environment variables are for temporary sessions, CI, or secret-manager wrappers only.
- The `_mask()` helper in `cli.auth_show` ensures credentials are never printed in clear.
- `ARC_DEBUG=1` prints full stack traces — do not enable in shared terminal sessions.
- SSH `AutoAddPolicy` is used for managed devices; acceptable in controlled network-ops environments but means host keys are not verified. Document this when deploying.
