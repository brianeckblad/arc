---
command: "set ipsec-tunnels"
description: "Create an IPsec tunnel"
category: network
scope: global
---

# set ipsec-tunnels

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an IPsec tunnel

## Usage

```
set ipsec-tunnels [--remote]
```

## Examples

Run via SCM API:
```
arc > set ipsec-tunnels
```

Run directly on device via SSH:
```
arc:fw-01 > set ipsec-tunnels --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ipsec-tunnels
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
