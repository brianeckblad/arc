---
command: "delete aggregate-interfaces"
description: "Delete an Aggregate Interface"
category: network
scope: global
---

# delete aggregate-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an Aggregate Interface

## Usage

```
delete aggregate-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > delete aggregate-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > delete aggregate-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete aggregate-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
