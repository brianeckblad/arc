# delete dhcp-interface

Delete a **dhcp-interface** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`dhcp`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete dhcp-interface <name>
```

## API

```
DELETE /config/network/v1/dhcp-interfaces/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete dhcp-interface MyObject
  ✓ Dhcp-Interface MyObject deleted.
```

## Related commands

- `show dhcp-interface` — list dhcp-interface objects (to confirm name)
- `set dhcp-interface <name>` — create a dhcp-interface object

---
*Generated stub.*
