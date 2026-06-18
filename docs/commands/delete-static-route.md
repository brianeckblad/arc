# delete static-route

Delete a **static-route** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`show_routing`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete static-route <name>
```

## API

```
DELETE /config/network/v1/routing/static-routes/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete static-route MyObject
  ✓ Static-Route MyObject deleted.
```

## Related commands

- `show static-route` — list static-route objects (to confirm name)
- `set static-route <name>` — create a static-route object

---
*Generated stub.*
