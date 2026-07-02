---
command: "update ipsec-crypto-profiles"
description: "Update an IPsec crypto profile"
category: network
scope: global
---

# update ipsec-crypto-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an IPsec crypto profile

## Usage

```
update ipsec-crypto-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update ipsec-crypto-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update ipsec-crypto-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ipsec-crypto-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
