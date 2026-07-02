---
command: "delete loopback-interfaces"
description: "Delete a loopback interface"
category: network
scope: global
---

# delete loopback-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a loopback interface

## Usage

```
delete loopback-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > delete loopback-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > delete loopback-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete loopback-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
