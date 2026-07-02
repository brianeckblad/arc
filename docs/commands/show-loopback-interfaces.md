---
command: "show loopback-interfaces"
description: "List loopback interfaces"
category: network
scope: global
---

# show loopback-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List loopback interfaces

## Usage

```
show loopback-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > show loopback-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > show loopback-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show loopback-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
