---
command: "show management-interface"
description: "List management interface settings"
category: device-device-settings
scope: global
---

# show management-interface

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List management interface settings

## Usage

```
show management-interface [--remote]
```

## Examples

Run via SCM API:
```
arc > show management-interface
```

Run directly on device via SSH:
```
arc:fw-01 > show management-interface --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show management-interface
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
