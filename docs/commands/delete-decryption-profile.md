# delete decryption-profile

Delete a **decryption-profile** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`decryption_policy`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete decryption-profile <name>
```

## API

```
DELETE /config/security/v1/decryption-profiles/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete decryption-profile MyObject
  ✓ Decryption-Profile MyObject deleted.
```

## Related commands

- `show decryption-profile` — list decryption-profile objects (to confirm name)
- `set decryption-profile <name>` — create a decryption-profile object

---
*Generated stub.*
