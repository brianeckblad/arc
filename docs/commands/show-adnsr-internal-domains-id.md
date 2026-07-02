---
command: "show adnsr internal-domains id"
description: "Get an internal domain"
category: adnsr
scope: global
---

# show adnsr internal-domains id

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an internal domain

## Usage

```
show adnsr internal-domains id [--remote]
```

## Examples

Run via SCM API:
```
arc > show adnsr internal-domains id
```

Run directly on device via SSH:
```
arc:fw-01 > show adnsr internal-domains id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show adnsr internal-domains id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
