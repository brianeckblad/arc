---
command: "set tunnel-interfaces"
description: "Create a tunnel interface"
category: network
scope: global
---

# set tunnel-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a tunnel interface

## Usage

```
set tunnel-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > set tunnel-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > set tunnel-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set tunnel-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
