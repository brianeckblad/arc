---
command: "update auto-vpn-settings"
description: "Update Auto VPN settings"
category: network
scope: global
---

# update auto-vpn-settings

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update Auto VPN settings

## Usage

```
update auto-vpn-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > update auto-vpn-settings
```

Run directly on device via SSH:
```
arc:fw-01 > update auto-vpn-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update auto-vpn-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
