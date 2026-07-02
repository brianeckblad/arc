---
command: "show cngfw snippets id"
description: "Get a snippet"
category: cloudngfw
scope: global
---

# show cngfw snippets id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a snippet

## Usage

```
show cngfw snippets id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw snippets id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw snippets id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw snippets id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
