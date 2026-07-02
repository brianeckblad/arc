---
command: "show cngfw hip-objects"
description: "List HIP objects"
category: cloudngfw
scope: global
---

# show cngfw hip-objects

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List HIP objects

## Usage

```
show cngfw hip-objects [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw hip-objects
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw hip-objects --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw hip-objects
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
