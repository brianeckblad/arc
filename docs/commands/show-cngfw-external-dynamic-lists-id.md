---
command: "show cngfw external-dynamic-lists id"
description: "Get an External Dynamic List"
category: cloudngfw
scope: global
---

# show cngfw external-dynamic-lists id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an External Dynamic List

## Usage

```
show cngfw external-dynamic-lists id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw external-dynamic-lists id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw external-dynamic-lists id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw external-dynamic-lists id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
