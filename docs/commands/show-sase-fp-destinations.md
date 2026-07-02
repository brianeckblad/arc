---
command: "show sase fp-destinations"
description: "List GlobalProtect destinations"
category: sase
scope: global
---

# show sase fp-destinations

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List GlobalProtect destinations

## Usage

```
show sase fp-destinations [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase fp-destinations
```

Run directly on device via SSH:
```
arc:fw-01 > show sase fp-destinations --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase fp-destinations
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
