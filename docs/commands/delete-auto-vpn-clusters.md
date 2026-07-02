---
command: "delete auto-vpn-clusters"
description: "Delete an Auto VPN cluster"
category: network
scope: global
---

# delete auto-vpn-clusters

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an Auto VPN cluster

## Usage

```
delete auto-vpn-clusters [--remote]
```

## Examples

Run via SCM API:
```
arc > delete auto-vpn-clusters
```

Run directly on device via SSH:
```
arc:fw-01 > delete auto-vpn-clusters --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete auto-vpn-clusters
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
