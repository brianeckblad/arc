---
command: "delete adnsr conn-sources"
description: "Delete a Connection Source"
category: adnsr
scope: global
---

# delete adnsr conn-sources

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a Connection Source

## Usage

```
delete adnsr conn-sources [--remote]
```

## Examples

Run via SCM API:
```
arc > delete adnsr conn-sources
```

Run directly on device via SSH:
```
arc:fw-01 > delete adnsr conn-sources --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete adnsr conn-sources
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
