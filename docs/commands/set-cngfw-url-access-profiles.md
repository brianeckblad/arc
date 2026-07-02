---
command: "set cngfw url-access-profiles"
description: "Create a URL access profile"
category: cloudngfw
scope: global
---

# set cngfw url-access-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a URL access profile

## Usage

```
set cngfw url-access-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw url-access-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw url-access-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw url-access-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
