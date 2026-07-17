---
command: "show local-user"
description: "Show local users in the active folder"
feature_flag: local_users
category: identity
scope: folder
api: "GET /config/identity/v1/local-users"
---

---
command: "show local-user"
description: "Show local users in the active folder"
feature_flag: local_users
category: identity
scope: folder
api: "GET /config/identity/v1/local-users"
---

---
command: "show local-user"
description: "Show local users in the active folder"
feature_flag: local_users
category: identity
scope: folder
api: "GET /config/identity/v1/local-users"
---

# show local-user

**Category:** identity
**API mode:** ✓ Live SCM data
**SSH mode:** `show local-user`

## Description

Show local users in the active folder

## Usage

```
show local-user [--remote]
```

## Examples

Run via SCM API:
```
arc > show local-user
```

Run directly on device via SSH:
```
arc:fw-01 > show local-user --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show local-user
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
