---
command: "show cngfw data-objects"
description: "List Data Objects"
category: cloudngfw
scope: global
---

# show cngfw data-objects

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List Data Objects

## Usage

```
show cngfw data-objects [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw data-objects
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw data-objects --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw data-objects
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
