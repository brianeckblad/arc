---
command: "show qos-profiles id"
description: "Get a QoS profile"
category: network
scope: global
---

# show qos-profiles id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a QoS profile

## Usage

```
show qos-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show qos-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show qos-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show qos-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
