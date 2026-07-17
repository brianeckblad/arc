---
command: "delete authentication-profile"
description: "Delete an authentication profile — delete authentication-profile <name>"
usage: "delete authentication-profile <name>"
feature_flag: authentication
category: identity
scope: folder
---

---
command: "delete authentication-profile"
description: "Delete an authentication profile — delete authentication-profile <name>"
usage: "delete authentication-profile <name>"
feature_flag: authentication
category: identity
scope: folder
---

# delete authentication-profile

Delete a **authentication-profile** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`authentication`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete authentication-profile <name>
```

## API

```
DELETE /config/identity/v1/authentication-profiles/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete authentication-profile MyObject
  ✓ Authentication-Profile MyObject deleted.
```

## Related commands

- `show authentication-profile` — list authentication-profile objects (to confirm name)
- `set authentication-profile <name>` — create a authentication-profile object

---
*Generated stub.*
