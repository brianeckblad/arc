---
command: "set ike-gateways"
description: "Create an IKE gateway"
category: network
scope: global
---

# set ike-gateways

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an IKE gateway

## Usage

```
set ike-gateways [--remote]
```

## Examples

Run via SCM API:
```
arc > set ike-gateways
```

Run directly on device via SSH:
```
arc:fw-01 > set ike-gateways --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ike-gateways
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
