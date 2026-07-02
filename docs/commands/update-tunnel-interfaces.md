---
command: "update tunnel-interfaces"
description: "Update a tunnel interface"
category: network
scope: global
---

# update tunnel-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a tunnel interface

## Usage

```
update tunnel-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > update tunnel-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > update tunnel-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update tunnel-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
