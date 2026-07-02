---
command: "update cngfw url-access-profiles"
description: "Update a URL access Profile"
category: cloudngfw
scope: global
---

# update cngfw url-access-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a URL access Profile

## Usage

```
update cngfw url-access-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw url-access-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw url-access-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw url-access-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
