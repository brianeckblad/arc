# show syslog-server-profile

List **syslog-server-profile** objects in the active SCM folder.

## Feature flag

This command requires **`log_profiles`** to be enabled:

```bash
arc> feature enable log_profiles
```

## Syntax

```text
show syslog-server-profile
show syslog-server-profile --remote    # live device state via SSH
```

## API

```
GET /config/objects/v1/syslog-server-profiles?folder=<active-folder>
```

Notes: syslog server configuration for log forwarding

## Output

Returns a table of syslog-server-profile objects with key fields.

## Example

```text
arc:global > feature enable log_profiles
arc:global > show syslog-server-profile
  Name           ...
  ─────────────  ...
  my-object      ...
```

## Related commands

- `set syslog-server-profile <name>` — create a syslog-server-profile object
- `delete syslog-server-profile <name>` — remove a syslog-server-profile object
- `help features` — manage feature flags

---
*Generated stub.*
