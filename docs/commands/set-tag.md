---
command: "set tag"
description: "Create tag — set tag <name> [color red|green|blue|...] [comments <text>]"
usage: "set tag <name> [color <color>] [comments <text>]"
feature_flag: create_tag
category: objects
scope: folder
api: "POST /config/objects/v1/tags"
---

# set tag

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a tag — set tag <name> [color <color>]

## Usage

```
set tag [--remote]
```

## Examples

Run via SCM API:
```
arc > set tag
```

Run directly on device via SSH:
```
arc:fw-01 > set tag --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set tag
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
