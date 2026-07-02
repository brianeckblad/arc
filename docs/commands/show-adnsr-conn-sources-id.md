---
command: "show adnsr conn-sources id"
description: "Get a Connection Source"
category: adnsr
scope: global
---

# show adnsr conn-sources id

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a Connection Source

## Usage

```
show adnsr conn-sources id [--remote]
```

## Examples

Run via SCM API:
```
arc > show adnsr conn-sources id
```

Run directly on device via SSH:
```
arc:fw-01 > show adnsr conn-sources id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show adnsr conn-sources id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
