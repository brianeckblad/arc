---
command: "show motd-banner-settings"
description: "List login banner settings"
category: device-device-settings
scope: global
---

# show motd-banner-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List login banner settings

## Usage

```
show motd-banner-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > show motd-banner-settings
```

Run directly on device via SSH:
```
arc:fw-01 > show motd-banner-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show motd-banner-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
