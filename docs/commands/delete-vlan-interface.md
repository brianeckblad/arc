# delete vlan-interface

Delete a **vlan-interface** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`show_interface`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete vlan-interface <name>
```

## API

```
DELETE /config/network/v1/vlan-interfaces/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete vlan-interface MyObject
  ✓ Vlan-Interface MyObject deleted.
```

## Related commands

- `show vlan-interface` — list vlan-interface objects (to confirm name)
- `set vlan-interface <name>` — create a vlan-interface object

---
*Generated stub.*
