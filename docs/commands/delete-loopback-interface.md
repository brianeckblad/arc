# delete loopback-interface

Delete a **loopback-interface** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`show_interface`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete loopback-interface <name>
```

## API

```
DELETE /config/network/v1/loopback-interfaces/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete loopback-interface MyObject
  ✓ Loopback-Interface MyObject deleted.
```

## Related commands

- `show loopback-interface` — list loopback-interface objects (to confirm name)
- `set loopback-interface <name>` — create a loopback-interface object

---
*Generated stub.*
