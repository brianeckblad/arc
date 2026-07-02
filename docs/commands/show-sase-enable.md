---
command: "show sase enable"
description: "Get GlobalProtect enablement status"
category: sase
scope: global
---

# show sase enable

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get GlobalProtect enablement status

## Usage

```
show sase enable [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase enable
```

Run directly on device via SSH:
```
arc:fw-01 > show sase enable --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase enable
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
