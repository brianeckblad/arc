---
command: "delete qos-profiles"
description: "Delete a QoS profile"
category: network
scope: global
---

# delete qos-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a QoS profile

## Usage

```
delete qos-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete qos-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete qos-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete qos-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
