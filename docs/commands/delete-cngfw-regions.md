---
command: "delete cngfw regions"
description: "Delete a region"
category: cloudngfw
scope: global
---

# delete cngfw regions

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a region

## Usage

```
delete cngfw regions [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw regions
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw regions --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw regions
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
