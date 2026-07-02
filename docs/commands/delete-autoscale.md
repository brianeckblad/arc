---
command: "delete autoscale"
description: "Delete autoscale settings"
category: device-device-settings
scope: global
---

# delete autoscale

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete autoscale settings

## Usage

```
delete autoscale [--remote]
```

## Examples

Run via SCM API:
```
arc > delete autoscale
```

Run directly on device via SSH:
```
arc:fw-01 > delete autoscale --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete autoscale
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
