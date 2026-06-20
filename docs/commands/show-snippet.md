---
command: "show snippet"
description: "Show full detail for a snippet"
usage: "show snippet <name>"
feature_flag: show_snippets
category: setup
scope: global
api: "GET /config/setup/v1/snippets"
---

# show snippet

**Category:** setup
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show full detail for a named snippet, including identity, metadata, all
**variables**, and any other configuration sections returned by the SCM API.

Output is split into multiple tables:

| Table | Contents |
|-------|----------|
| Snippet: \<name\> | Name, ID, type, prefix flag, shared-in scope, description, labels, attached folders |
| Variables | Variable name, type, default value, description |
| Additional sections | Any other structured data the snippet API returns (e.g. config elements) |

## Usage

```
show snippet <name>
```

## Examples

```
arc > show snippet my-snippet-name
```

## See Also

- `help show snippets` — List all snippets
- `help show device snippets` — List snippets attached to a device
- `help commands` — Full command reference
