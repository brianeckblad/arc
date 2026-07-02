---
command: "set adnsr custom-fqdns"
description: "Create a Custom FQDN"
category: adnsr
scope: global
---

# set adnsr custom-fqdns

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a Custom FQDN

## Usage

```
set adnsr custom-fqdns [--remote]
```

## Examples

Run via SCM API:
```
arc > set adnsr custom-fqdns
```

Run directly on device via SSH:
```
arc:fw-01 > set adnsr custom-fqdns --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set adnsr custom-fqdns
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
