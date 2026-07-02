---
command: "update aggregate-interfaces"
description: "Update an Aggregate Interface"
category: network
scope: global
---

# update aggregate-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an Aggregate Interface

## Usage

```
update aggregate-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > update aggregate-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > update aggregate-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update aggregate-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
