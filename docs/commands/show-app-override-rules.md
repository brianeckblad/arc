---
command: "show app-override-rules"
description: "Show application override rules in the active folder"
feature_flag: app_override
category: security
scope: folder
api: "GET /config/security/v1/app-override-rules"
---

---
command: "show app-override-rules"
description: "Show application override rules in the active folder"
feature_flag: app_override
category: security
scope: folder
api: "GET /config/security/v1/app-override-rules"
---

---
command: "show app-override-rules"
description: "Show application override rules in the active folder"
feature_flag: app_override
category: security
scope: folder
api: "GET /config/security/v1/app-override-rules"
---

# show app-override-rules

**Category:** security
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show application override rules in the active folder

## Usage

```
show app-override-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > show app-override-rules
```

Run directly on device via SSH:
```
arc:fw-01 > show app-override-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show app-override-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
