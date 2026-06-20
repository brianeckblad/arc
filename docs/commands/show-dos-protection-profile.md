---
command: "show dos-protection-profile"
description: "Show DoS protection profiles in the active folder"
feature_flag: dos_protection
category: security
scope: folder
api: "GET /config/security/v1/dos-protection-profiles"
---

# show dos-protection-profile

**Category:** security
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show DoS protection profiles in the active folder

## Usage

```
show dos-protection-profile [--remote]
```

## Examples

Run via SCM API:
```
arc > show dos-protection-profile
```

Run directly on device via SSH:
```
arc:fw-01 > show dos-protection-profile --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show dos-protection-profile
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
