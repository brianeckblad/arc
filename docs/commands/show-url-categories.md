---
command: "show url-categories"
description: "Show custom URL categories in the active folder"
feature_flag: show_url_categories
category: security
scope: folder
api: "GET /config/security/v1/url-categories"
---

---
command: "show url-categories"
description: "Show custom URL categories in the active folder"
feature_flag: show_url_categories
category: security
scope: folder
api: "GET /config/security/v1/url-categories"
---

---
command: "show url-categories"
description: "Show custom URL categories in the active folder"
feature_flag: show_url_categories
category: security
scope: folder
api: "GET /config/security/v1/url-categories"
---

# show url-categories

**Category:** security
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show custom URL categories in the active folder

## Usage

```
show url-categories [--remote]
```

## Examples

Run via SCM API:
```
arc > show url-categories
```

Run directly on device via SSH:
```
arc:fw-01 > show url-categories --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show url-categories
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
