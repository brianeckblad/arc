---
command: "show ha-configurations"
description: "Get high availability configuration"
category: device-device-settings
scope: global
---

# show ha-configurations

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get high availability configuration

## Usage

```
show ha-configurations [--remote]
```

## Examples

Run via SCM API:
```
arc > show ha-configurations
```

Run directly on device via SSH:
```
arc:fw-01 > show ha-configurations --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ha-configurations
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
