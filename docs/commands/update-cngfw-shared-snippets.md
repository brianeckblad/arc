---
command: "update cngfw shared-snippets"
description: "Update Shared Snippets"
category: cloudngfw
scope: global
---

# update cngfw shared-snippets

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update Shared Snippets

## Usage

```
update cngfw shared-snippets [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw shared-snippets
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw shared-snippets --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw shared-snippets
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
