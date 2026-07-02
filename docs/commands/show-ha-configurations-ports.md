---
command: "show ha-configurations-ports"
description: "Autocomplete HA ports"
category: device-device-settings
scope: global
---

# show ha-configurations-ports

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Autocomplete HA ports

## Usage

```
show ha-configurations-ports [--remote]
```

## Examples

Run via SCM API:
```
arc > show ha-configurations-ports
```

Run directly on device via SSH:
```
arc:fw-01 > show ha-configurations-ports --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ha-configurations-ports
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
