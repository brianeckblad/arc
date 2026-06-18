# delete profile-group

Delete a **profile-group** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`profile_groups`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete profile-group <name>
```

## API

```
DELETE /config/security/v1/profile-groups/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete profile-group MyObject
  ✓ Profile-Group MyObject deleted.
```

## Related commands

- `show profile-group` — list profile-group objects (to confirm name)
- `set profile-group <name>` — create a profile-group object

---
*Generated stub.*
