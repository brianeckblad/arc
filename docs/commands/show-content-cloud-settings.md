---
command: "show content-cloud-settings"
description: "List Content Cloud settings"
category: device-device-settings
scope: global
---

# show content-cloud-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List Content Cloud settings

## Usage

```
show content-cloud-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > show content-cloud-settings
```

Run directly on device via SSH:
```
arc:fw-01 > show content-cloud-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show content-cloud-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
