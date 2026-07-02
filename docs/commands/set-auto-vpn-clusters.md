---
command: "set auto-vpn-clusters"
description: "Create an Auto VPN cluster"
category: network
scope: global
---

# set auto-vpn-clusters

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an Auto VPN cluster

## Usage

```
set auto-vpn-clusters [--remote]
```

## Examples

Run via SCM API:
```
arc > set auto-vpn-clusters
```

Run directly on device via SSH:
```
arc:fw-01 > set auto-vpn-clusters --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set auto-vpn-clusters
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
