---
command: "delete ipsec-tunnels"
description: "Delete an IPsec tunnel"
category: network
scope: global
---

# delete ipsec-tunnels

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an IPsec tunnel

## Usage

```
delete ipsec-tunnels [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ipsec-tunnels
```

Run directly on device via SSH:
```
arc:fw-01 > delete ipsec-tunnels --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ipsec-tunnels
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
