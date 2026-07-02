---
command: "show sase fp-user-locations"
description: "List GlobalProtect user locations"
category: sase
scope: global
---

# show sase fp-user-locations

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List GlobalProtect user locations

## Usage

```
show sase fp-user-locations [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase fp-user-locations
```

Run directly on device via SSH:
```
arc:fw-01 > show sase fp-user-locations --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase fp-user-locations
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
