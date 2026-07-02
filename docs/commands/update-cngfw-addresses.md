---
command: "update cngfw addresses"
description: "Update an address"
category: cloudngfw
scope: global
---

# update cngfw addresses

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an address

## Usage

```
update cngfw addresses [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw addresses
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw addresses --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw addresses
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
