---
command: "update sase sites"
description: "Update a site"
category: sase
scope: global
---

# update sase sites

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a site

## Usage

```
update sase sites [--remote]
```

## Examples

Run via SCM API:
```
arc > update sase sites
```

Run directly on device via SSH:
```
arc:fw-01 > update sase sites --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update sase sites
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
