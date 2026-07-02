---
command: "show cngfw external-dynamic-lists"
description: "List External Dynamic Lists"
category: cloudngfw
scope: global
---

# show cngfw external-dynamic-lists

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List External Dynamic Lists

## Usage

```
show cngfw external-dynamic-lists [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw external-dynamic-lists
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw external-dynamic-lists --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw external-dynamic-lists
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
