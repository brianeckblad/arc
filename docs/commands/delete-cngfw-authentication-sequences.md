---
command: "delete cngfw authentication-sequences"
description: "Delete an authentication sequence"
category: cloudngfw
scope: global
---

# delete cngfw authentication-sequences

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an authentication sequence

## Usage

```
delete cngfw authentication-sequences [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw authentication-sequences
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw authentication-sequences --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw authentication-sequences
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
