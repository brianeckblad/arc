---
command: "show cngfw url-categories"
description: "List custom URL categories"
category: cloudngfw
scope: global
---

# show cngfw url-categories

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List custom URL categories

## Usage

```
show cngfw url-categories [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw url-categories
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw url-categories --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw url-categories
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
