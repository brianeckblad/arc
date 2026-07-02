---
command: "show cngfw file-blocking-profiles"
description: "List file blocking profiles"
category: cloudngfw
scope: global
---

# show cngfw file-blocking-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List file blocking profiles

## Usage

```
show cngfw file-blocking-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw file-blocking-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw file-blocking-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw file-blocking-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
