---
command: "set cngfw properties"
description: "Create a property"
category: cloudngfw
scope: global
---

# set cngfw properties

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a property

## Usage

```
set cngfw properties [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw properties
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw properties --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw properties
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
