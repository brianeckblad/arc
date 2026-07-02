---
command: "show cngfw regions"
description: "List regions"
category: cloudngfw
scope: global
---

# show cngfw regions

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List regions

## Usage

```
show cngfw regions [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw regions
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw regions --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw regions
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
