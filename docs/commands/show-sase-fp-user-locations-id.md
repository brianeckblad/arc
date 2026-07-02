---
command: "show sase fp-user-locations id"
description: "Get a GlobalProtect user location"
category: sase
scope: global
---

# show sase fp-user-locations id

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a GlobalProtect user location

## Usage

```
show sase fp-user-locations id [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase fp-user-locations id
```

Run directly on device via SSH:
```
arc:fw-01 > show sase fp-user-locations id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase fp-user-locations id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
