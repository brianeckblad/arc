---
command: "show service-route id"
description: "Get existing service route settings"
category: device-device-settings
scope: global
---

# show service-route id

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get existing service route settings

## Usage

```
show service-route id [--remote]
```

## Examples

Run via SCM API:
```
arc > show service-route id
```

Run directly on device via SSH:
```
arc:fw-01 > show service-route id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show service-route id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
