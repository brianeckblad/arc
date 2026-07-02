---
command: "show service-route"
description: "List service route settings"
category: device-device-settings
scope: global
---

# show service-route

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List service route settings

## Usage

```
show service-route [--remote]
```

## Examples

Run via SCM API:
```
arc > show service-route
```

Run directly on device via SSH:
```
arc:fw-01 > show service-route --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show service-route
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
