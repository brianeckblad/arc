# delete ike-gateway

Delete a **ike-gateway** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`ipsec_vpn`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete ike-gateway <name>
```

## API

```
DELETE /config/network/v1/ike-gateways/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete ike-gateway MyObject
  ✓ Ike-Gateway MyObject deleted.
```

## Related commands

- `show ike-gateway` — list ike-gateway objects (to confirm name)
- `set ike-gateway <name>` — create a ike-gateway object

---
*Generated stub.*
