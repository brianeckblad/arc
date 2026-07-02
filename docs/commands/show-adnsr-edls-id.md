---
command: "show adnsr edls id"
description: "Get an EDL definition"
category: adnsr
scope: global
---

# show adnsr edls id

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an EDL definition

## Usage

```
show adnsr edls id [--remote]
```

## Examples

Run via SCM API:
```
arc > show adnsr edls id
```

Run directly on device via SSH:
```
arc:fw-01 > show adnsr edls id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show adnsr edls id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
