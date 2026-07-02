---
command: "update adnsr edls"
description: "Update an EDL definition"
category: adnsr
scope: global
---

# update adnsr edls

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an EDL definition

## Usage

```
update adnsr edls [--remote]
```

## Examples

Run via SCM API:
```
arc > update adnsr edls
```

Run directly on device via SSH:
```
arc:fw-01 > update adnsr edls --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update adnsr edls
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
