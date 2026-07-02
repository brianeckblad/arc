---
command: "update ha-configurations"
description: "Update high availability configuration"
category: device-device-settings
scope: global
---

# update ha-configurations

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update high availability configuration

## Usage

```
update ha-configurations [--remote]
```

## Examples

Run via SCM API:
```
arc > update ha-configurations
```

Run directly on device via SSH:
```
arc:fw-01 > update ha-configurations --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ha-configurations
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
