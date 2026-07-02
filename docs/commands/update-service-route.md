---
command: "update service-route"
description: "Update service route settings"
category: device-device-settings
scope: global
---

# update service-route

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update service route settings

## Usage

```
update service-route [--remote]
```

## Examples

Run via SCM API:
```
arc > update service-route
```

Run directly on device via SSH:
```
arc:fw-01 > update service-route --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update service-route
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
