---
command: "set qos-profiles"
description: "Create a QoS profile"
category: network
scope: global
---

# set qos-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a QoS profile

## Usage

```
set qos-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set qos-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set qos-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set qos-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
