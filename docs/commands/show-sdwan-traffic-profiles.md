---
command: "show sdwan-traffic-profiles"
description: "List SD-WAN traffic distribution profiles"
category: network
scope: global
---

# show sdwan-traffic-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List SD-WAN traffic distribution profiles

## Usage

```
show sdwan-traffic-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show sdwan-traffic-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show sdwan-traffic-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sdwan-traffic-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
