---
command: "delete cngfw schedules"
description: "Delete a schedule"
category: cloudngfw
scope: global
---

# delete cngfw schedules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a schedule

## Usage

```
delete cngfw schedules [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw schedules
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw schedules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw schedules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
