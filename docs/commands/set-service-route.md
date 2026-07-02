---
command: "set service-route"
description: "Create service route settings"
category: device-device-settings
scope: global
---

# set service-route

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create service route settings

## Usage

```
set service-route [--remote]
```

## Examples

Run via SCM API:
```
arc > set service-route
```

Run directly on device via SSH:
```
arc:fw-01 > set service-route --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set service-route
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
