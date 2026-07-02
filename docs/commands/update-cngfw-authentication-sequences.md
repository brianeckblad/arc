---
command: "update cngfw authentication-sequences"
description: "Update an authentication sequence"
category: cloudngfw
scope: global
---

# update cngfw authentication-sequences

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an authentication sequence

## Usage

```
update cngfw authentication-sequences [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw authentication-sequences
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw authentication-sequences --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw authentication-sequences
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
