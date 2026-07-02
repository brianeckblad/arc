---
command: "set ha-configurations"
description: "Create high availability configuration"
category: device-device-settings
scope: global
---

# set ha-configurations

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create high availability configuration

## Usage

```
set ha-configurations [--remote]
```

## Examples

Run via SCM API:
```
arc > set ha-configurations
```

Run directly on device via SSH:
```
arc:fw-01 > set ha-configurations --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ha-configurations
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
