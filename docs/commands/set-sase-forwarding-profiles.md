---
command: "set sase forwarding-profiles"
description: "Create a GlobalProtect forwarding profile"
category: sase
scope: global
---

# set sase forwarding-profiles

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a GlobalProtect forwarding profile

## Usage

```
set sase forwarding-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set sase forwarding-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set sase forwarding-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set sase forwarding-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
