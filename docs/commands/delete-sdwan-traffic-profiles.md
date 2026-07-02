---
command: "delete sdwan-traffic-profiles"
description: "Delete an SD-WAN traffic distribution profile"
category: network
scope: global
---

# delete sdwan-traffic-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an SD-WAN traffic distribution profile

## Usage

```
delete sdwan-traffic-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete sdwan-traffic-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete sdwan-traffic-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete sdwan-traffic-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
