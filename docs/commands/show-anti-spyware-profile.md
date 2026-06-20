---
command: "show anti-spyware-profile"
description: "Show anti-spyware profiles in the active folder"
feature_flag: security_profiles
category: security
scope: folder
api: "GET /config/security/v1/anti-spyware-profiles"
---

# show anti-spyware-profile

**Category:** security
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show anti-spyware profiles in the active folder

## Usage

```
show anti-spyware-profile [--remote]
```

## Examples

Run via SCM API:
```
arc > show anti-spyware-profile
```

Run directly on device via SSH:
```
arc:fw-01 > show anti-spyware-profile --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show anti-spyware-profile
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
