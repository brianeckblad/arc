---
command: "update ethernet-interfaces"
description: "Update an ethernet interface"
category: network
scope: global
---

# update ethernet-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an ethernet interface

## Usage

```
update ethernet-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > update ethernet-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > update ethernet-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ethernet-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
