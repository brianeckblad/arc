---
command: "set adnsr conn-sources subnets verify"
description: "Verify a subnet for a connection source"
category: adnsr
scope: global
---

# set adnsr conn-sources subnets verify

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Verify a subnet for a connection source

## Usage

```
set adnsr conn-sources subnets verify [--remote]
```

## Examples

Run via SCM API:
```
arc > set adnsr conn-sources subnets verify
```

Run directly on device via SSH:
```
arc:fw-01 > set adnsr conn-sources subnets verify --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set adnsr conn-sources subnets verify
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
