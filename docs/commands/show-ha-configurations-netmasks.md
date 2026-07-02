---
command: "show ha-configurations-netmasks"
description: "Autocomplete HA netmasks"
category: device-device-settings
scope: global
---

# show ha-configurations-netmasks

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Autocomplete HA netmasks

## Usage

```
show ha-configurations-netmasks [--remote]
```

## Examples

Run via SCM API:
```
arc > show ha-configurations-netmasks
```

Run directly on device via SSH:
```
arc:fw-01 > show ha-configurations-netmasks --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ha-configurations-netmasks
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
