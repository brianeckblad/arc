---
command: "show device"
description: "Show detail for a device (or 'show device' when cd'd in)"
usage: "show device <hostname>"
feature_flag: show_devices
category: setup
scope: global
api: "GET /config/setup/v1/devices/{id}"
---

# show device

**Category:** setup
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show detail for a device — show device <hostname>  (or just 'show device' when cd'd into one)

## Usage

```
show device [--remote]
```

## Examples

Run via SCM API:
```
arc > show device
```

Run directly on device via SSH:
```
arc:fw-01 > show device --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show device
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
