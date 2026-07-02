---
command: "update ngts dist-issuers configurations"
description: "Update an Issuer configuration details"
category: ngts
scope: global
---

# update ngts dist-issuers configurations

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an Issuer configuration details

## Usage

```
update ngts dist-issuers configurations [--remote]
```

## Examples

Run via SCM API:
```
arc > update ngts dist-issuers configurations
```

Run directly on device via SSH:
```
arc:fw-01 > update ngts dist-issuers configurations --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ngts dist-issuers configurations
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
