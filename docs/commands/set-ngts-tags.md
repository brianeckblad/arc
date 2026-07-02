---
command: "set ngts tags"
description: "Create a tag"
category: ngts
scope: global
---

# set ngts tags

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a tag

## Usage

```
set ngts tags [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts tags
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts tags --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts tags
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
