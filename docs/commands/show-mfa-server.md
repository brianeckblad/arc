---
command: "show mfa-server"
description: "Show MFA server profiles in the active folder"
feature_flag: authentication
category: identity
scope: folder
api: "GET /config/identity/v1/mfa-servers"
---

---
command: "show mfa-server"
description: "Show MFA server profiles in the active folder"
feature_flag: authentication
category: identity
scope: folder
api: "GET /config/identity/v1/mfa-servers"
---

---
command: "show mfa-server"
description: "Show MFA server profiles in the active folder"
feature_flag: authentication
category: identity
scope: folder
api: "GET /config/identity/v1/mfa-servers"
---

# show mfa-server

**Category:** identity
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show MFA server profiles in the active folder

## Usage

```
show mfa-server [--remote]
```

## Examples

Run via SCM API:
```
arc > show mfa-server
```

Run directly on device via SSH:
```
arc:fw-01 > show mfa-server --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show mfa-server
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
