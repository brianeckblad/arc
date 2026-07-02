---
command: "delete cngfw url-admin-override"
description: "Delete a url admin override"
usage: "delete cngfw url-admin-override id <value>"
feature_flag: cngfw_url_admin_override_write
category: cloudngfw
scope: global
api: "DELETE https://api.strata.paloaltonetworks.com/config/security/v1/url-admin-override/{id}"
---

# delete url-admin-override

Delete a **url-admin-override** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`url_admin_override`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete url-admin-override <name>
```

## API

```
DELETE /config/security/v1/url-admin-override/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete url-admin-override MyObject
  ✓ Url-Admin-Override MyObject deleted.
```

## Related commands

- `show url-admin-override` — list url-admin-override objects (to confirm name)
- `set url-admin-override <name>` — create a url-admin-override object

---
*Generated stub.*
