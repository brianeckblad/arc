# delete virtual-router

Delete a **virtual-router** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`show_routing`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete virtual-router <name>
```

## API

```
DELETE /config/network/v1/virtual-routers/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete virtual-router MyObject
  ✓ Virtual-Router MyObject deleted.
```

## Related commands

- `show virtual-router` — list virtual-router objects (to confirm name)
- `set virtual-router <name>` — create a virtual-router object

---
*Generated stub.*
