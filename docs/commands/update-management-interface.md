---
command: "update management-interface"
description: "Update management interface settings"
category: device-device-settings
scope: global
---

# update management-interface

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update management interface settings

## Usage

```
update management-interface [--remote]
```

## Examples

Run via SCM API:
```
arc > update management-interface
```

Run directly on device via SSH:
```
arc:fw-01 > update management-interface --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update management-interface
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
