---
command: "delete management-interface"
description: "Delete management interface settings"
category: device-device-settings
scope: global
---

# delete management-interface

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete management interface settings

## Usage

```
delete management-interface [--remote]
```

## Examples

Run via SCM API:
```
arc > delete management-interface
```

Run directly on device via SSH:
```
arc:fw-01 > delete management-interface --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete management-interface
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
