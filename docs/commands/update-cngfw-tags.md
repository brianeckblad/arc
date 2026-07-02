---
command: "update cngfw tags"
description: "Update a tag"
category: cloudngfw
scope: global
---

# update cngfw tags

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a tag

## Usage

```
update cngfw tags [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw tags
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw tags --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw tags
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
