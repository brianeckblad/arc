---
command: "show ha-configurations-ip-addresses"
description: "Autocomplete HA IP addresses"
category: device-device-settings
scope: global
---

# show ha-configurations-ip-addresses

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Autocomplete HA IP addresses

## Usage

```
show ha-configurations-ip-addresses [--remote]
```

## Examples

Run via SCM API:
```
arc > show ha-configurations-ip-addresses
```

Run directly on device via SSH:
```
arc:fw-01 > show ha-configurations-ip-addresses --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ha-configurations-ip-addresses
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
