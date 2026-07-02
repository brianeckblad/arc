---
command: "delete cngfw config-versions candidate"
description: "Delete a candidate configuration"
category: cloudngfw
scope: global
---

# delete cngfw config-versions candidate

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a candidate configuration

## Usage

```
delete cngfw config-versions candidate [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw config-versions candidate
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw config-versions candidate --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw config-versions candidate
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
