---
command: "set jobs device-interfaces"
description: "Initiate a job to retrieve network interfaces from device(s)"
category: operations
scope: global
---

# set jobs device-interfaces

**Category:** operations
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Initiate a job to retrieve network interfaces from device(s)

## Usage

```
set jobs device-interfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > set jobs device-interfaces
```

Run directly on device via SSH:
```
arc:fw-01 > set jobs device-interfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set jobs device-interfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
