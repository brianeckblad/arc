---
command: "delete cngfw url-access-profiles"
description: "Delete a URL access profile"
category: cloudngfw
scope: global
---

# delete cngfw url-access-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a URL access profile

## Usage

```
delete cngfw url-access-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw url-access-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw url-access-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw url-access-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
