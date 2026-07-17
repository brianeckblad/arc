---
command: "show tag"
description: "Show tags in the active folder"
usage: "show tag [<name>]"
feature_flag: show_tag
category: objects
scope: folder
api: "GET /config/objects/v1/tags"
---

---
command: "show tag"
description: "Show tags in the active folder"
usage: "show tag [<name>]"
feature_flag: show_tag
category: objects
scope: folder
api: "GET /config/objects/v1/tags"
---

---
command: "show tag"
description: "Show tags in the active folder"
feature_flag: show_tag
category: objects
scope: folder
api: "GET /config/objects/v1/tags"
---

# show tag

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show tags in the active folder

## Usage

```
show tag [--remote]
```

## Examples

Run via SCM API:
```
arc > show tag
```

Run directly on device via SSH:
```
arc:fw-01 > show tag --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show tag
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
