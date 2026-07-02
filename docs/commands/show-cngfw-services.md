---
command: "show cngfw services"
description: "List services"
category: cloudngfw
scope: global
---

# show cngfw services

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List services

## Usage

```
show cngfw services [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw services
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw services --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw services
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
