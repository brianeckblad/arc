# test url

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** `(dynamic)`

## Description

Test URL categorization — test url <url>  (use --remote)

## Usage

```
test url [--remote]
```

## Examples

Run via SCM API:
```
arc > test url
```

Run directly on device via SSH:
```
arc:fw-01 > test url --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > test url
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
