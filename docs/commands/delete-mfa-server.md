# delete mfa-server

Delete a **mfa-server** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`authentication`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete mfa-server <name>
```

## API

```
DELETE /config/identity/v1/mfa-servers/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete mfa-server MyObject
  ✓ Mfa-Server MyObject deleted.
```

## Related commands

- `show mfa-server` — list mfa-server objects (to confirm name)
- `set mfa-server <name>` — create a mfa-server object

---
*Generated stub.*
