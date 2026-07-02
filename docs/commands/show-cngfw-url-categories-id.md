---
command: "show cngfw url-categories id"
description: "Get a custom URL category"
category: cloudngfw
scope: global
---

# show cngfw url-categories id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a custom URL category

## Usage

```
show cngfw url-categories id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw url-categories id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw url-categories id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw url-categories id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
