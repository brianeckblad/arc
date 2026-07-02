---
command: "set autoscale"
description: "Create autoscale settings"
category: device-device-settings
scope: global
---

# set autoscale

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create autoscale settings

## Usage

```
set autoscale [--remote]
```

## Examples

Run via SCM API:
```
arc > set autoscale
```

Run directly on device via SSH:
```
arc:fw-01 > set autoscale --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set autoscale
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
