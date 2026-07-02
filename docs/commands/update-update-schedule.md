---
command: "update update-schedule"
description: "Update update schedule settings"
category: device-device-settings
scope: global
---

# update update-schedule

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update update schedule settings

## Usage

```
update update-schedule [--remote]
```

## Examples

Run via SCM API:
```
arc > update update-schedule
```

Run directly on device via SSH:
```
arc:fw-01 > update update-schedule --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update update-schedule
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
