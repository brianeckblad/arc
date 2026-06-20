---
command: "update address-group"
description: "Update address group — update address-group <name> static <m1>... | dynamic filter '<expr>'"
usage: "update address-group <name> static|dynamic <value> [description <text>]"
feature_flag: update_objects
category: objects
scope: folder
api: "PUT /config/objects/v1/address-groups/{id}"
---

# update address-group

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update address group — update address-group <name> static <m1>... | dynamic filter '<expr>'

## Usage

```
update address-group [--remote]
```

## Examples

Run via SCM API:
```
arc > update address-group
```

Run directly on device via SSH:
```
arc:fw-01 > update address-group --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update address-group
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
