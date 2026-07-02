---
command: "show cngfw snippets"
description: "List snippets"
category: cloudngfw
scope: global
---

# show cngfw snippets

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List snippets

## Usage

```
show cngfw snippets [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw snippets
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw snippets --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw snippets
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
