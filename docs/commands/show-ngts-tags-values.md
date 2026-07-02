---
command: "show ngts tags values"
description: "Retrieve values for all tags"
category: ngts
scope: global
---

# show ngts tags values

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve values for all tags

## Usage

```
show ngts tags values [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts tags values
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts tags values --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts tags values
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
