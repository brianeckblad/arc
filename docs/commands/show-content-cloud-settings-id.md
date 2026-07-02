---
command: "show content-cloud-settings id"
description: "Get existing Content Cloud settings"
category: device-device-settings
scope: global
---

# show content-cloud-settings id

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get existing Content Cloud settings

## Usage

```
show content-cloud-settings id [--remote]
```

## Examples

Run via SCM API:
```
arc > show content-cloud-settings id
```

Run directly on device via SSH:
```
arc:fw-01 > show content-cloud-settings id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show content-cloud-settings id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
