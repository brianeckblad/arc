---
command: "delete adnsr conn-sources subnets"
description: "Delete a Connection Source Subnet"
category: adnsr
scope: global
---

# delete adnsr conn-sources subnets

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a Connection Source Subnet

## Usage

```
delete adnsr conn-sources subnets [--remote]
```

## Examples

Run via SCM API:
```
arc > delete adnsr conn-sources subnets
```

Run directly on device via SSH:
```
arc:fw-01 > delete adnsr conn-sources subnets --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete adnsr conn-sources subnets
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
