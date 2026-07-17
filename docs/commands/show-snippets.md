---
command: "show snippets"
description: "List snippets for the current context  [dim](device → device snippets | folder → folder snippets | Shared → all)[/dim]"
feature_flag: show_snippets
category: setup
scope: folder
api: "GET /config/setup/v1/snippets"
---

---
command: "show snippets"
description: "List snippets for the current context  [dim](device → device snippets | folder → folder snippets | Shared → all)[/dim]"
feature_flag: show_snippets
category: setup
scope: folder
api: "GET /config/setup/v1/snippets"
---

---
command: "show snippets"
description: "List snippets for the current context  [dim](device → device snippets | folder → folder snippets | Shared → all)[/dim]"
feature_flag: show_snippets
category: setup
scope: folder
api: "GET /config/setup/v1/snippets"
---

# show snippets

**Category:** setup
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List all SCM snippets (auto-filtered to current device when cd'd into one)

## Usage

```
show snippets [--remote]
```

## Examples

Run via SCM API:
```
arc > show snippets
```

Run directly on device via SSH:
```
arc:fw-01 > show snippets --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show snippets
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
