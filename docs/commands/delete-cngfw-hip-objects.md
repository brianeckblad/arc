---
command: "delete cngfw hip-objects"
description: "Delete a HIP object"
category: cloudngfw
scope: global
---

# delete cngfw hip-objects

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a HIP object

## Usage

```
delete cngfw hip-objects [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw hip-objects
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw hip-objects --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw hip-objects
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
