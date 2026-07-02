---
command: "show adnsr edls"
description: "List EDL definitions"
category: adnsr
scope: global
---

# show adnsr edls

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List EDL definitions

## Usage

```
show adnsr edls [--remote]
```

## Examples

Run via SCM API:
```
arc > show adnsr edls
```

Run directly on device via SSH:
```
arc:fw-01 > show adnsr edls --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show adnsr edls
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
