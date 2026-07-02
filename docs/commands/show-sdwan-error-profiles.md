---
command: "show sdwan-error-profiles"
description: "List SD-WAN error correction profiles"
category: network
scope: global
---

# show sdwan-error-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List SD-WAN error correction profiles

## Usage

```
show sdwan-error-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show sdwan-error-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show sdwan-error-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sdwan-error-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
