---
command: "show autoscale"
description: "Get autoscale settings"
category: device-device-settings
scope: global
---

# show autoscale

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get autoscale settings

## Usage

```
show autoscale [--remote]
```

## Examples

Run via SCM API:
```
arc > show autoscale
```

Run directly on device via SSH:
```
arc:fw-01 > show autoscale --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show autoscale
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
