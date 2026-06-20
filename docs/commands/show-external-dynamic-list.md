---
command: "show external-dynamic-list"
description: "Show external dynamic lists (EDLs) in the active folder"
feature_flag: show_external_dynamic_list
category: objects
scope: folder
api: "GET /config/objects/v1/external-dynamic-lists"
---

# show external-dynamic-list

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show external dynamic lists (EDLs) in the active folder

## Usage

```
show external-dynamic-list [--remote]
```

## Examples

Run via SCM API:
```
arc > show external-dynamic-list
```

Run directly on device via SSH:
```
arc:fw-01 > show external-dynamic-list --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show external-dynamic-list
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
