---
command: "delete qos-policy-rules"
description: "Delete a QoS policy rule"
category: network
scope: global
---

# delete qos-policy-rules

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a QoS policy rule

## Usage

```
delete qos-policy-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > delete qos-policy-rules
```

Run directly on device via SSH:
```
arc:fw-01 > delete qos-policy-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete qos-policy-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
