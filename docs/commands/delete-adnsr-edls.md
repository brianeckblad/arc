---
command: "delete adnsr edls"
description: "Delete an EDL definition"
category: adnsr
scope: global
---

# delete adnsr edls

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an EDL definition

## Usage

```
delete adnsr edls [--remote]
```

## Examples

Run via SCM API:
```
arc > delete adnsr edls
```

Run directly on device via SSH:
```
arc:fw-01 > delete adnsr edls --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete adnsr edls
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
