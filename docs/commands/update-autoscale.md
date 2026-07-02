---
command: "update autoscale"
description: "Update autoscale settings"
category: device-device-settings
scope: global
---

# update autoscale

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update autoscale settings

## Usage

```
update autoscale [--remote]
```

## Examples

Run via SCM API:
```
arc > update autoscale
```

Run directly on device via SSH:
```
arc:fw-01 > update autoscale --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update autoscale
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
