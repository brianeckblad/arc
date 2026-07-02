---
command: "delete sase agent-profiles"
description: "Delete a GlobalProtect agent profile"
category: sase
scope: global
---

# delete sase agent-profiles

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a GlobalProtect agent profile

## Usage

```
delete sase agent-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete sase agent-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete sase agent-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete sase agent-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
