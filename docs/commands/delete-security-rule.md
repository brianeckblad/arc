---
command: "delete security-rule"
description: "Delete a security rule — delete security-rule <name>"
usage: "delete security-rule <name>"
feature_flag: delete_security
category: security
scope: folder
api: "DELETE /config/security/v1/security-rules/{id}"
---

# delete security-rule

**Category:** security
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a security rule — delete security-rule <name>

## Usage

```
delete security-rule [--remote]
```

## Examples

Run via SCM API:
```
arc > delete security-rule
```

Run directly on device via SSH:
```
arc:fw-01 > delete security-rule --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete security-rule
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
