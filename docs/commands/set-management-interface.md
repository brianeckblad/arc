---
command: "set management-interface"
description: "Create management interface settings"
category: device-device-settings
scope: global
---

# set management-interface

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create management interface settings

## Usage

```
set management-interface [--remote]
```

## Examples

Run via SCM API:
```
arc > set management-interface
```

Run directly on device via SSH:
```
arc:fw-01 > set management-interface --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set management-interface
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
