---
command: "update content-cloud-settings"
description: "Update Content Cloud settings"
category: device-device-settings
scope: global
---

# update content-cloud-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update Content Cloud settings

## Usage

```
update content-cloud-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > update content-cloud-settings
```

Run directly on device via SSH:
```
arc:fw-01 > update content-cloud-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update content-cloud-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
