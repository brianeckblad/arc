---
command: "set qos-policy-rules move"
description: "Move a QoS policy rule"
category: network
scope: global
---

# set qos-policy-rules move

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Move a QoS policy rule

## Usage

```
set qos-policy-rules move [--remote]
```

## Examples

Run via SCM API:
```
arc > set qos-policy-rules move
```

Run directly on device via SSH:
```
arc:fw-01 > set qos-policy-rules move --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set qos-policy-rules move
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
