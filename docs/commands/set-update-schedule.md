---
command: "set update-schedule"
description: "Create update schedule settings"
category: device-device-settings
scope: global
---

# set update-schedule

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create update schedule settings

## Usage

```
set update-schedule [--remote]
```

## Examples

Run via SCM API:
```
arc > set update-schedule
```

Run directly on device via SSH:
```
arc:fw-01 > set update-schedule --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set update-schedule
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
