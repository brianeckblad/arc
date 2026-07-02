---
command: "show cngfw regions id"
description: "Get a region"
category: cloudngfw
scope: global
---

# show cngfw regions id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a region

## Usage

```
show cngfw regions id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw regions id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw regions id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw regions id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
