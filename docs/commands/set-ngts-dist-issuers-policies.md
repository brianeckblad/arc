---
command: "set ngts dist-issuers policies"
description: "Create a new Workload Issuance policy"
category: ngts
scope: global
---

# set ngts dist-issuers policies

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a new Workload Issuance policy

## Usage

```
set ngts dist-issuers policies [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts dist-issuers policies
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts dist-issuers policies --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts dist-issuers policies
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
