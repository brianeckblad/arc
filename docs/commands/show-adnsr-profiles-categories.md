---
command: "show adnsr profiles categories"
description: "Get profile categories"
category: adnsr
scope: global
---

# show adnsr profiles categories

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get profile categories

## Usage

```
show adnsr profiles categories [--remote]
```

## Examples

Run via SCM API:
```
arc > show adnsr profiles categories
```

Run directly on device via SSH:
```
arc:fw-01 > show adnsr profiles categories --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show adnsr profiles categories
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
