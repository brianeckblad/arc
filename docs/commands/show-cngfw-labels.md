---
command: "show cngfw labels"
description: "List labels"
category: cloudngfw
scope: global
---

# show cngfw labels

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List labels

## Usage

```
show cngfw labels [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw labels
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw labels --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw labels
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
