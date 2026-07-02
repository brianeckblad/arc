---
command: "set sase fp-destinations"
description: "Create a GlobalProtect destination"
category: sase
scope: global
---

# set sase fp-destinations

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a GlobalProtect destination

## Usage

```
set sase fp-destinations [--remote]
```

## Examples

Run via SCM API:
```
arc > set sase fp-destinations
```

Run directly on device via SSH:
```
arc:fw-01 > set sase fp-destinations --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set sase fp-destinations
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
