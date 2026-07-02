---
command: "update ipsec-tunnels"
description: "Update an IPsec tunnel"
category: network
scope: global
---

# update ipsec-tunnels

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an IPsec tunnel

## Usage

```
update ipsec-tunnels [--remote]
```

## Examples

Run via SCM API:
```
arc > update ipsec-tunnels
```

Run directly on device via SSH:
```
arc:fw-01 > update ipsec-tunnels --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ipsec-tunnels
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
