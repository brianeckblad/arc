---
command: "delete link-tags"
description: "Delete a link tag"
category: network
scope: global
---

# delete link-tags

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a link tag

## Usage

```
delete link-tags [--remote]
```

## Examples

Run via SCM API:
```
arc > delete link-tags
```

Run directly on device via SSH:
```
arc:fw-01 > delete link-tags --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete link-tags
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
