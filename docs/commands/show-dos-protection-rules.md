---
command: "show dos-protection-rules"
description: "Show DoS protection rules in the active folder"
feature_flag: dos_protection
category: security
scope: folder
api: "GET /config/security/v1/dos-protection-rules"
---

---
command: "show dos-protection-rules"
description: "Show DoS protection rules in the active folder"
feature_flag: dos_protection
category: security
scope: folder
api: "GET /config/security/v1/dos-protection-rules"
---

---
command: "show dos-protection-rules"
description: "Show DoS protection rules in the active folder"
feature_flag: dos_protection
category: security
scope: folder
api: "GET /config/security/v1/dos-protection-rules"
---

# show dos-protection-rules

**Category:** security
**API mode:** ✓ Live SCM data
**SSH mode:** `show dos-protection rule all`

## Description

Show DoS protection rules in the active folder

## Usage

```
show dos-protection-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > show dos-protection-rules
```

Run directly on device via SSH:
```
arc:fw-01 > show dos-protection-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show dos-protection-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
