---
command: "delete sase fp-destinations"
description: "Delete a GlobalProtect destination"
category: sase
scope: global
---

# delete sase fp-destinations

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a GlobalProtect destination

## Usage

```
delete sase fp-destinations [--remote]
```

## Examples

Run via SCM API:
```
arc > delete sase fp-destinations
```

Run directly on device via SSH:
```
arc:fw-01 > delete sase fp-destinations --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete sase fp-destinations
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
