# show http-server-profile

List **http-server-profile** objects in the active SCM folder.

## Feature flag

This command requires **`log_profiles`** to be enabled:

```bash
arc> feature enable log_profiles
```

## Syntax

```text
show http-server-profile
show http-server-profile --remote    # live device state via SSH
```

## API

```
GET /config/objects/v1/http-server-profiles?folder=<active-folder>
```

Notes: HTTP server profile for log forwarding

## Output

Returns a table of http-server-profile objects with key fields.

## Example

```text
arc:global > feature enable log_profiles
arc:global > show http-server-profile
  Name           ...
  ─────────────  ...
  my-object      ...
```

## Related commands

- `set http-server-profile <name>` — create a http-server-profile object
- `delete http-server-profile <name>` — remove a http-server-profile object
- `help features` — manage feature flags

---
*Generated stub.*
