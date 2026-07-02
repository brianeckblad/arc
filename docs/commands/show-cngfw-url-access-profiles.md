---
command: "show cngfw url-access-profiles"
description: "List URL access profiles"
category: cloudngfw
scope: global
---

# show cngfw url-access-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List URL access profiles

## Usage

```
show cngfw url-access-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw url-access-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw url-access-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw url-access-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
