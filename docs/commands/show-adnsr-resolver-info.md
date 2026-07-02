---
command: "show adnsr resolver-info"
description: "Get resolver information"
category: adnsr
scope: global
---

# show adnsr resolver-info

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get resolver information

## Usage

```
show adnsr resolver-info [--remote]
```

## Examples

Run via SCM API:
```
arc > show adnsr resolver-info
```

Run directly on device via SSH:
```
arc:fw-01 > show adnsr resolver-info --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show adnsr resolver-info
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
