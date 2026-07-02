---
command: "set cngfw data-objects"
description: "Create Data Object"
category: cloudngfw
scope: global
---

# set cngfw data-objects

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create Data Object

## Usage

```
set cngfw data-objects [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw data-objects
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw data-objects --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw data-objects
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
