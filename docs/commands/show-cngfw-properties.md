---
command: "show cngfw properties"
description: "List properties"
category: cloudngfw
scope: global
---

# show cngfw properties

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List properties

## Usage

```
show cngfw properties [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw properties
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw properties --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw properties
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
