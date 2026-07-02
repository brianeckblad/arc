---
command: "update cngfw anti-spyware-signatures"
description: "Update an anti-spyware signature"
category: cloudngfw
scope: global
---

# update cngfw anti-spyware-signatures

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an anti-spyware signature

## Usage

```
update cngfw anti-spyware-signatures [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw anti-spyware-signatures
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw anti-spyware-signatures --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw anti-spyware-signatures
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
