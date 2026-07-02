---
command: "delete update-schedule"
description: "Delete update schedule settings"
category: device-device-settings
scope: global
---

# delete update-schedule

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete update schedule settings

## Usage

```
delete update-schedule [--remote]
```

## Examples

Run via SCM API:
```
arc > delete update-schedule
```

Run directly on device via SSH:
```
arc:fw-01 > delete update-schedule --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete update-schedule
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
