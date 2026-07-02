---
command: "set adnsr internal-domains"
description: "Create a custom internal domain"
category: adnsr
scope: global
---

# set adnsr internal-domains

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a custom internal domain

## Usage

```
set adnsr internal-domains [--remote]
```

## Examples

Run via SCM API:
```
arc > set adnsr internal-domains
```

Run directly on device via SSH:
```
arc:fw-01 > set adnsr internal-domains --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set adnsr internal-domains
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
