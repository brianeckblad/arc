# delete url-access-profile

Delete a **url-access-profile** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`security_profiles`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete url-access-profile <name>
```

## API

```
DELETE /config/security/v1/url-access-profiles/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete url-access-profile MyObject
  ✓ Url-Access-Profile MyObject deleted.
```

## Related commands

- `show url-access-profile` — list url-access-profile objects (to confirm name)
- `set url-access-profile <name>` — create a url-access-profile object

---
*Generated stub.*
