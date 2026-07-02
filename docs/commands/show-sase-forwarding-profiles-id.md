---
command: "show sase forwarding-profiles id"
description: "Get a GlobalProtect forwarding profile"
category: sase
scope: global
---

# show sase forwarding-profiles id

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a GlobalProtect forwarding profile

## Usage

```
show sase forwarding-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase forwarding-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show sase forwarding-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase forwarding-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
