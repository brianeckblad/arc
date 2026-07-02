---
command: "show auto-vpn-settings"
description: "Get Auto VPN settings"
category: network
scope: global
---

# show auto-vpn-settings

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get Auto VPN settings

## Usage

```
show auto-vpn-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > show auto-vpn-settings
```

Run directly on device via SSH:
```
arc:fw-01 > show auto-vpn-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show auto-vpn-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
