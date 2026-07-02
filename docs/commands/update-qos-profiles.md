---
command: "update qos-profiles"
description: "Update a QoS profile"
category: network
scope: global
---

# update qos-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a QoS profile

## Usage

```
update qos-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update qos-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update qos-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update qos-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
