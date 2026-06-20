---
command: "commit"
description: "Push candidate config to managed devices"
usage: "commit [description <text>]"
feature_flag: commit
category: operations
scope: folder
api: "POST /config/setup/v1/config-versions/candidate:push"
---

# commit

Commit the candidate configuration — commit [description <text>]

## Category

config

## Default path

API mode through SCM REST when a translation exists; otherwise use SSH for live device output.

## Remote behavior

Supported

## Examples

```text
commit description planned-change
```

## Notes

Use `pwd` to confirm the current device and mode before running device-scoped commands.
