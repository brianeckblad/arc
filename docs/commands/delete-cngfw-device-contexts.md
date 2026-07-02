---
command: "delete cngfw device-contexts"
description: "Delete device context segments by name"
category: cloudngfw
scope: global
---

# delete cngfw device-contexts

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete device context segments by name

## Usage

```
delete cngfw device-contexts [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw device-contexts
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw device-contexts --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw device-contexts
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
