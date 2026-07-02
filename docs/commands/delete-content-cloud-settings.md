---
command: "delete content-cloud-settings"
description: "Delete Content Cloud settings"
category: device-device-settings
scope: global
---

# delete content-cloud-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete Content Cloud settings

## Usage

```
delete content-cloud-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > delete content-cloud-settings
```

Run directly on device via SSH:
```
arc:fw-01 > delete content-cloud-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete content-cloud-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
