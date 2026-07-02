---
command: "show cngfw application-filters"
description: "List application filters"
category: cloudngfw
scope: global
---

# show cngfw application-filters

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List application filters

## Usage

```
show cngfw application-filters [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw application-filters
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw application-filters --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw application-filters
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
