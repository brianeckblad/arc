---
command: "delete ethernet-interfaces"
description: "Delete an ethernet interface"
category: network
scope: global
---

# delete ethernet-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an ethernet interface

## Usage

```
delete ethernet-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ethernet-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > delete ethernet-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ethernet-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
