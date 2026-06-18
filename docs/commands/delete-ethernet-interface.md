# delete ethernet-interface

Delete a **ethernet-interface** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`show_interface`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete ethernet-interface <name>
```

## API

```
DELETE /config/network/v1/ethernet-interfaces/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete ethernet-interface MyObject
  ✓ Ethernet-Interface MyObject deleted.
```

## Related commands

- `show ethernet-interface` — list ethernet-interface objects (to confirm name)
- `set ethernet-interface <name>` — create a ethernet-interface object

---
*Generated stub.*
