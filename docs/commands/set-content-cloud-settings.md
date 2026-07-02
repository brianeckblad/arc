---
command: "set content-cloud-settings"
description: "Create Content Cloud settings"
category: device-device-settings
scope: global
---

# set content-cloud-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create Content Cloud settings

## Usage

```
set content-cloud-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > set content-cloud-settings
```

Run directly on device via SSH:
```
arc:fw-01 > set content-cloud-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set content-cloud-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
