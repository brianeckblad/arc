# delete local-user

Delete a **local-user** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`local_users`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete local-user <name>
```

## API

```
DELETE /config/identity/v1/local-users/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete local-user MyObject
  ✓ Local-User MyObject deleted.
```

## Related commands

- `show local-user` — list local-user objects (to confirm name)
- `set local-user <name>` — create a local-user object

---
*Generated stub.*
