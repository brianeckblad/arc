---
command: "update link-tags"
description: "Update a link tag"
category: network
scope: global
---

# update link-tags

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a link tag

## Usage

```
update link-tags [--remote]
```

## Examples

Run via SCM API:
```
arc > update link-tags
```

Run directly on device via SSH:
```
arc:fw-01 > update link-tags --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update link-tags
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
