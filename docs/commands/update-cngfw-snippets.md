---
command: "update cngfw snippets"
description: "Update a snippet"
category: cloudngfw
scope: global
---

# update cngfw snippets

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a snippet

## Usage

```
update cngfw snippets [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw snippets
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw snippets --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw snippets
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
