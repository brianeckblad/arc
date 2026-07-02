---
command: "show adnsr custom-fqdns id"
description: "Get a custom fqdn"
category: adnsr
scope: global
---

# show adnsr custom-fqdns id

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a custom fqdn

## Usage

```
show adnsr custom-fqdns id [--remote]
```

## Examples

Run via SCM API:
```
arc > show adnsr custom-fqdns id
```

Run directly on device via SSH:
```
arc:fw-01 > show adnsr custom-fqdns id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show adnsr custom-fqdns id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
