---
command: "set aggregate-interfaces"
description: "Create an Aggregate Interface"
category: network
scope: global
---

# set aggregate-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an Aggregate Interface

## Usage

```
set aggregate-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > set aggregate-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > set aggregate-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set aggregate-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
