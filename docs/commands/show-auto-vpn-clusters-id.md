---
command: "show auto-vpn-clusters id"
description: "Get an Auto VPN cluster"
category: network
scope: global
---

# show auto-vpn-clusters id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an Auto VPN cluster

## Usage

```
show auto-vpn-clusters id [--remote]
```

## Examples

Run via SCM API:
```
arc > show auto-vpn-clusters id
```

Run directly on device via SSH:
```
arc:fw-01 > show auto-vpn-clusters id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show auto-vpn-clusters id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
