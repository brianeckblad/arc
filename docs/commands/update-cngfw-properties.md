---
command: "update cngfw properties"
description: "Update a property"
category: cloudngfw
scope: global
---

# update cngfw properties

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a property

## Usage

```
update cngfw properties [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw properties
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw properties --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw properties
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
