---
command: "update ike-crypto-profiles"
description: "Update an IKE crypto profile"
category: network
scope: global
---

# update ike-crypto-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an IKE crypto profile

## Usage

```
update ike-crypto-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update ike-crypto-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update ike-crypto-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ike-crypto-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
