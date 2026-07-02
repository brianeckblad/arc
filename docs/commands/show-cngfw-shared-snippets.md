---
command: "show cngfw shared-snippets"
description: "Get Shared Snippets"
category: cloudngfw
scope: global
---

# show cngfw shared-snippets

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get Shared Snippets

## Usage

```
show cngfw shared-snippets [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw shared-snippets
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw shared-snippets --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw shared-snippets
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
