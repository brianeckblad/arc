# ARC Settings — User-Editable Files

Everything in this folder customizes ARC **without touching code**.
Edit a file, save, restart ARC. That's it.

| File | What it controls | How to edit |
|------|------------------|-------------|
| `features.json` | Which commands are turned **on/off** | Set a flag to `true` or `false` |
| `banner.txt` | The startup logo / banner | Plain text + Rich colour tags like `[bold cyan]…[/bold cyan]` |
| `goodbye.txt` | Random exit messages (one per line) | Add/remove lines |
| `theme.json` | Colours used in `?` help and prompts | Rich style strings: `"cyan"`, `"bold yellow"`, `"dim"` |
| `cli-structure.yaml` | Verb descriptions, section headers, help footer, configure banner | YAML key/values |
| `command-structure.json` | The **order** of fields for a command (`{"address": ["name", "type", ...]}`) | Add/move field names in the array to reorder |

> **Command help text** (the one-liner + usage shown by `?` and the full
> `help <command>` page) is **not** here — it lives in each command's own
> `docs/commands/<command>.md` file. See "Command help" below.

---

## features.json — turn features on/off

This is the most important file. Each entry is a **feature flag** with one of
three states:

```json
{
  "show_address": true,       // ON  — visible and runnable for everyone
  "nat_rules":    "dev",      // DEV — under development; hidden until dev mode
  "delete_objects": false      // OFF — hidden and blocked for everyone
}
```

- `true`  → the command(s) the flag gates appear in `?` help and run.
- `"dev"` → hidden for normal users, **revealed only in development mode**
  (see below). Use this for commands you are still building/testing.
- `false` → those commands are hidden and blocked for everyone.
- A flag **missing** from this file defaults to **off** (safe).

Keys starting with `_` (like `_README`, `_section_*`) are comments — ignored.

### Development mode — test work-in-progress commands

`"dev"` commands stay invisible to normal users so they are never confused by
half-finished features. To reveal them, type the hidden **`dev`** command:

```
dev            toggle development mode on/off  (prompt shows arc:global:dev >)
dev on         force it on
dev off        force it off
```

This supports a CI/CD lifecycle: ship a command as `"dev"`, test it in
development mode, then flip its flag to `true` here when it is ready for
everyone. For automation, start ARC with the environment variable
`ARC_DEV_MODE=1` to enter development mode immediately.

**Inside ARC** you can also change a single flag for one session (not saved):

```
feature show                 list every flag grouped ON / DEV / OFF
feature enable show_zone     set one ON for this session
feature disable show_zone    set one OFF for this session
feature dev show_zone        mark one DEV for this session
```

To make a change permanent, edit `features.json` here and restart.

---

## commands help — reword descriptions & usage (in the docs)

Every command's help lives in **one** file: `docs/commands/<command>.md`. The top
of that file is a small YAML *front-matter* block that the `?` help reads; the
Markdown below it is the full `help <command>` page:

```markdown
---
command: packet-tracer
description: Trace a packet through the folder's security rule base
usage: packet-tracer from <zone> to <zone> source <ip> destination <ip>
---
# packet-tracer
...the full help page (examples, output, API)...
```

- `description` → the one-liner shown in `?`.
- `usage` → the syntax line shown by `<command> ?`.
- The body → the full `help <command>` page.

Edit that one file, save, restart ARC — the quick `?` help **and** the full
`help` page both update. This is the single source of truth: no second file to
keep in sync.

If you add a brand-new command in code, generate its doc (and refresh the index
+ API reference) with:

```
python dev/generate_command_docs.py
```

This also runs automatically whenever you pull new API specs with `docsupdate`.

---

## command-structure.json — argument order

This file controls **only one thing: the order of fields** for each
`set <object>` command. One JSON entry per command — the object is the key,
and the value is an array of field names in the order you type them:

```json
{
  "_comment": [
    "Instructions..."
  ],
  "address": ["name", "type", "value", "description", "tag"]
}
```

- **Reorder** a command by moving field names in the array. That is all you edit.
- Everything else — which field is a fixed choice (and what the choices are),
  which are required, the Tab/`?` hints — is **not** in this file. It comes from
  the API-derived field library in the code, so you never have to maintain it.
- **You do not need quotes** around values with spaces — ARC works out where each
  field ends (e.g. `set address my web host fqdn example.com`). Quotes still work
  for the rare value that contains a reserved word.
- A command with no entry here falls back to the `usage:` line in its
  `docs/commands/<command>.md`.
- Keys starting with `_` are treated as comments and ignored by the parser.

---

## Where secrets live (NOT here)

Credentials (API tokens, SSH passwords) are **never** stored in this folder.
They live in the OS keychain + `config/<your-username>/config.json`.
Run `arc auth configure` to set them.

