# show data-filtering-profile

List **data-filtering-profile** objects in the active SCM folder.

## Feature flag

This command requires **`security_profiles`** to be enabled:

```bash
arc> feature enable security_profiles
```

## Syntax

```text
show data-filtering-profile
show data-filtering-profile --remote    # live device state via SSH
```

## API

```
GET /config/security/v1/data-filtering-profiles?folder=<active-folder>
```

Notes: data loss prevention (DLP) profile

## Output

Returns a table of data-filtering-profile objects with key fields.

## Example

```text
arc:global > feature enable security_profiles
arc:global > show data-filtering-profile
  Name           ...
  ─────────────  ...
  my-object      ...
```

## Related commands

- `set data-filtering-profile <name>` — create a data-filtering-profile object
- `delete data-filtering-profile <name>` — remove a data-filtering-profile object
- `help features` — manage feature flags

---
*Generated stub.*
