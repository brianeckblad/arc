---
command: "delete tunnel-interfaces"
description: "Delete a tunnel interface"
category: network
scope: global
---

# delete tunnel-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a tunnel interface

## Usage

```
delete tunnel-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > delete tunnel-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > delete tunnel-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete tunnel-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
