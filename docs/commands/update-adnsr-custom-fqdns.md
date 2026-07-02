---
command: "update adnsr custom-fqdns"
description: "Update a Custom FQDN"
category: adnsr
scope: global
---

# update adnsr custom-fqdns

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a Custom FQDN

## Usage

```
update adnsr custom-fqdns [--remote]
```

## Examples

Run via SCM API:
```
arc > update adnsr custom-fqdns
```

Run directly on device via SSH:
```
arc:fw-01 > update adnsr custom-fqdns --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update adnsr custom-fqdns
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
