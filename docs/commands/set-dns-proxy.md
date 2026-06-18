# set dns-proxy

Create a **dns-proxy** object in the active SCM folder.

## Feature flag

This command requires the **`dns_proxy`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable dns_proxy

# Enable permanently (config/features.json — git-ignored):
{"  \"dns_proxy\": true"}
```

## Syntax

```text
configure
set dns-proxy <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/network/v1/dns-proxies
```

Resource notes: DNS proxy configuration

## Supported methods

- GET (list)
- POST (create)
- PUT (update)
- DELETE

## Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `name` | Yes | Object name (must be unique in folder) |
| `folder` | Yes | Set automatically from active folder context |
| `description` | No | Human-readable description |
| `tag` | No | One or more tag names to associate |

> **Full schema:** See `docs/scm-api/specs/ngfw-network.md` for all fields.

## Example

```text
arc:global > configure
arc:global # feature enable dns_proxy
arc:global # set dns-proxy MyObject ...
  ✓ Dns-Proxy MyObject created (id: ...)
```

## Related commands

- `show dns-proxy` — list dns-proxy objects in the active folder
- `delete dns-proxy <name>` — remove a dns-proxy object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
