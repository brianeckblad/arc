---
command: "set sase sites"
description: "Create a site"
category: sase
scope: global
---

# set sase sites

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a site

## Usage

```
set sase sites [--remote]
```

## Examples

Run via SCM API:
```
arc > set sase sites
```

Run directly on device via SSH:
```
arc:fw-01 > set sase sites --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set sase sites
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
