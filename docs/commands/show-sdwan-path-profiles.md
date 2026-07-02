---
command: "show sdwan-path-profiles"
description: "List SD-WAN path quality profiles"
category: network
scope: global
---

# show sdwan-path-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List SD-WAN path quality profiles

## Usage

```
show sdwan-path-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show sdwan-path-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show sdwan-path-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sdwan-path-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
