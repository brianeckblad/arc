---
command: "show cngfw app-override-rules"
description: "List application override rules"
category: cloudngfw
scope: global
---

# show cngfw app-override-rules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List application override rules

## Usage

```
show cngfw app-override-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw app-override-rules
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw app-override-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw app-override-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
