---
command: "show ipsec-crypto-profiles"
description: "List IPsec crypto profiles"
category: network
scope: global
---

# show ipsec-crypto-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List IPsec crypto profiles

## Usage

```
show ipsec-crypto-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show ipsec-crypto-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show ipsec-crypto-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ipsec-crypto-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
