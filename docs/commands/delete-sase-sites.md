---
command: "delete sase sites"
description: "Delete a site"
category: sase
scope: global
---

# delete sase sites

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a site

## Usage

```
delete sase sites [--remote]
```

## Examples

Run via SCM API:
```
arc > delete sase sites
```

Run directly on device via SSH:
```
arc:fw-01 > delete sase sites --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete sase sites
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
