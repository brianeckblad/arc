# feature — Feature Flags

ARC commands are turned on/off by **feature flags** stored in
**`settings/features.json`**.  This lets you ship an MVP with a handful of
commands and roll out the rest as they are built and tested — without touching
any Python.  `settings/features.json` is the single source of truth.

Every flag has **three states**: `true` (on for everyone), `"dev"` (under
development — hidden until development mode is on), and `false` (off for
everyone).

## Usage (inside ARC)

```text
feature show                 List every flag grouped ON / DEV / OFF
feature enable <flag>        Set one ON for this session (not saved)
feature disable <flag>       Set one OFF for this session (not saved)
feature dev <flag>           Mark one DEV for this session (not saved)
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

`feature enable/disable/dev` change the running session only. To make a change
**permanent**, edit `settings/features.json` and restart ARC.

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

```jsonc
{
  "_README": "comment keys start with _ and are ignored",
  "show_address": true,
  "nat_rules": "dev",
  "delete_objects": false,
  "packet_tracer": true
}
```

One-session override via environment variable (`on` | `dev` | `off`):

```bash
ARC_FEATURE_SHOW_ZONE=on arc    # force show_zone on
ARC_FEATURE_NAT_RULES=dev arc   # mark nat_rules as dev
ARC_FEATURE_SHOW_ADDRESS=off arc  # force show_address off
ARC_DEV_MODE=1 arc              # start in development mode (reveal dev commands)
```

## MVP defaults (shipped on)

| Flag | Commands |
|------|----------|
| `show_devices` | show devices / show device / show device snippets |
| `show_address` | show address |
| `show_service` | show service |
| `show_security_policy` | show security policy |
| `show_snippets` | show snippet / show snippets / show snippets global |
| `show_system_info` | show system info |
| `show_jobs` | show jobs all / show jobs id |
| `packet_tracer` | packet-tracer / test security-policy-match |

Everything else ships as **`"dev"`** (visible in development mode) or **`false`**.
Run `feature show` to see the full list grouped by state.

## Adding a new feature (for developers)

1. Set `feature_flag='your_flag'` on the CommandDef in `app/commands/<module>.py`
2. Add `"your_flag": "dev"` to `settings/features.json` while building it
3. Flip it to `true` when the command is ready to ship for everyone

## Related

- `settings/README.md` — overview of all user-editable files
- `help api-reference` — full API → command mapping

