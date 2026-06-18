# delete dynamic-user-group

Delete a **dynamic-user-group** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`local_users`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete dynamic-user-group <name>
```

## API

```
DELETE /config/objects/v1/dynamic-user-groups/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete dynamic-user-group MyObject
  ✓ Dynamic-User-Group MyObject deleted.
```

## Related commands

- `show dynamic-user-group` — list dynamic-user-group objects (to confirm name)
- `set dynamic-user-group <name>` — create a dynamic-user-group object

---
*Generated stub.*
