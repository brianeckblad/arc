---
command: "set cngfw labels"
description: "Create a label"
category: cloudngfw
scope: global
---

# set cngfw labels

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a label

## Usage

```
set cngfw labels [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw labels
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw labels --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw labels
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
