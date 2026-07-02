---
command: "update motd-banner-settings"
description: "Update login banner settings"
category: device-device-settings
scope: global
---

# update motd-banner-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update login banner settings

## Usage

```
update motd-banner-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > update motd-banner-settings
```

Run directly on device via SSH:
```
arc:fw-01 > update motd-banner-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update motd-banner-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
