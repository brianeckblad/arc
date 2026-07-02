---
command: "update qos-policy-rules"
description: "Update a QoS policy rule"
category: network
scope: global
---

# update qos-policy-rules

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a QoS policy rule

## Usage

```
update qos-policy-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > update qos-policy-rules
```

Run directly on device via SSH:
```
arc:fw-01 > update qos-policy-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update qos-policy-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
