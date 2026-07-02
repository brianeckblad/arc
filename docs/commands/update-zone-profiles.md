---
command: "update zone-profiles"
description: "Update a zone protection profile"
category: network
scope: global
---

# update zone-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a zone protection profile

## Usage

```
update zone-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update zone-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update zone-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update zone-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
