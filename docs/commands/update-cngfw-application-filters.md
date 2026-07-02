---
command: "update cngfw application-filters"
description: "Update an application filter"
category: cloudngfw
scope: global
---

# update cngfw application-filters

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an application filter

## Usage

```
update cngfw application-filters [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw application-filters
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw application-filters --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw application-filters
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
