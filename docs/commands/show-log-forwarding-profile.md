---
command: "show log-forwarding-profile"
description: "Show log forwarding profiles in the active folder"
feature_flag: log_profiles
category: objects
scope: folder
api: "GET /config/objects/v1/log-forwarding-profiles"
---

# show log-forwarding-profile

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show log forwarding profiles in the active folder

## Usage

```
show log-forwarding-profile [--remote]
```

## Examples

Run via SCM API:
```
arc > show log-forwarding-profile
```

Run directly on device via SSH:
```
arc:fw-01 > show log-forwarding-profile --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show log-forwarding-profile
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
