---
command: "update content-id-settings"
description: "Update Content-ID settings"
category: device-device-settings
scope: global
---

# update content-id-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update Content-ID settings

## Usage

```
update content-id-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > update content-id-settings
```

Run directly on device via SSH:
```
arc:fw-01 > update content-id-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update content-id-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
