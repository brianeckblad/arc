---
command: "set adnsr conn-sources"
description: "Create a Connection Source"
category: adnsr
scope: global
---

# set adnsr conn-sources

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a Connection Source

## Usage

```
set adnsr conn-sources [--remote]
```

## Examples

Run via SCM API:
```
arc > set adnsr conn-sources
```

Run directly on device via SSH:
```
arc:fw-01 > set adnsr conn-sources --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set adnsr conn-sources
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
