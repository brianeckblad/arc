---
command: "clone"
description: "Clone a named object under a new name (address, service, group, tag, EDL, …)"
usage: "clone <resource> <source-name> <new-name>"
feature_flag: clone_object
category: objects
scope: folder
api: "GET <resource> + POST <resource> (staged)"
---

# clone

**Category:** objects
**API mode:** ✓ Live SCM data (staged write)
**SSH mode:** Not applicable (config read/write via SCM)

## Description

Duplicate an existing configuration object under a new name. `clone` reads the
source object from the **active container** (the current folder, or the active
snippet when you have `cd snippet`-ed into one), strips its server-managed
fields (id/uuid/audit), renames it, and creates the copy in the same container.

Like every other write, the create is **staged** — run `commit` to apply it and
`show config` to review the queue first.

## Usage

```
clone <resource> <source-name> <new-name>
```

Cloneable object types: `address`, `address-group`, `service`, `service-group`,
`tag`, `external-dynamic-list`. Other resources that expose a `show`/`set` pair
with a collection endpoint are cloned generically from the resource catalog.

## Examples

Clone an address in the active folder:
```
clone address web-1 web-2
commit
```

Clone a service group:
```
clone service-group web-stack web-stack-v2
```

Clone an object **into a snippet** (enter the snippet first):
```
cd snippet dmz-baseline
clone address web-1 web-1-dmz
commit
```

## Notes

- The new name must differ from the source name.
- Tab-complete the resource type, then the source object name.
- The clone lands in whatever container the prompt shows — folder or snippet.
