---
command: "show ha-configurations-gateways"
description: "Autocomplete HA gateways"
category: device-device-settings
scope: global
---

# show ha-configurations-gateways

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Autocomplete HA gateways

## Usage

```
show ha-configurations-gateways [--remote]
```

## Examples

Run via SCM API:
```
arc > show ha-configurations-gateways
```

Run directly on device via SSH:
```
arc:fw-01 > show ha-configurations-gateways --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ha-configurations-gateways
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
