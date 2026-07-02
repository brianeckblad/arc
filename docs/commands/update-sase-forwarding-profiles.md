---
command: "update sase forwarding-profiles"
description: "Update a GlobalProtect forwarding profile"
category: sase
scope: global
---

# update sase forwarding-profiles

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a GlobalProtect forwarding profile

## Usage

```
update sase forwarding-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update sase forwarding-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update sase forwarding-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update sase forwarding-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
