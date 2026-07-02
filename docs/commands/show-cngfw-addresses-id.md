---
command: "show cngfw addresses id"
description: "Get an address"
category: cloudngfw
scope: global
---

# show cngfw addresses id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an address

## Usage

```
show cngfw addresses id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw addresses id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw addresses id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw addresses id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
