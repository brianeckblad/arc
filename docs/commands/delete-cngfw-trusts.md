---
command: "delete cngfw trusts"
description: "Delete a Trust"
category: cloudngfw
scope: global
---

# delete cngfw trusts

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a Trust

## Usage

```
delete cngfw trusts [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw trusts
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw trusts --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw trusts
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
