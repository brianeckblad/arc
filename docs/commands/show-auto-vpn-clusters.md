---
command: "show auto-vpn-clusters"
description: "List Auto VPN clusters"
category: network
scope: global
---

# show auto-vpn-clusters

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List Auto VPN clusters

## Usage

```
show auto-vpn-clusters [--remote]
```

## Examples

Run via SCM API:
```
arc > show auto-vpn-clusters
```

Run directly on device via SSH:
```
arc:fw-01 > show auto-vpn-clusters --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show auto-vpn-clusters
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
