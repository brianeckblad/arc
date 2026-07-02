---
command: "show ngts dist-issuers policies"
description: "Get the details of all Workload"
category: ngts
scope: global
---

# show ngts dist-issuers policies

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get the details of all Workload

## Usage

```
show ngts dist-issuers policies [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts dist-issuers policies
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts dist-issuers policies --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts dist-issuers policies
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
