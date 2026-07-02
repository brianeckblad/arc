---
command: "update sase agent-profiles"
description: "Update a GlobalProtect agent profile"
category: sase
scope: global
---

# update sase agent-profiles

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a GlobalProtect agent profile

## Usage

```
update sase agent-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update sase agent-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update sase agent-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update sase agent-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
