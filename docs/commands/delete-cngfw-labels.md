---
command: "delete cngfw labels"
description: "Delete a label"
category: cloudngfw
scope: global
---

# delete cngfw labels

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a label

## Usage

```
delete cngfw labels [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw labels
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw labels --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw labels
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
