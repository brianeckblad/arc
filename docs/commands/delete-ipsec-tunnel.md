# delete ipsec-tunnel

Delete a **ipsec-tunnel** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`ipsec_vpn`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete ipsec-tunnel <name>
```

## API

```
DELETE /config/network/v1/ipsec-tunnels/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete ipsec-tunnel MyObject
  ✓ Ipsec-Tunnel MyObject deleted.
```

## Related commands

- `show ipsec-tunnel` — list ipsec-tunnel objects (to confirm name)
- `set ipsec-tunnel <name>` — create a ipsec-tunnel object

---
*Generated stub.*
