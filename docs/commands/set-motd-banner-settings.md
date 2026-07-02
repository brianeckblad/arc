---
command: "set motd-banner-settings"
description: "Create login banner settings"
category: device-device-settings
scope: global
---

# set motd-banner-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create login banner settings

## Usage

```
set motd-banner-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > set motd-banner-settings
```

Run directly on device via SSH:
```
arc:fw-01 > set motd-banner-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set motd-banner-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
