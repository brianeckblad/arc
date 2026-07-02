---
command: "set sdwan-path-profiles"
description: "Create an SD-WAN path quality profile"
category: network
scope: global
---

# set sdwan-path-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an SD-WAN path quality profile

## Usage

```
set sdwan-path-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set sdwan-path-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set sdwan-path-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set sdwan-path-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
