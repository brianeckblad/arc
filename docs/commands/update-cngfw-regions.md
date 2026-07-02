---
command: "update cngfw regions"
description: "Update a region"
category: cloudngfw
scope: global
---

# update cngfw regions

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a region

## Usage

```
update cngfw regions [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw regions
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw regions --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw regions
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
