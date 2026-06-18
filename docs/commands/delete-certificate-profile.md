# delete certificate-profile

Delete a **certificate-profile** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`certificates`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete certificate-profile <name>
```

## API

```
DELETE /config/identity/v1/certificate-profiles/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete certificate-profile MyObject
  ✓ Certificate-Profile MyObject deleted.
```

## Related commands

- `show certificate-profile` — list certificate-profile objects (to confirm name)
- `set certificate-profile <name>` — create a certificate-profile object

---
*Generated stub.*
