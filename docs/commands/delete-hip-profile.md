# delete hip-profile

Delete a **hip-profile** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`hip`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete hip-profile <name>
```

## API

```
DELETE /config/objects/v1/hip-profiles/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete hip-profile MyObject
  ✓ Hip-Profile MyObject deleted.
```

## Related commands

- `show hip-profile` — list hip-profile objects (to confirm name)
- `set hip-profile <name>` — create a hip-profile object

---
*Generated stub.*
