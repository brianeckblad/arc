---
command: "delete tag"
description: "Delete a tag — delete tag <name>"
usage: "delete tag <name>"
feature_flag: delete_objects
category: objects
scope: folder
api: "DELETE /config/objects/v1/tags/{id}"
---

# delete tag

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a tag — delete tag <name>

## Usage

```
delete tag [--remote]
```

## Examples

Run via SCM API:
```
arc > delete tag
```

Run directly on device via SSH:
```
arc:fw-01 > delete tag --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete tag
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
