# delete local-user-group

Delete a **local-user-group** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`local_users`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete local-user-group <name>
```

## API

```
DELETE /config/identity/v1/local-user-groups/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete local-user-group MyObject
  ✓ Local-User-Group MyObject deleted.
```

## Related commands

- `show local-user-group` — list local-user-group objects (to confirm name)
- `set local-user-group <name>` — create a local-user-group object

---
*Generated stub.*
