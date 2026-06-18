# delete tunnel-interface

Delete a **tunnel-interface** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`ipsec_vpn`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete tunnel-interface <name>
```

## API

```
DELETE /config/network/v1/tunnel-interfaces/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete tunnel-interface MyObject
  ✓ Tunnel-Interface MyObject deleted.
```

## Related commands

- `show tunnel-interface` — list tunnel-interface objects (to confirm name)
- `set tunnel-interface <name>` — create a tunnel-interface object

---
*Generated stub.*
