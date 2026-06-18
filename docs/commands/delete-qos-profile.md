# delete qos-profile

Delete a **qos-profile** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`qos`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete qos-profile <name>
```

## API

```
DELETE /config/network/v1/qos-profiles/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete qos-profile MyObject
  ✓ Qos-Profile MyObject deleted.
```

## Related commands

- `show qos-profile` — list qos-profile objects (to confirm name)
- `set qos-profile <name>` — create a qos-profile object

---
*Generated stub.*
