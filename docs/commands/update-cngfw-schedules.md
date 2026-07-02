---
command: "update cngfw schedules"
description: "Update a schedule"
category: cloudngfw
scope: global
---

# update cngfw schedules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a schedule

## Usage

```
update cngfw schedules [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw schedules
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw schedules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw schedules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
