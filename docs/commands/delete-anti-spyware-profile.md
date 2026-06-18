# delete anti-spyware-profile

Delete a **anti-spyware-profile** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`security_profiles`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete anti-spyware-profile <name>
```

## API

```
DELETE /config/security/v1/anti-spyware-profiles/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete anti-spyware-profile MyObject
  ✓ Anti-Spyware-Profile MyObject deleted.
```

## Related commands

- `show anti-spyware-profile` — list anti-spyware-profile objects (to confirm name)
- `set anti-spyware-profile <name>` — create a anti-spyware-profile object

---
*Generated stub.*
