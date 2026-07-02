---
command: "update adnsr internal-domains"
description: "Update a custom internal domain"
category: adnsr
scope: global
---

# update adnsr internal-domains

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a custom internal domain

## Usage

```
update adnsr internal-domains [--remote]
```

## Examples

Run via SCM API:
```
arc > update adnsr internal-domains
```

Run directly on device via SSH:
```
arc:fw-01 > update adnsr internal-domains --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update adnsr internal-domains
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
