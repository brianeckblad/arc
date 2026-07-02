---
command: "show ipsec-crypto-profiles id"
description: "Get an IPsec crypto profile"
category: network
scope: global
---

# show ipsec-crypto-profiles id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an IPsec crypto profile

## Usage

```
show ipsec-crypto-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ipsec-crypto-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show ipsec-crypto-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ipsec-crypto-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
