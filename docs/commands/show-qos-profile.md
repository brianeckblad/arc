---
command: "show qos-profile"
description: "Show QoS profiles in the active folder"
feature_flag: qos
category: network
scope: folder
api: "GET /config/network/v1/qos-profiles"
---

# show qos-profile

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show QoS profiles in the active folder

## Usage

```
show qos-profile [--remote]
```

## Examples

Run via SCM API:
```
arc > show qos-profile
```

Run directly on device via SSH:
```
arc:fw-01 > show qos-profile --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show qos-profile
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
