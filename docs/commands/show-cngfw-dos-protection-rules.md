---
command: "show cngfw dos-protection-rules"
description: "List DoS protection rules"
category: cloudngfw
scope: global
---

# show cngfw dos-protection-rules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List DoS protection rules

## Usage

```
show cngfw dos-protection-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw dos-protection-rules
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw dos-protection-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw dos-protection-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
