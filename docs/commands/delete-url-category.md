---
command: "delete url-category"
description: "Delete a URL category — delete url-category <name>"
usage: "delete url-category <name>"
feature_flag: delete_security
category: security
scope: folder
api: "DELETE /config/security/v1/url-categories/{id}"
---

# delete url-category

**Category:** security
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a URL category — delete url-category <name>

## Usage

```
delete url-category [--remote]
```

## Examples

Run via SCM API:
```
arc > delete url-category
```

Run directly on device via SSH:
```
arc:fw-01 > delete url-category --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete url-category
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
