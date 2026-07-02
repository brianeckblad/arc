---
command: "delete sase fp-user-locations"
description: "Delete a GlobalProtect user location"
category: sase
scope: global
---

# delete sase fp-user-locations

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a GlobalProtect user location

## Usage

```
delete sase fp-user-locations [--remote]
```

## Examples

Run via SCM API:
```
arc > delete sase fp-user-locations
```

Run directly on device via SSH:
```
arc:fw-01 > delete sase fp-user-locations --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete sase fp-user-locations
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
