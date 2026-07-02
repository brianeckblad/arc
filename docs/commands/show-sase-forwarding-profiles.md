---
command: "show sase forwarding-profiles"
description: "List GlobalProtect forwarding profiles"
category: sase
scope: global
---

# show sase forwarding-profiles

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List GlobalProtect forwarding profiles

## Usage

```
show sase forwarding-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase forwarding-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show sase forwarding-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase forwarding-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
