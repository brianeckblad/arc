---
command: "update ike-gateways"
description: "Update an IKE gateway"
category: network
scope: global
---

# update ike-gateways

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an IKE gateway

## Usage

```
update ike-gateways [--remote]
```

## Examples

Run via SCM API:
```
arc > update ike-gateways
```

Run directly on device via SSH:
```
arc:fw-01 > update ike-gateways --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ike-gateways
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
