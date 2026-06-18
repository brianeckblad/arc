# delete wildfire-profile

Delete a **wildfire-profile** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`security_profiles`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete wildfire-profile <name>
```

## API

```
DELETE /config/security/v1/wildfire-anti-virus-profiles/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete wildfire-profile MyObject
  ✓ Wildfire-Profile MyObject deleted.
```

## Related commands

- `show wildfire-profile` — list wildfire-profile objects (to confirm name)
- `set wildfire-profile <name>` — create a wildfire-profile object

---
*Generated stub.*
