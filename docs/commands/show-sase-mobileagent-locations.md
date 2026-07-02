---
command: "show sase mobileagent locations"
description: "List GlobalProtect locations"
category: sase
scope: global
---

# show sase mobileagent locations

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List GlobalProtect locations

## Usage

```
show sase mobileagent locations [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase mobileagent locations
```

Run directly on device via SSH:
```
arc:fw-01 > show sase mobileagent locations --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase mobileagent locations
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
