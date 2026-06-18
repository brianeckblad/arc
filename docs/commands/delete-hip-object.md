# delete hip-object

Delete a **hip-object** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`hip`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete hip-object <name>
```

## API

```
DELETE /config/objects/v1/hip-objects/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete hip-object MyObject
  ✓ Hip-Object MyObject deleted.
```

## Related commands

- `show hip-object` — list hip-object objects (to confirm name)
- `set hip-object <name>` — create a hip-object object

---
*Generated stub.*
