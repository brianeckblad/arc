---
command: "delete cngfw vuln-signatures"
description: "Delete a vulnerability protection signature"
category: cloudngfw
scope: global
---

# delete cngfw vuln-signatures

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a vulnerability protection signature

## Usage

```
delete cngfw vuln-signatures [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw vuln-signatures
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw vuln-signatures --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw vuln-signatures
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
