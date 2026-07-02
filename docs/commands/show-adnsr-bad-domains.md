---
command: "show adnsr bad-domains"
description: "List misconfigured domains"
category: adnsr
scope: global
---

# show adnsr bad-domains

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List misconfigured domains

## Usage

```
show adnsr bad-domains [--remote]
```

## Examples

Run via SCM API:
```
arc > show adnsr bad-domains
```

Run directly on device via SSH:
```
arc:fw-01 > show adnsr bad-domains --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show adnsr bad-domains
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
