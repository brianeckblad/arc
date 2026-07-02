---
command: "show sase sites id"
description: "Get a site"
category: sase
scope: global
---

# show sase sites id

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a site

## Usage

```
show sase sites id [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase sites id
```

Run directly on device via SSH:
```
arc:fw-01 > show sase sites id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase sites id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
