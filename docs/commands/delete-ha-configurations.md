---
command: "delete ha-configurations"
description: "Delete high availability configuration"
category: device-device-settings
scope: global
---

# delete ha-configurations

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete high availability configuration

## Usage

```
delete ha-configurations [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ha-configurations
```

Run directly on device via SSH:
```
arc:fw-01 > delete ha-configurations --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ha-configurations
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
