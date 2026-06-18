# delete dos-protection-profile

Delete a **dos-protection-profile** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`dos_protection`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete dos-protection-profile <name>
```

## API

```
DELETE /config/security/v1/dos-protection-profiles/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete dos-protection-profile MyObject
  ✓ Dos-Protection-Profile MyObject deleted.
```

## Related commands

- `show dos-protection-profile` — list dos-protection-profile objects (to confirm name)
- `set dos-protection-profile <name>` — create a dos-protection-profile object

---
*Generated stub.*
