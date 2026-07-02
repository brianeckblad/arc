---
command: "delete adnsr internal-domains"
description: "Delete a custom internal domain"
category: adnsr
scope: global
---

# delete adnsr internal-domains

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a custom internal domain

## Usage

```
delete adnsr internal-domains [--remote]
```

## Examples

Run via SCM API:
```
arc > delete adnsr internal-domains
```

Run directly on device via SSH:
```
arc:fw-01 > delete adnsr internal-domains --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete adnsr internal-domains
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
