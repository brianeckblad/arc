---
command: "show ike-crypto-profiles"
description: "List IKE crypto profiles"
category: network
scope: global
---

# show ike-crypto-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List IKE crypto profiles

## Usage

```
show ike-crypto-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show ike-crypto-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show ike-crypto-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ike-crypto-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
