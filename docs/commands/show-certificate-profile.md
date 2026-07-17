---
command: "show certificate-profile"
description: "Show certificate profiles in the active folder"
feature_flag: certificates
category: identity
scope: folder
api: "GET /config/identity/v1/certificate-profiles"
---

---
command: "show certificate-profile"
description: "Show certificate profiles in the active folder"
feature_flag: certificates
category: identity
scope: folder
api: "GET /config/identity/v1/certificate-profiles"
---

---
command: "show certificate-profile"
description: "Show certificate profiles in the active folder"
feature_flag: certificates
category: identity
scope: folder
api: "GET /config/identity/v1/certificate-profiles"
---

# show certificate-profile

**Category:** identity
**API mode:** ✓ Live SCM data
**SSH mode:** `show certificate-profile`

## Description

Show certificate profiles in the active folder

## Usage

```
show certificate-profile [--remote]
```

## Examples

Run via SCM API:
```
arc > show certificate-profile
```

Run directly on device via SSH:
```
arc:fw-01 > show certificate-profile --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show certificate-profile
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
