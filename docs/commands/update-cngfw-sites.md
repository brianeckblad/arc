---
command: "update cngfw sites"
description: "Update a site"
category: cloudngfw
scope: global
---

# update cngfw sites

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a site

## Usage

```
update cngfw sites [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw sites
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw sites --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw sites
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
