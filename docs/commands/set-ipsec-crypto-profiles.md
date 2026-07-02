---
command: "set ipsec-crypto-profiles"
description: "Create an IPsec crypto profile"
category: network
scope: global
---

# set ipsec-crypto-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an IPsec crypto profile

## Usage

```
set ipsec-crypto-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set ipsec-crypto-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set ipsec-crypto-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ipsec-crypto-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
