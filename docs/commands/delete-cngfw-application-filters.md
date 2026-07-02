---
command: "delete cngfw application-filters"
description: "Delete an application filter"
category: cloudngfw
scope: global
---

# delete cngfw application-filters

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an application filter

## Usage

```
delete cngfw application-filters [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw application-filters
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw application-filters --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw application-filters
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
