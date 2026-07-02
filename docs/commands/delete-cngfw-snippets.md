---
command: "delete cngfw snippets"
description: "Delete a snippet"
category: cloudngfw
scope: global
---

# delete cngfw snippets

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a snippet

## Usage

```
delete cngfw snippets [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw snippets
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw snippets --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw snippets
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
