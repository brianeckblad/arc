---
command: "delete service-route"
description: "Delete service route settings"
category: device-device-settings
scope: global
---

# delete service-route

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete service route settings

## Usage

```
delete service-route [--remote]
```

## Examples

Run via SCM API:
```
arc > delete service-route
```

Run directly on device via SSH:
```
arc:fw-01 > delete service-route --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete service-route
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
