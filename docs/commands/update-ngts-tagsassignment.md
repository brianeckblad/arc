---
command: "update ngts tagsassignment"
description: "Replace Add Or Delete Tags"
category: ngts
scope: global
---

# update ngts tagsassignment

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Replace Add Or Delete Tags

## Usage

```
update ngts tagsassignment [--remote]
```

## Examples

Run via SCM API:
```
arc > update ngts tagsassignment
```

Run directly on device via SSH:
```
arc:fw-01 > update ngts tagsassignment --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ngts tagsassignment
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
