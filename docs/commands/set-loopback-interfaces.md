---
command: "set loopback-interfaces"
description: "Create a loopback interface"
category: network
scope: global
---

# set loopback-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a loopback interface

## Usage

```
set loopback-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > set loopback-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > set loopback-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set loopback-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
