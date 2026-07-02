---
command: "set cngfw regions"
description: "Create a region"
category: cloudngfw
scope: global
---

# set cngfw regions

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a region

## Usage

```
set cngfw regions [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw regions
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw regions --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw regions
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
