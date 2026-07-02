---
command: "show ngts tags"
description: "Retrieve all tags"
category: ngts
scope: global
---

# show ngts tags

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve all tags

## Usage

```
show ngts tags [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts tags
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts tags --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts tags
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
