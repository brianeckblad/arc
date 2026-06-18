# delete tls-service-profile

Delete a **tls-service-profile** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`certificates`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete tls-service-profile <name>
```

## API

```
DELETE /config/identity/v1/tls-service-profiles/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete tls-service-profile MyObject
  ✓ Tls-Service-Profile MyObject deleted.
```

## Related commands

- `show tls-service-profile` — list tls-service-profile objects (to confirm name)
- `set tls-service-profile <name>` — create a tls-service-profile object

---
*Generated stub.*
