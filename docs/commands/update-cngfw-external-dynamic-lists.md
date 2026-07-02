---
command: "update cngfw external-dynamic-lists"
description: "Update an External Dynamic List"
category: cloudngfw
scope: global
---

# update cngfw external-dynamic-lists

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an External Dynamic List

## Usage

```
update cngfw external-dynamic-lists [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw external-dynamic-lists
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw external-dynamic-lists --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw external-dynamic-lists
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
