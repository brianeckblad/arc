---
command: "show sase fp-destinations id"
description: "Get a GlobalProtect destination"
category: sase
scope: global
---

# show sase fp-destinations id

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a GlobalProtect destination

## Usage

```
show sase fp-destinations id [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase fp-destinations id
```

Run directly on device via SSH:
```
arc:fw-01 > show sase fp-destinations id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase fp-destinations id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
