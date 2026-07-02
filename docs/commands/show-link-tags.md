---
command: "show link-tags"
description: "List link tags"
category: network
scope: global
---

# show link-tags

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List link tags

## Usage

```
show link-tags [--remote]
```

## Examples

Run via SCM API:
```
arc > show link-tags
```

Run directly on device via SSH:
```
arc:fw-01 > show link-tags --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show link-tags
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
