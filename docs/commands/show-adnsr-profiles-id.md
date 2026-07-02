---
command: "show adnsr profiles id"
description: "Get a profile"
category: adnsr
scope: global
---

# show adnsr profiles id

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a profile

## Usage

```
show adnsr profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show adnsr profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show adnsr profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show adnsr profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
