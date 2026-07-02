---
command: "show cdug user-attr-values"
description: "Retrieve User Attribute Values"
category: cdug
scope: global
---

# show cdug user-attr-values

**Category:** cdug
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve User Attribute Values

## Usage

```
show cdug user-attr-values [--remote]
```

## Examples

Run via SCM API:
```
arc > show cdug user-attr-values
```

Run directly on device via SSH:
```
arc:fw-01 > show cdug user-attr-values --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cdug user-attr-values
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
