---
command: "set cngfw external-dynamic-lists"
description: "Create an External Dynamic List"
category: cloudngfw
scope: global
---

# set cngfw external-dynamic-lists

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an External Dynamic List

## Usage

```
set cngfw external-dynamic-lists [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw external-dynamic-lists
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw external-dynamic-lists --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw external-dynamic-lists
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
