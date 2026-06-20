---
command: "show routing route"
description: "Show static routes in the active folder"
feature_flag: show_routing
category: network
scope: folder
api: "GET /config/network/v1/routing/static-routes"
---

# show routing route

Show routing table

## Category

network

## Default path

API mode through SCM REST when a translation exists; otherwise use SSH for live device output.

## Remote behavior

Supported

## Examples

```text
show routing route
```

## Notes

Use `pwd` to confirm the current device and mode before running device-scoped commands.
