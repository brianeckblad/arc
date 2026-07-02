---
command: "set cngfw hip-objects"
description: "Create a HIP object"
category: cloudngfw
scope: global
---

# set cngfw hip-objects

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a HIP object

## Usage

```
set cngfw hip-objects [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw hip-objects
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw hip-objects --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw hip-objects
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
