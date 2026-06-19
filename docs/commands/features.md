# feature — Feature Flags

ARC commands are turned on/off by **feature flags** stored in
**`settings/features.json`**.  This lets you ship an MVP with a handful of
commands and enable the rest as they are built and tested — without touching
any Python.  `settings/features.json` is the single source of truth.

## Usage (inside ARC)

```text
feature show                 List every flag grouped ENABLED / DISABLED
feature enable <flag>        Turn one on for this session (not saved)
feature disable <flag>       Turn one off for this session (not saved)
feature ?                    Show the sub-command summary
feature enable ?             List flags currently OFF (candidates to enable)
feature disable ?            List flags currently ON (candidates to disable)
feature help                 Show this page
```

## How flags work

| Flag state | What happens |
|---|---|
| **true**  | The command(s) the flag gates appear in `?` help and run normally |
| **false** | Those commands are hidden from `?` and blocked at runtime |
| **absent** | Treated as `false` (safe default — unlisted features are off) |

`feature enable/disable` change the running session only. To make a change
**permanent**, edit `settings/features.json` and restart ARC.

## Editing settings/features.json

```jsonc
{
  "_README": "comment keys start with _ and are ignored",
  "show_address": true,
  "show_zone": false,
  "test_security_policy_match": true
}
```

One-session override via environment variable:

```bash
ARC_FEATURE_SHOW_ZONE=1 arc     # force show_zone on
ARC_FEATURE_SHOW_ADDRESS=0 arc  # force show_address off
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
| `test_security_policy_match` | packet-tracer / test security-policy-match |

Everything else ships **off**. Run `feature show` to see the full list.

## Adding a new feature (for developers)

1. Set `feature_flag='your_flag'` on the CommandDef in `app/commands/<module>.py`
2. Add `"your_flag": false` to `settings/features.json`
3. Flip it to `true` when the command is ready to ship

## Related

- `settings/README.md` — overview of all user-editable files
- `help api-reference` — full API → command mapping

