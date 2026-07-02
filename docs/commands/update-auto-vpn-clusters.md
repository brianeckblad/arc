---
command: "update auto-vpn-clusters"
description: "Update an Auto VPN cluster"
category: network
scope: global
---

# update auto-vpn-clusters

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an Auto VPN cluster

## Usage

```
update auto-vpn-clusters [--remote]
```

## Examples

Run via SCM API:
```
arc > update auto-vpn-clusters
```

Run directly on device via SSH:
```
arc:fw-01 > update auto-vpn-clusters --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update auto-vpn-clusters
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
