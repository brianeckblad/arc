# feature — Feature Flags

ARC commands are turned on/off by **feature flags** stored in
**`settings/features/`**.  The file is generated from the pulled OpenAPI
specs plus explicit ARC commands, then edited by operators to enable the pieces
they want.  New generated flags default to `false` so API surface fails closed
until intentionally enabled.

Every flag has **three states**: `true` (on for everyone), `"dev"` (under
development — hidden until development mode is on), and `false` (off for
everyone).

## Usage (inside ARC)

```text
feature show                 List every flag grouped ON / DEV / OFF / HIDDEN (human names)
feature show on|off|dev|hidden   List only flags in one state
feature show <name>          List flags/commands matching a name fragment
show feature on              Alias for feature show on
show feature <name>          Alias for feature show <name>
feature gui                  Open the browser feature editor (see below)
feature area                 List areas + which are enabled/disabled
feature area <name> enable|disable   Turn a whole area on/off (name or key)
feature info <flag>          Describe a flag (human name + area) + its gated commands
feature <flag> ?             Same as feature info <flag>
feature enable <flag>        Set one ON and save to settings/features/
feature disable <flag>       Set one OFF and save to settings/features/
feature dev <flag>           Mark one DEV and save to settings/features/
feature hidden <flag>        Mark one HIDDEN (runs, not shown in normal ?)
feature scope <cmd> <global|folder|device|reset>
                             Override where a command may run (reset = code default)
feature default <domain> <on|dev|off>
                             Set a domain file's default state for unlisted commands
feature carry <domain> <on|off>
                             Keep manual edits when the domain file is regenerated
feature ?                    Show the sub-command summary
feature enable ?             List flags not yet ON
feature disable ?            List flags not yet OFF
feature help                 Show this page

alias                        List personal aliases  (alias <name> <expansion> to add)
dev                          Toggle development mode (reveal DEV commands)
```

## Browser editor — `feature gui`

`feature gui` starts a small local web server (127.0.0.1, port from
`features_gui.port` in config.json — default **4445**), opens your browser, and
**waits** while you edit. Click **Done** in the page (or press **Ctrl-C** in the
shell) to close it and return to the prompt. Nothing runs after you close it.

The editor uses one consistent layout everywhere — a top tab bar of **sections**,
a left sidebar of **groups** for that section, and a main pane of the selected
group's items. Click a section tab, pick a group on the left, edit on the right.
The browser back/forward buttons and refresh work (the URL updates to
`#section/group`).

The six sections:

- **Areas** — enable or disable whole capability areas. Disabling an area is a
  real off switch (see "Areas" below). This is the one place a disabled area
  still appears, so you can turn it back on.
- **Features** — the left sidebar lists **areas** (Advanced DNS Security, Cloud
  NGFW, …) by real name; pick one to see only that area's features. Each shows a
  plain-English name (technical flag id secondary). Toggle **ON / DEV / OFF /
  HIDDEN**, expand to set the **run scope per command**, and click **?** for
  details. A bar at the top carries **Enable all** and **Disable area**.
  (Disabled areas don't appear here — manage them in the Areas tab.)
- **Command Structure** — left sidebar lists the same **areas**; pick one to see
  its `set`/`update`/`delete` commands. Expand a command to reorder fields and
  edit each field's type, required flag, hint, and choices. Saving locks the
  entry so regeneration won't overwrite it.
- **Aliases** — left sidebar has **System (shared)** and **My aliases**; add /
  edit / delete shortcuts in each.
- **Built-ins** — left sidebar groups the shell's own commands (Navigation,
  Configure & Write, Info & Help, …). Set each one's visibility
  (**Shown / Dev / Hidden / Disabled**), and edit its display name, help text,
  and configure-mode toggles.
- **Advanced** — left sidebar lists the `settings/features/` **files by human
  name**; pick one to edit its **Default state** (`_default`) and **Keep my
  edits** (`_carry`). Most users never touch these.

Every section header and every row has a **?** help icon. Every change saves
immediately and applies to the running shell — the GUI, the CLI sub-commands,
and hand-editing the files all read and write the same `settings/` files.

## Human-readable names

Feature flags carry terse, API-derived ids (`adnsr_conn_sources_read`). Both the
GUI and the CLI (`feature show`, `feature info`, `feature area`) show a
natural-language name derived from the gated command's description ("Connection
Sources" · "List Connection Sources"). Area/acronym names live in the
user-editable **`settings/feature-labels.json`** — rename any of them there.
That file is auto-augmented when new areas appear (via `docsupdate` /
`generate_feature_flags.py`) **without overwriting your edits**, so new features
always get a sensible name in both the GUI and the CLI.


