# delete application-group

Delete a **application-group** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`app_groups`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete application-group <name>
```

## API

```
DELETE /config/objects/v1/application-groups/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete application-group MyObject
  ✓ Application-Group MyObject deleted.
```

## Related commands

- `show application-group` — list application-group objects (to confirm name)
- `set application-group <name>` — create a application-group object

---
*Generated stub.*
