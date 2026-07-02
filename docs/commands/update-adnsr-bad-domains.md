---
command: "update adnsr bad-domains"
description: "Update a misconfigured domain"
category: adnsr
scope: global
---

# update adnsr bad-domains

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a misconfigured domain

## Usage

```
update adnsr bad-domains [--remote]
```

## Examples

Run via SCM API:
```
arc > update adnsr bad-domains
```

Run directly on device via SSH:
```
arc:fw-01 > update adnsr bad-domains --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update adnsr bad-domains
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