## How flags work

| Flag state | What happens |
|---|---|
| **true**  | The command(s) the flag gates appear in `?` help and run for everyone |
| **"dev"** | Hidden for normal users; appear and run only in **development mode** |
| **"hidden"** | The command runs, but is not shown in normal `?` help (revealed in dev mode) |
| **false** | Those commands are hidden from `?` and blocked for everyone |
| **absent** | Treated as `false` (safe default — unlisted features are off) |

`feature enable/disable/dev/hidden` update the running session and save
immediately to `settings/features/`. Restart ARC in another terminal/session to
pick up the same persisted state there.

## Areas — enable or disable a whole major feature

An **area** is a major capability made of many features (Advanced DNS Security,
Cloud NGFW, …). **Disabling an area is a real off switch** — every command in it
is:

- hidden from `?`, tab-completion, and help,
- blocked from running, and
- removed from the editor's **Features**, **Command Structure**, and
  **Advanced** sections.

Your individual feature settings inside the area are **remembered** and restored
when you re-enable it (disable is a master gate above the per-feature flags, not
a bulk edit).

```text
feature area                          List areas + which are enabled/disabled
feature area cloudngfw disable        Turn the whole Cloud NGFW area off
feature area "Cloud NGFW" enable      Turn it back on (name or key both work)
```

In the GUI, the **Areas** tab lists every area with an Enabled/Disabled toggle.
Disabled areas are stored in **`settings/features/local.json`** under
`_disabled_areas` (regeneration-proof), so the CLI, GUI, and hand-editing all
share the same switch.

## Run scope — where a command may run

Enablement (on/dev/off) is separate from **where** a command runs. Every command
has a **scope**, defined in code (`CommandDef.scope`):

| Scope | Meaning |
|---|---|
| **global** | Runs anywhere — no folder/device context needed |
| **folder** | Uses the active SCM folder as its filter (`cd folder <name>`) |
| **device** | Requires a device context — hidden until `cd <device>`; runs on that device (via SSH/`--remote`). This is how `ping` behaves. |

The code scope is the source of truth. You can **override** it per command when
the default is wrong for your workflow:

```text
feature scope "ping host" device     # force device scope
feature scope "show bgp" folder       # this flag gates commands at 2 scopes
feature scope "show address" reset    # clear the override (back to code default)
```

Overrides are stored in **`settings/features/local.json`** under
`_scope_overrides` (never touched by the regenerators), so they survive
`docsupdate` / `catalog rebuild`:

```jsonc
{
  "_scope_overrides": {
    "ping host": "device",
    "show bgp": "folder"
  }
}
```

`feature show` and `feature info <flag>` display the **effective** scope
(override if set, otherwise the code default). A command whose handler can't
satisfy an override (e.g. a device/SSH-only command forced to a pure-SCM scope)
still returns a clear runtime error — the tool warns you when an override
diverges from the code default.

## Domain defaults — `_default` and `_carry`

Each `settings/features/<domain>.json` file has two file-level settings, editable
from the CLI (`feature default` / `feature carry`) or the GUI **Domains** tab:

| Field | Friendly name | Meaning |
|---|---|---|
| `_default` | Default state for commands not listed | State inherited by flags absent from the file (usually `false`) |
| `_carry` | Keep my edits when regenerated | `true` = the regenerator preserves your on/dev values; `false` = the file is rebuilt fresh |

```text
feature default panos-ops on      # unlisted panos-ops flags default ON
feature carry   panos-ops on      # protect manual edits from docsupdate
```

The GUI exposes these on the **Advanced / Files** tab (with human-readable file
names).

## Aliases — shortcuts

Aliases let you type a short word instead of a full command. Two kinds:

| Kind | Stored in | Edited by |
|---|---|---|
| **System** (shared) | `settings/command-aliases.json` | GUI **Aliases** tab, or hand-edit |
| **Personal** (per-user) | `config/<user>/preferences.json` | GUI **Aliases** tab, or the `alias` builtin |

```text
alias                    List your personal aliases
alias sap show address   Create a personal alias: 'sap' runs 'show address'
alias delete sap         Remove it
```

An alias may not shadow a shell builtin or a real command word (e.g. `show`).
The GUI validates the same way.

## Command structure — how a command parses arguments

`set`/`update`/`delete` commands have a **structure** that defines their fields,
field types, and tab-completion. The GUI **Command Structure** tab lets you
reorder fields and edit each field's type (`value` / `choice` / `keyword`),
whether it's required, its hint, and its choices. Saving writes a locked
(`override: true`) entry to `settings/command-structure.json`, so a later
`command-structure update` (or `commandupdate`) never overwrites your edits:

