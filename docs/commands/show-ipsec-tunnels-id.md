---
command: "show ipsec-tunnels id"
description: "Get an IPsec tunnel"
category: network
scope: global
---

# show ipsec-tunnels id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an IPsec tunnel

## Usage

```
show ipsec-tunnels id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ipsec-tunnels id
```

Run directly on device via SSH:
```
arc:fw-01 > show ipsec-tunnels id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ipsec-tunnels id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
