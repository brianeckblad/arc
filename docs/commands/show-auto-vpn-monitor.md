---
command: "show auto-vpn-monitor"
description: "Get Auto VPN status"
category: network
scope: global
---

# show auto-vpn-monitor

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get Auto VPN status

## Usage

```
show auto-vpn-monitor [--remote]
```

## Examples

Run via SCM API:
```
arc > show auto-vpn-monitor
```

Run directly on device via SSH:
```
arc:fw-01 > show auto-vpn-monitor --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show auto-vpn-monitor
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
