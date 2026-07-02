---
command: "show sase sites"
description: "List sites"
category: sase
scope: global
---

# show sase sites

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List sites

## Usage

```
show sase sites [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase sites
```

Run directly on device via SSH:
```
arc:fw-01 > show sase sites --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase sites
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
