---
command: "set ike-crypto-profiles"
description: "Create an IKE crypto profile"
category: network
scope: global
---

# set ike-crypto-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an IKE crypto profile

## Usage

```
set ike-crypto-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set ike-crypto-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set ike-crypto-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ike-crypto-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
