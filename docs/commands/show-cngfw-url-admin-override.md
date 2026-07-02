---
command: "show cngfw url-admin-override"
description: "URL Admin Override"
usage: "show cngfw url-admin-override"
feature_flag: cngfw_url_admin_override_read
category: cloudngfw
scope: global
api: "GET https://api.strata.paloaltonetworks.com/config/security/v1/url-admin-override"
---

# show url-admin-override

List **url-admin-override** objects in the active SCM folder.

## Feature flag

This command requires **`url_admin_override`** to be enabled:

```bash
arc> feature enable url_admin_override
```

## Syntax

```text
show url-admin-override
show url-admin-override --remote    # live device state via SSH
```

## API

```
GET /config/security/v1/url-admin-override?folder=<active-folder>
```

Notes: admin password for overriding URL filtering

## Output

Returns a table of url-admin-override objects with key fields.

## Example

```text
arc:global > feature enable url_admin_override
arc:global > show url-admin-override
  Name           ...
  ─────────────  ...
  my-object      ...
```

## Related commands

- `set url-admin-override <name>` — create a url-admin-override object
- `delete url-admin-override <name>` — remove a url-admin-override object
- `help features` — manage feature flags

---
*Generated stub.*
