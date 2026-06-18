# show file-blocking-profile

List **file-blocking-profile** objects in the active SCM folder.

## Feature flag

This command requires **`security_profiles`** to be enabled:

```bash
arc> feature enable security_profiles
```

## Syntax

```text
show file-blocking-profile
show file-blocking-profile --remote    # live device state via SSH
```

## API

```
GET /config/security/v1/file-blocking-profiles?folder=<active-folder>
```

Notes: file type blocking profile

## Output

Returns a table of file-blocking-profile objects with key fields.

## Example

```text
arc:global > feature enable security_profiles
arc:global > show file-blocking-profile
  Name           ...
  ─────────────  ...
  my-object      ...
```

## Related commands

- `set file-blocking-profile <name>` — create a file-blocking-profile object
- `delete file-blocking-profile <name>` — remove a file-blocking-profile object
- `help features` — manage feature flags

---
*Generated stub.*
