---
command: "show general-settings id"
description: "Get existing general settings"
category: device-device-settings
scope: global
---

# show general-settings id

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get existing general settings

## Usage

```
show general-settings id [--remote]
```

## Examples

Run via SCM API:
```
arc > show general-settings id
```

Run directly on device via SSH:
```
arc:fw-01 > show general-settings id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show general-settings id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
