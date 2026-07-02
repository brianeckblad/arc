---
command: "update cngfw labels"
description: "Update a label"
category: cloudngfw
scope: global
---

# update cngfw labels

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a label

## Usage

```
update cngfw labels [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw labels
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw labels --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw labels
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
