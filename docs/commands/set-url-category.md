# set url-category

**Category:** security
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a custom URL category — set url-category <name> type url-list list <url1>

## Usage

```
set url-category [--remote]
```

## Examples

Run via SCM API:
```
arc > set url-category
```

Run directly on device via SSH:
```
arc:fw-01 > set url-category --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set url-category
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
