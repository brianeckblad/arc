---
command: "update external-dynamic-list"
description: "Update EDL url/frequency — update external-dynamic-list <name> url <url>"
feature_flag: update_objects
category: objects
scope: folder
api: "PUT /config/objects/v1/external-dynamic-lists/{id}"
---

---
command: "update external-dynamic-list"
description: "Update EDL url/frequency — update external-dynamic-list <name> url <url>"
feature_flag: update_objects
category: objects
scope: folder
api: "PUT /config/objects/v1/external-dynamic-lists/{id}"
---

---
command: "update external-dynamic-list"
description: "Update EDL url/frequency — update external-dynamic-list <name> url <url>"
usage: "update external-dynamic-list <name> url <fetch-url>"
feature_flag: update_objects
category: objects
scope: folder
api: "PUT /config/objects/v1/external-dynamic-lists/{id}"
---

# update external-dynamic-list

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update EDL url/frequency — update external-dynamic-list <name> url <url>

## Usage

```
update external-dynamic-list [--remote]
```

## Examples

Run via SCM API:
```
arc > update external-dynamic-list
```

Run directly on device via SSH:
```
arc:fw-01 > update external-dynamic-list --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update external-dynamic-list
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
