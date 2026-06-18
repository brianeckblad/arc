# show url-access-profile

List **url-access-profile** objects in the active SCM folder.

## Feature flag

This command requires **`security_profiles`** to be enabled:

```bash
arc> feature enable security_profiles
```

## Syntax

```text
show url-access-profile
show url-access-profile --remote    # live device state via SSH
```

## API

```
GET /config/security/v1/url-access-profiles?folder=<active-folder>
```

Notes: URL filtering access profile

## Output

Returns a table of url-access-profile objects with key fields.

## Example

```text
arc:global > feature enable security_profiles
arc:global > show url-access-profile
  Name           ...
  ─────────────  ...
  my-object      ...
```

## Related commands

- `set url-access-profile <name>` — create a url-access-profile object
- `delete url-access-profile <name>` — remove a url-access-profile object
- `help features` — manage feature flags

---
*Generated stub.*
