---
command: "show cngfw hip-objects id"
description: "Get a HIP object"
category: cloudngfw
scope: global
---

# show cngfw hip-objects id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a HIP object

## Usage

```
show cngfw hip-objects id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw hip-objects id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw hip-objects id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw hip-objects id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
