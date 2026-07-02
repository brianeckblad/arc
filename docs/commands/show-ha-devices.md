---
command: "show ha-devices"
description: "List high availability devices"
category: device-device-settings
scope: global
---

# show ha-devices

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List high availability devices

## Usage

```
show ha-devices [--remote]
```

## Examples

Run via SCM API:
```
arc > show ha-devices
```

Run directly on device via SSH:
```
arc:fw-01 > show ha-devices --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ha-devices
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
