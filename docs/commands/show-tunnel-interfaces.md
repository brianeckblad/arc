---
command: "show tunnel-interfaces"
description: "List tunnel interfaces"
category: network
scope: global
---

# show tunnel-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List tunnel interfaces

## Usage

```
show tunnel-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > show tunnel-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > show tunnel-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show tunnel-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
