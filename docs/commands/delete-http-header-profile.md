# delete http-header-profile

Delete a **http-header-profile** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`security_profiles`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete http-header-profile <name>
```

## API

```
DELETE /config/security/v1/http-header-profiles/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete http-header-profile MyObject
  ✓ Http-Header-Profile MyObject deleted.
```

## Related commands

- `show http-header-profile` — list http-header-profile objects (to confirm name)
- `set http-header-profile <name>` — create a http-header-profile object

---
*Generated stub.*
