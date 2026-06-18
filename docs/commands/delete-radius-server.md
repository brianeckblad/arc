# delete radius-server

Delete a **radius-server** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`authentication`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete radius-server <name>
```

## API

```
DELETE /config/identity/v1/radius-server-profiles/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete radius-server MyObject
  ✓ Radius-Server MyObject deleted.
```

## Related commands

- `show radius-server` — list radius-server objects (to confirm name)
- `set radius-server <name>` — create a radius-server object

---
*Generated stub.*
