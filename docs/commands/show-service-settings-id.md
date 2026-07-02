---
command: "show service-settings id"
description: "Get existing service settings"
category: device-device-settings
scope: global
---

# show service-settings id

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get existing service settings

## Usage

```
show service-settings id [--remote]
```

## Examples

Run via SCM API:
```
arc > show service-settings id
```

Run directly on device via SSH:
```
arc:fw-01 > show service-settings id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show service-settings id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
