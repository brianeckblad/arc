---
command: "show cngfw snippet-categories"
description: "List snippets categories"
category: cloudngfw
scope: global
---

# show cngfw snippet-categories

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List snippets categories

## Usage

```
show cngfw snippet-categories [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw snippet-categories
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw snippet-categories --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw snippet-categories
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
