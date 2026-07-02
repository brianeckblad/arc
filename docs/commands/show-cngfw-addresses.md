---
command: "show cngfw addresses"
description: "List addresses"
category: cloudngfw
scope: global
---

# show cngfw addresses

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List addresses

## Usage

```
show cngfw addresses [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw addresses
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw addresses --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw addresses
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
