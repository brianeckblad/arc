---
command: "delete cngfw anti-spyware-signatures"
description: "Delete an anti-spyware signature"
category: cloudngfw
scope: global
---

# delete cngfw anti-spyware-signatures

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an anti-spyware signature

## Usage

```
delete cngfw anti-spyware-signatures [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw anti-spyware-signatures
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw anti-spyware-signatures --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw anti-spyware-signatures
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