```jsonc
"set adnsr bad-domains": {
  "override": true,
  "args": [
    { "name": "domain", "kind": "value", "required": true, "hint": "e.g. example.com" },
    { "name": "description", "kind": "keyword", "required": false, "hint": "optional note" }
  ]
}
```

Hand-editing that file, using the GUI, or running the generators all produce the
same result.

## Built-in commands

The shell's own commands (`cd`, `configure`, `commit`, `feature`, …) are
configured in **`settings/builtin-commands.json`**. The GUI **Built-ins** section
(grouped by function) lets you set each one's **visibility** — the same
four-state idea as features:

| Visibility | Meaning |
|---|---|
| **Shown** (`true`) | Listed in `?` and runnable for everyone |
| **Dev** (`"dev"`) | Only visible/runnable in development mode |
| **Hidden** (`"hidden"`) | Runs, but not listed in normal `?` (dev mode reveals it) |
| **Disabled** (`false`) | Hidden and blocked for everyone |

You can also edit the **display name**, **help text**, and the
**configure-mode** toggles. Changes save to `settings/builtin-commands.json` and
apply to the running shell's `?` / dispatch / completion immediately — the same
loader the shell already uses. Hand-editing the file produces the same result.

## Development mode — the hidden `dev` command

`"dev"` commands are invisible to normal users so a half-finished feature never
confuses anyone. Type the hidden **`dev`** command to reveal them:

```text
dev            Toggle development mode on/off  (prompt shows arc:global:dev >)
dev on         Force development mode on
dev off        Force development mode off
dev status     Show the current state without changing it
```

This enables a CI/CD lifecycle: ship a command as `"dev"`, test it in
development mode, then flip its flag to `true` when it is ready. For automation
or CI, start ARC with `ARC_DEV_MODE=1` to enter development mode immediately.

## Editing settings/features/

`settings/features/` is organized for browsing:

1. A `_GLOSSARY` explains abbreviations such as ADNSR, CDUG, CIE-DSS, cngfw,
   IAM, NGTS, and SASE.
2. Flags are grouped by **category**, then **feature/resource**.
3. Each feature has one readable `_category_resource` label line.
4. Each feature lists actions in this order: **show**, **set/create**,
   **update**, **delete**.
5. Keys beginning with `_` are descriptions/comments and are ignored by ARC.

```jsonc
{
  "_GLOSSARY": {
    "adnsr": "Advanced DNS Security Resolver",
    "cngfw": "Cloud NGFW",
    "ngts": "Next-Generation Trust Security",
    "sase": "Secure Access Service Edge"
  },

  "_section_ngts": "===== Next-Generation Trust Security =====",
  "_ngts_cert_requests": "Next-Generation Trust Security: cert_requests",
  "show_ngts_cert_requests": false,
  "show_ngts_cert_requests_id": false,
  "create_ngts_cert_requests": false
}
```

Change only the non-underscore flag values (`true`, `"dev"`, or `false`) when
editing the file manually. The in-shell `feature enable|disable|dev <flag>`
commands write those same values for you.
The generated labels are safe to leave alone and will be refreshed by
`python app/scripts/docsupdate.py`.

One-session override via environment variable (`on` | `dev` | `off`):

```bash
ARC_FEATURE_SHOW_ZONE=on arc    # force show_zone on
ARC_FEATURE_NAT_RULES=dev arc   # mark nat_rules as dev
ARC_FEATURE_SHOW_ADDRESS=off arc  # force show_address off
ARC_DEV_MODE=1 arc              # start in development mode (reveal dev commands)
```

## Regenerating from pan.dev

`python app/scripts/docsupdate.py` refreshes the local OpenAPI specs, discovers new SCM
spec files, regenerates the command catalog, and rewrites `settings/features/`
in the feature-first format above. Existing flag states are preserved when the
same flag still exists; newly discovered flags default to `false`.

Run `feature show` to see the currently loaded states grouped by ON / DEV / OFF.

## Adding a new feature (for developers)

1. For generated OpenAPI commands, run `python app/scripts/docsupdate.py`; the feature
   flag is created automatically.
2. For hand-written commands, set `feature_flag='your_flag'` on the `CommandDef`.
3. Run `python app/scripts/generate_feature_flags.py`; the new flag appears defaulted to
   `false`.
4. Edit `settings/features/` to set the flag to `"dev"` or `true` when ready.

## Related

- `settings/README.md` — overview of all user-editable files
- `help api-reference` — full API → command mapping

