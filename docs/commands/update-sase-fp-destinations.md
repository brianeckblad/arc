---
command: "update sase fp-destinations"
description: "Update a GlobalProtect destination"
category: sase
scope: global
---

# update sase fp-destinations

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a GlobalProtect destination

## Usage

```
update sase fp-destinations [--remote]
```

## Examples

Run via SCM API:
```
arc > update sase fp-destinations
```

Run directly on device via SSH:
```
arc:fw-01 > update sase fp-destinations --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update sase fp-destinations
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
