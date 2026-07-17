---
command: "show profile-group"
description: "Show security profile groups in the active folder"
feature_flag: profile_groups
category: security
scope: folder
api: "GET /config/security/v1/profile-groups"
---

---
command: "show profile-group"
description: "Show security profile groups in the active folder"
feature_flag: profile_groups
category: security
scope: folder
api: "GET /config/security/v1/profile-groups"
---

---
command: "show profile-group"
description: "Show security profile groups in the active folder"
feature_flag: profile_groups
category: security
scope: folder
api: "GET /config/security/v1/profile-groups"
---

# show profile-group

**Category:** security
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show security profile groups in the active folder

## Usage

```
show profile-group [--remote]
```

## Examples

Run via SCM API:
```
arc > show profile-group
```

Run directly on device via SSH:
```
arc:fw-01 > show profile-group --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show profile-group
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
