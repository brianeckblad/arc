---
command: "set adnsr bad-domains"
description: "Create a misconfigured domain"
category: adnsr
scope: global
---

# set adnsr bad-domains

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a misconfigured domain

## Usage

```
set adnsr bad-domains [--remote]
```

## Examples

Run via SCM API:
```
arc > set adnsr bad-domains
```

Run directly on device via SSH:
```
arc:fw-01 > set adnsr bad-domains --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set adnsr bad-domains
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
