---
command: "set cngfw url-admin-override"
description: "Add URL Admin Override"
usage: "set cngfw url-admin-override [password <value>] [ssl-tls-service-profile <value>]"
feature_flag: cngfw_url_admin_override_write
category: cloudngfw
scope: global
api: "POST https://api.strata.paloaltonetworks.com/config/security/v1/url-admin-override"
---

---
command: "set cngfw url-admin-override"
description: "Add URL Admin Override"
usage: "set cngfw url-admin-override [password <value>] [ssl-tls-service-profile <value>]"
feature_flag: cngfw_url_admin_override_write
category: cloudngfw
scope: global
api: "POST https://api.strata.paloaltonetworks.com/config/security/v1/url-admin-override"
---

---
command: "set cngfw url-admin-override"
description: "Add URL Admin Override"
usage: "set cngfw url-admin-override [password <value>] [ssl-tls-service-profile <value>]"
feature_flag: cngfw_url_admin_override_write
category: cloudngfw
scope: global
api: "POST https://api.strata.paloaltonetworks.com/config/security/v1/url-admin-override"
---

# set url-admin-override

Create a **url-admin-override** object in the active SCM folder.

## Feature flag

This command requires the **`url_admin_override`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable url_admin_override

# Enable permanently (its settings/features/ file — git-ignored):
{"  \"url_admin_override\": true"}
```

## Syntax

```text
configure
set url-admin-override <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/security/v1/url-admin-override
```

Resource notes: admin password for overriding URL filtering

## Supported methods

- GET (list)
- POST (create)
- PUT (update)
- DELETE

## Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `name` | Yes | Object name (must be unique in folder) |
| `folder` | Yes | Set automatically from active folder context |
| `description` | No | Human-readable description |
| `tag` | No | One or more tag names to associate |

> **Full schema:** See `docs/scm-api/specs/ngfw-security.md` for all fields.

## Example

```text
arc:global > configure
arc:global # feature enable url_admin_override
arc:global # set url-admin-override MyObject ...
  ✓ Url-Admin-Override MyObject created (id: ...)
```

## Related commands

- `show url-admin-override` — list url-admin-override objects in the active folder
- `delete url-admin-override <name>` — remove a url-admin-override object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
