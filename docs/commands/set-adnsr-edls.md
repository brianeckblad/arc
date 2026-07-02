---
command: "set adnsr edls"
description: "Create an EDL definition"
category: adnsr
scope: global
---

# set adnsr edls

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an EDL definition

## Usage

```
set adnsr edls [--remote]
```

## Examples

Run via SCM API:
```
arc > set adnsr edls
```

Run directly on device via SSH:
```
arc:fw-01 > set adnsr edls --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set adnsr edls
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
