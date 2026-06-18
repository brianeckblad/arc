# delete dns-security-profile

Delete a **dns-security-profile** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`security_profiles`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete dns-security-profile <name>
```

## API

```
DELETE /config/security/v1/dns-security-profiles/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete dns-security-profile MyObject
  ✓ Dns-Security-Profile MyObject deleted.
```

## Related commands

- `show dns-security-profile` — list dns-security-profile objects (to confirm name)
- `set dns-security-profile <name>` — create a dns-security-profile object

---
*Generated stub.*
