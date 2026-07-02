---
command: "show cngfw address-groups id"
description: "Get an address group"
category: cloudngfw
scope: global
---

# show cngfw address-groups id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an address group

## Usage

```
show cngfw address-groups id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw address-groups id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw address-groups id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw address-groups id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
