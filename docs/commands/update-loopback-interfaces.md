---
command: "update loopback-interfaces"
description: "Update a loopback interface"
category: network
scope: global
---

# update loopback-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a loopback interface

## Usage

```
update loopback-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > update loopback-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > update loopback-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update loopback-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
