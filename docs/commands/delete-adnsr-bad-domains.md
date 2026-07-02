---
command: "delete adnsr bad-domains"
description: "Delete a misconfigured domain"
category: adnsr
scope: global
---

# delete adnsr bad-domains

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a misconfigured domain

## Usage

```
delete adnsr bad-domains [--remote]
```

## Examples

Run via SCM API:
```
arc > delete adnsr bad-domains
```

Run directly on device via SSH:
```
arc:fw-01 > delete adnsr bad-domains --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete adnsr bad-domains
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
