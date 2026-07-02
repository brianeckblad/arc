---
command: "show adnsr conn-sources"
description: "List Connection Sources"
category: adnsr
scope: global
---

# show adnsr conn-sources

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List Connection Sources

## Usage

```
show adnsr conn-sources [--remote]
```

## Examples

Run via SCM API:
```
arc > show adnsr conn-sources
```

Run directly on device via SSH:
```
arc:fw-01 > show adnsr conn-sources --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show adnsr conn-sources
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
