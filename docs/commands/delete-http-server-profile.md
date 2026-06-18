# delete http-server-profile

Delete a **http-server-profile** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`log_profiles`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete http-server-profile <name>
```

## API

```
DELETE /config/objects/v1/http-server-profiles/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete http-server-profile MyObject
  ✓ Http-Server-Profile MyObject deleted.
```

## Related commands

- `show http-server-profile` — list http-server-profile objects (to confirm name)
- `set http-server-profile <name>` — create a http-server-profile object

---
*Generated stub.*
