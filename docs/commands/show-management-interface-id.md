---
command: "show management-interface id"
description: "Get existing management interface settings"
category: device-device-settings
scope: global
---

# show management-interface id

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get existing management interface settings

## Usage

```
show management-interface id [--remote]
```

## Examples

Run via SCM API:
```
arc > show management-interface id
```

Run directly on device via SSH:
```
arc:fw-01 > show management-interface id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show management-interface id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
