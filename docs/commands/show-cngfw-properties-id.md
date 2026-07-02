---
command: "show cngfw properties id"
description: "Get a property"
category: cloudngfw
scope: global
---

# show cngfw properties id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a property

## Usage

```
show cngfw properties id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw properties id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw properties id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw properties id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
