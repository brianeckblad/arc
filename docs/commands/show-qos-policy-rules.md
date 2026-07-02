---
command: "show qos-policy-rules"
description: "List QoS policy rules"
category: network
scope: global
---

# show qos-policy-rules

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List QoS policy rules

## Usage

```
show qos-policy-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > show qos-policy-rules
```

Run directly on device via SSH:
```
arc:fw-01 > show qos-policy-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show qos-policy-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
