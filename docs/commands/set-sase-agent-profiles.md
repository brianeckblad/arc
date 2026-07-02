---
command: "set sase agent-profiles"
description: "Create a GlobalProtect agent profile"
category: sase
scope: global
---

# set sase agent-profiles

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a GlobalProtect agent profile

## Usage

```
set sase agent-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set sase agent-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set sase agent-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set sase agent-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
