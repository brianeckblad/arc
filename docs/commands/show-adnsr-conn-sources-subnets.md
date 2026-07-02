---
command: "show adnsr conn-sources subnets"
description: "List Subnets"
category: adnsr
scope: global
---

# show adnsr conn-sources subnets

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List Subnets

## Usage

```
show adnsr conn-sources subnets [--remote]
```

## Examples

Run via SCM API:
```
arc > show adnsr conn-sources subnets
```

Run directly on device via SSH:
```
arc:fw-01 > show adnsr conn-sources subnets --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show adnsr conn-sources subnets
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
