---
command: "set zones"
description: "Create a security zone"
category: network
scope: global
---

# set zones

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a security zone

## Usage

```
set zones [--remote]
```

## Examples

Run via SCM API:
```
arc > set zones
```

Run directly on device via SSH:
```
arc:fw-01 > set zones --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set zones
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
