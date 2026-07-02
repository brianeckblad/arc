---
command: "set auto-vpn-push"
description: "Push Auto VPN configs"
category: network
scope: global
---

# set auto-vpn-push

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Push Auto VPN configs

## Usage

```
set auto-vpn-push [--remote]
```

## Examples

Run via SCM API:
```
arc > set auto-vpn-push
```

Run directly on device via SSH:
```
arc:fw-01 > set auto-vpn-push --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set auto-vpn-push
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
