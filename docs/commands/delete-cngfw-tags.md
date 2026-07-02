---
command: "delete cngfw tags"
description: "Delete a tag"
category: cloudngfw
scope: global
---

# delete cngfw tags

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a tag

## Usage

```
delete cngfw tags [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw tags
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw tags --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw tags
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
