# feature — Feature Flags

ARC commands are turned on/off by **feature flags** stored in
**`settings/features.json`**.  The file is generated from the pulled OpenAPI
specs plus explicit ARC commands, then edited by operators to enable the pieces
they want.  New generated flags default to `false` so API surface fails closed
until intentionally enabled.

Every flag has **three states**: `true` (on for everyone), `"dev"` (under
development — hidden until development mode is on), and `false` (off for
everyone).

## Usage (inside ARC)

```text
feature show                 List every flag grouped ON / DEV / OFF
feature show on              List only enabled flags
feature show off             List only disabled flags
feature show dev             List only development flags
feature show <name>          List flags/commands matching a name fragment
show feature on              Alias for feature show on
show feature off             Alias for feature show off
show feature <name>          Alias for feature show <name>
feature enable <flag>        Set one ON and save to settings/features.json
feature disable <flag>       Set one OFF and save to settings/features.json
feature dev <flag>           Mark one DEV and save to settings/features.json
feature ?                    Show the sub-command summary
feature enable ?             List flags not yet ON
feature disable ?            List flags not yet OFF
feature help                 Show this page

dev                          Toggle development mode (reveal DEV commands)
```

## How flags work

| Flag state | What happens |
|---|---|
| **true**  | The command(s) the flag gates appear in `?` help and run for everyone |
| **"dev"** | Hidden for normal users; appear and run only in **development mode** |
| **false** | Those commands are hidden from `?` and blocked for everyone |
| **absent** | Treated as `false` (safe default — unlisted features are off) |

`feature enable/disable/dev` update the running session and save immediately to
`settings/features.json`. Restart ARC in another terminal/session to pick up the
same persisted state there.

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

## Editing settings/features.json

`settings/features.json` is organized for browsing:

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
`python dev/docsupdate.py`.

One-session override via environment variable (`on` | `dev` | `off`):

```bash
ARC_FEATURE_SHOW_ZONE=on arc    # force show_zone on
ARC_FEATURE_NAT_RULES=dev arc   # mark nat_rules as dev
ARC_FEATURE_SHOW_ADDRESS=off arc  # force show_address off
ARC_DEV_MODE=1 arc              # start in development mode (reveal dev commands)
```

## Regenerating from pan.dev

`python dev/docsupdate.py` refreshes the local OpenAPI specs, discovers new SCM
spec files, regenerates the command catalog, and rewrites `settings/features.json`
in the feature-first format above. Existing flag states are preserved when the
same flag still exists; newly discovered flags default to `false`.

Run `feature show` to see the currently loaded states grouped by ON / DEV / OFF.

## Adding a new feature (for developers)

1. For generated OpenAPI commands, run `python dev/docsupdate.py`; the feature
   flag is created automatically.
2. For hand-written commands, set `feature_flag='your_flag'` on the `CommandDef`.
3. Run `python dev/generate_feature_flags.py`; the new flag appears defaulted to
   `false`.
4. Edit `settings/features.json` to set the flag to `"dev"` or `true` when ready.

## Related

- `settings/README.md` — overview of all user-editable files
- `help api-reference` — full API → command mapping

