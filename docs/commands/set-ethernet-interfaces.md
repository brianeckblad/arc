---
command: "set ethernet-interfaces"
description: "Create an ethernet interface"
category: network
scope: global
---

# set ethernet-interfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an ethernet interface

## Usage

```
set ethernet-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > set ethernet-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > set ethernet-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ethernet-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
