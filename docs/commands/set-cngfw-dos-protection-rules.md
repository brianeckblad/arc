---
command: "set cngfw dos-protection-rules"
description: "Create a DoS protection rule"
category: cloudngfw
scope: global
---

# set cngfw dos-protection-rules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a DoS protection rule

## Usage

```
set cngfw dos-protection-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw dos-protection-rules
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw dos-protection-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw dos-protection-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
