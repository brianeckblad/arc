# delete file-blocking-profile

Delete a **file-blocking-profile** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`security_profiles`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete file-blocking-profile <name>
```

## API

```
DELETE /config/security/v1/file-blocking-profiles/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete file-blocking-profile MyObject
  ✓ File-Blocking-Profile MyObject deleted.
```

## Related commands

- `show file-blocking-profile` — list file-blocking-profile objects (to confirm name)
- `set file-blocking-profile <name>` — create a file-blocking-profile object

---
*Generated stub.*
