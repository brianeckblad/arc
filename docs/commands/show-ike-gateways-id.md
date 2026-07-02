---
command: "show ike-gateways id"
description: "Get an IKE gateway"
category: network
scope: global
---

# show ike-gateways id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an IKE gateway

## Usage

```
show ike-gateways id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ike-gateways id
```

Run directly on device via SSH:
```
arc:fw-01 > show ike-gateways id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ike-gateways id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
