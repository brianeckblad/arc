---
command: "show cngfw schedules id"
description: "Get a schedule"
category: cloudngfw
scope: global
---

# show cngfw schedules id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a schedule

## Usage

```
show cngfw schedules id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw schedules id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw schedules id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw schedules id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
