---
command: "set cngfw snippets"
description: "Create a snippet"
category: cloudngfw
scope: global
---

# set cngfw snippets

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a snippet

## Usage

```
set cngfw snippets [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw snippets
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw snippets --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw snippets
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
