# delete bgp-profile

Delete a **bgp-profile** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`bgp_routing`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete bgp-profile <name>
```

## API

```
DELETE /config/network/v1/bgp-address-family-profiles/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete bgp-profile MyObject
  ✓ Bgp-Profile MyObject deleted.
```

## Related commands

- `show bgp-profile` — list bgp-profile objects (to confirm name)
- `set bgp-profile <name>` — create a bgp-profile object

---
*Generated stub.*
