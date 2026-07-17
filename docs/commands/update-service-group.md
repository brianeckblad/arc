---
command: "update service-group"
description: "Update service group members — update service-group <name> members <svc1> [svc2...]"
feature_flag: update_objects
category: objects
scope: folder
api: "PUT /config/objects/v1/service-groups/{id}"
---

---
command: "update service-group"
description: "Update service group members — update service-group <name> members <svc1> [svc2...]"
feature_flag: update_objects
category: objects
scope: folder
api: "PUT /config/objects/v1/service-groups/{id}"
---

---
command: "update service-group"
description: "Update service group members — update service-group <name> members <svc1> [svc2...]"
usage: "update service-group <name> members <svc1> [svc2 ...]"
feature_flag: update_objects
category: objects
scope: folder
api: "PUT /config/objects/v1/service-groups/{id}"
---

# update service-group

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update service group members — update service-group <name> members <svc1> [svc2...]

## Usage

```
update service-group [--remote]
```

## Examples

Run via SCM API:
```
arc > update service-group
```

Run directly on device via SSH:
```
arc:fw-01 > update service-group --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update service-group
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
