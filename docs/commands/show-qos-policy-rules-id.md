---
command: "show qos-policy-rules id"
description: "Get a QoS policy rule"
category: network
scope: global
---

# show qos-policy-rules id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a QoS policy rule

## Usage

```
show qos-policy-rules id [--remote]
```

## Examples

Run via SCM API:
```
arc > show qos-policy-rules id
```

Run directly on device via SSH:
```
arc:fw-01 > show qos-policy-rules id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show qos-policy-rules id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
