---
command: "delete ipsec-crypto-profiles"
description: "Delete an IPsec crypto profile"
category: network
scope: global
---

# delete ipsec-crypto-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an IPsec crypto profile

## Usage

```
delete ipsec-crypto-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ipsec-crypto-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete ipsec-crypto-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ipsec-crypto-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
