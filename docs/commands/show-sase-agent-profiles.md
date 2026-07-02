---
command: "show sase agent-profiles"
description: "List GlobalProtect agent profiles"
category: sase
scope: global
---

# show sase agent-profiles

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List GlobalProtect agent profiles

## Usage

```
show sase agent-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase agent-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show sase agent-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase agent-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
