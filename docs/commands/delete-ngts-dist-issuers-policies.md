---
command: "delete ngts dist-issuers policies"
description: "Remove a Workload Issuance policy"
category: ngts
scope: global
---

# delete ngts dist-issuers policies

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Remove a Workload Issuance policy

## Usage

```
delete ngts dist-issuers policies [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ngts dist-issuers policies
```

Run directly on device via SSH:
```
arc:fw-01 > delete ngts dist-issuers policies --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ngts dist-issuers policies
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
