---
command: "delete zone-profiles"
description: "Delete a zone protection profile"
category: network
scope: global
---

# delete zone-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a zone protection profile

## Usage

```
delete zone-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete zone-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete zone-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete zone-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
