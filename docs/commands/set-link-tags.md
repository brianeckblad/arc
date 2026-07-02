---
command: "set link-tags"
description: "Create a link tag"
category: network
scope: global
---

# set link-tags

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a link tag

## Usage

```
set link-tags [--remote]
```

## Examples

Run via SCM API:
```
arc > set link-tags
```

Run directly on device via SSH:
```
arc:fw-01 > set link-tags --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set link-tags
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
