# delete log-forwarding-profile

Delete a **log-forwarding-profile** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`log_profiles`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete log-forwarding-profile <name>
```

## API

```
DELETE /config/objects/v1/log-forwarding-profiles/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete log-forwarding-profile MyObject
  ✓ Log-Forwarding-Profile MyObject deleted.
```

## Related commands

- `show log-forwarding-profile` — list log-forwarding-profile objects (to confirm name)
- `set log-forwarding-profile <name>` — create a log-forwarding-profile object

---
*Generated stub.*
