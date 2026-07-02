---
command: "show adnsr bad-domains id"
description: "Get a misconfigured domain"
category: adnsr
scope: global
---

# show adnsr bad-domains id

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a misconfigured domain

## Usage

```
show adnsr bad-domains id [--remote]
```

## Examples

Run via SCM API:
```
arc > show adnsr bad-domains id
```

Run directly on device via SSH:
```
arc:fw-01 > show adnsr bad-domains id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show adnsr bad-domains id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
