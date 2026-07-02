---
command: "set cngfw dos-protection-profiles"
description: "Create a DoS protection profile"
category: cloudngfw
scope: global
---

# set cngfw dos-protection-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a DoS protection profile

## Usage

```
set cngfw dos-protection-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw dos-protection-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw dos-protection-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw dos-protection-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
