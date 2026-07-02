---
command: "update adnsr conn-sources"
description: "Update a Connection Source"
category: adnsr
scope: global
---

# update adnsr conn-sources

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a Connection Source

## Usage

```
update adnsr conn-sources [--remote]
```

## Examples

Run via SCM API:
```
arc > update adnsr conn-sources
```

Run directly on device via SSH:
```
arc:fw-01 > update adnsr conn-sources --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update adnsr conn-sources
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
