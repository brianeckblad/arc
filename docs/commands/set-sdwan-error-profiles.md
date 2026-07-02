---
command: "set sdwan-error-profiles"
description: "Create an SD-WAN error correction profile"
category: network
scope: global
---

# set sdwan-error-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an SD-WAN error correction profile

## Usage

```
set sdwan-error-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set sdwan-error-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set sdwan-error-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set sdwan-error-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
