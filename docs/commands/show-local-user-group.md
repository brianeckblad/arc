---
command: "show local-user-group"
description: "Show local user groups in the active folder"
feature_flag: local_users
category: identity
scope: folder
api: "GET /config/identity/v1/local-user-groups"
---

# show local-user-group

**Category:** identity
**API mode:** ✓ Live SCM data
**SSH mode:** `show local-user-group`

## Description

Show local user groups in the active folder

## Usage

```
show local-user-group [--remote]
```

## Examples

Run via SCM API:
```
arc > show local-user-group
```

Run directly on device via SSH:
```
arc:fw-01 > show local-user-group --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show local-user-group
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
