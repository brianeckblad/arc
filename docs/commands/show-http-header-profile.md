# show http-header-profile

List **http-header-profile** objects in the active SCM folder.

## Feature flag

This command requires **`security_profiles`** to be enabled:

```bash
arc> feature enable security_profiles
```

## Syntax

```text
show http-header-profile
show http-header-profile --remote    # live device state via SSH
```

## API

```
GET /config/security/v1/http-header-profiles?folder=<active-folder>
```

Notes: HTTP header insertion profiles

## Output

Returns a table of http-header-profile objects with key fields.

## Example

```text
arc:global > feature enable security_profiles
arc:global > show http-header-profile
  Name           ...
  ─────────────  ...
  my-object      ...
```

## Related commands

- `set http-header-profile <name>` — create a http-header-profile object
- `delete http-header-profile <name>` — remove a http-header-profile object
- `help features` — manage feature flags

---
*Generated stub.*
