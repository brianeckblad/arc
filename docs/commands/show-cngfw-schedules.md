---
command: "show cngfw schedules"
description: "List schedules"
category: cloudngfw
scope: global
---

# show cngfw schedules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List schedules

## Usage

```
show cngfw schedules [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw schedules
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw schedules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw schedules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
