---
command: "delete cngfw dos-protection-profiles"
description: "Delete a DoS protection profile"
category: cloudngfw
scope: global
---

# delete cngfw dos-protection-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a DoS protection profile

## Usage

```
delete cngfw dos-protection-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw dos-protection-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw dos-protection-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw dos-protection-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
