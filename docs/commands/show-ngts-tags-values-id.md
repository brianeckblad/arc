---
command: "show ngts tags values id"
description: "Retrieve values for a tag"
category: ngts
scope: global
---

# show ngts tags values id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve values for a tag

## Usage

```
show ngts tags values id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts tags values id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts tags values id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts tags values id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
