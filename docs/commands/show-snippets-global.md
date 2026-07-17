---
command: "show snippets global"
description: "List ALL snippets regardless of device or folder context"
feature_flag: show_snippets
category: setup
scope: global
api: "GET /config/setup/v1/snippets"
---

---
command: "show snippets global"
description: "List ALL snippets regardless of device or folder context"
feature_flag: show_snippets
category: setup
scope: global
api: "GET /config/setup/v1/snippets"
---

---
command: "show snippets global"
description: "List ALL snippets regardless of device or folder context"
feature_flag: show_snippets
category: setup
scope: global
api: "GET /config/setup/v1/snippets"
---

# show snippets global

**Category:** setup
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List ALL snippets regardless of device or folder context

## Usage

```
show snippets global [--remote]
```

## Examples

Run via SCM API:
```
arc > show snippets global
```

Run directly on device via SSH:
```
arc:fw-01 > show snippets global --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show snippets global
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
