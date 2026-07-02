---
command: "set cngfw schedules"
description: "Create a schedule"
category: cloudngfw
scope: global
---

# set cngfw schedules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a schedule

## Usage

```
set cngfw schedules [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw schedules
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw schedules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw schedules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
