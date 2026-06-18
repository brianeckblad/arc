# delete decryption-rule

Delete a **decryption-rule** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`decryption_policy`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete decryption-rule <name>
```

## API

```
DELETE /config/security/v1/decryption-rules/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete decryption-rule MyObject
  ✓ Decryption-Rule MyObject deleted.
```

## Related commands

- `show decryption-rule` — list decryption-rule objects (to confirm name)
- `set decryption-rule <name>` — create a decryption-rule object

---
*Generated stub.*
