---
command: "update sdwan-error-profiles"
description: "Update an SD-WAN error correction profile"
category: network
scope: global
---

# update sdwan-error-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an SD-WAN error correction profile

## Usage

```
update sdwan-error-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update sdwan-error-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update sdwan-error-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update sdwan-error-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
