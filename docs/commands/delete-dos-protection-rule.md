# delete dos-protection-rule

Delete a **dos-protection-rule** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`dos_protection`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete dos-protection-rule <name>
```

## API

```
DELETE /config/security/v1/dos-protection-rules/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete dos-protection-rule MyObject
  ✓ Dos-Protection-Rule MyObject deleted.
```

## Related commands

- `show dos-protection-rule` — list dos-protection-rule objects (to confirm name)
- `set dos-protection-rule <name>` — create a dos-protection-rule object

---
*Generated stub.*
