# delete decryption-exclusion

Delete a **decryption-exclusion** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`decryption_policy`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete decryption-exclusion <name>
```

## API

```
DELETE /config/security/v1/decryption-exclusions/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete decryption-exclusion MyObject
  ✓ Decryption-Exclusion MyObject deleted.
```

## Related commands

- `show decryption-exclusion` — list decryption-exclusion objects (to confirm name)
- `set decryption-exclusion <name>` — create a decryption-exclusion object

---
*Generated stub.*
