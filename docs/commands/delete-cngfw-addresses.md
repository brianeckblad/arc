---
command: "delete cngfw addresses"
description: "Delete an address"
category: cloudngfw
scope: global
---

# delete cngfw addresses

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an address

## Usage

```
delete cngfw addresses [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw addresses
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw addresses --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw addresses
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
