---
command: "set ngts dist-issuers configurations"
description: "Create a new Issuer configuration"
category: ngts
scope: global
---

# set ngts dist-issuers configurations

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a new Issuer configuration

## Usage

```
set ngts dist-issuers configurations [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts dist-issuers configurations
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts dist-issuers configurations --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts dist-issuers configurations
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
