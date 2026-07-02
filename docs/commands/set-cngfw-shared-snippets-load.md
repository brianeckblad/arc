---
command: "set cngfw shared-snippets load"
description: "Load Shared Snippets"
category: cloudngfw
scope: global
---

# set cngfw shared-snippets load

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Load Shared Snippets

## Usage

```
set cngfw shared-snippets load [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw shared-snippets load
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw shared-snippets load --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw shared-snippets load
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
