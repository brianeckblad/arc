---
command: "delete cngfw sites"
description: "Delete a site"
category: cloudngfw
scope: global
---

# delete cngfw sites

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a site

## Usage

```
delete cngfw sites [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw sites
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw sites --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw sites
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
