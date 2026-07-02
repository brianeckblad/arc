---
command: "update cngfw hip-objects"
description: "Update a HIP object"
category: cloudngfw
scope: global
---

# update cngfw hip-objects

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a HIP object

## Usage

```
update cngfw hip-objects [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw hip-objects
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw hip-objects --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw hip-objects
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
