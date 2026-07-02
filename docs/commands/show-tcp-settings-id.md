---
command: "show tcp-settings id"
description: "Get existing TCP settings"
category: device-device-settings
scope: global
---

# show tcp-settings id

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get existing TCP settings

## Usage

```
show tcp-settings id [--remote]
```

## Examples

Run via SCM API:
```
arc > show tcp-settings id
```

Run directly on device via SSH:
```
arc:fw-01 > show tcp-settings id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show tcp-settings id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
