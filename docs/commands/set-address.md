---
command: "set address"
description: "Create address — set address <name> ip-netmask|ip-range|ip-wildcard|fqdn <value>"
usage: "set address <name> ip-netmask|ip-range|ip-wildcard|fqdn <value> [description <optional>] [tag <optional>]"
feature_flag: create_address
category: objects
scope: folder
api: "POST /config/objects/v1/addresses"
---

# set address

Create an address object in the active SCM folder.

**Requires:** Configure mode — type `configure` to enter configure mode before using this command.

**Source:** `POST /config/objects/v1/addresses`  
**Schema:** addresses.addresses_create (see `docs/scm-api/specs/ngfw-objects.yaml`)  
**Feature flag:** `create_address` — enable with `feature enable create_address`

---

## Context-sensitive help (`?` and `??`)

Press `?` at any point to see only the **next** syntax options for where you are —
Cisco-style:

```text
set address ?
    <name>        Enter a unique name for the address object

set address web1 ?
    ip-netmask    Single IP or CIDR (10.1.2.3/32)
    ip-range      Inclusive range (10.0.0.1-10.0.0.9)
    ip-wildcard   Wildcard mask (10.0.0.0/0.0.0.255)
    fqdn          Domain name (api.example.com)

set address web1 fqdn ?
    <value>       Enter the value for the chosen type (e.g. 10.1.2.3/32)

set address web1 fqdn 10.1.2.3 ?
    description   Enter a description for this object
    tag           Enter a tag name (must already exist in this folder)
```

Press `?` **a second time** on the same line (i.e. `??`) to show the full command
help page instead of the brief next-options list.

---

## Spaces — no quotes needed

ARC figures out where each field ends from the command structure, so you can type
multi-word values **without quotes**:

```text
set address my web host fqdn api.example.com description primary edge node
```

- The **name** absorbs words until the type keyword (`ip-netmask` / `ip-range` /
  `ip-wildcard` / `fqdn`) appears → name = `my web host`.
- The **description** absorbs the rest of the line (up to `tag`).

Quotes are still accepted and are only needed for the rare case where a value
literally contains a reserved word (a type keyword, or `description` / `tag`):

```text
set address "tag server" fqdn example.com
```

The order of arguments is defined in `settings/command-structure.csv` — a single
line per command listing just the field names (`address,name,type,value,description,tag`).
Reorder by moving the names; the choices, hints and which fields are required come
from the API-derived field library in code, not the CSV.

---

## Address type variants (oneOf — exactly one required)

The `addresses` schema uses a `oneOf` to enforce that exactly one address type field is present.

### ip_netmask — IP address with optional CIDR prefix

```text
set address <name> ip-netmask <value>
```

| Field | Type | Pattern | Example |
|---|---|---|---|
| `ip_netmask` | string | `x.x.x.x[/prefix]` | `192.168.80.0/24` |

```text
set address WebServer     ip-netmask 10.1.2.3/32
set address DMZ-Subnet    ip-netmask 10.1.0.0/24
set address HostOnly      ip-netmask 192.168.1.50
set address RFC1918-10    ip-netmask 10.0.0.0/8    description "Class A private"
```

---

### ip_range — Inclusive IP address range

```text
set address <name> ip-range <start>-<end>
```

| Field | Type | Pattern | Example |
|---|---|---|---|
| `ip_range` | string | `x.x.x.x-x.x.x.x` | `10.0.0.1-10.0.0.4` |

```text
set address Corp-Hosts    ip-range 10.0.0.1-10.0.0.254
set address Small-Range   ip-range 192.168.1.100-192.168.1.120
```

---

### ip_wildcard — IP address with wildcard mask

```text
set address <name> ip-wildcard <ip>/<mask>
```

| Field | Type | Pattern | Example |
|---|---|---|---|
| `ip_wildcard` | string | `x.x.x.x/x.x.x.x` | `10.20.1.0/0.0.248.255` |

The mask is NOT a subnet mask — `0` bits match any value, `1` bits must match exactly.

```text
set address Odd-Subnets   ip-wildcard 10.20.1.0/0.0.248.255
set address Every-Other   ip-wildcard 10.0.0.0/0.255.255.255
```

---

### fqdn — Fully qualified domain name (or glob)

```text
set address <name> fqdn <domain>
```

| Field | Type | Pattern | minLength | maxLength |
|---|---|---|---|---|
| `fqdn` | string | `^[a-zA-Z0-9_]([a-zA-Z0-9._-])+[a-zA-Z0-9]$` | 1 | 255 |

```text
set address API-Server    fqdn api.example.com
set address CDN-Hosts     fqdn cdn.example.com
```

> **Note:** Glob wildcards like `*.example.com` are supported by PAN-OS devices but the
> SCM API schema enforces the pattern above.  If the API rejects a glob, use `ip-netmask`
> or `ip-range` instead.

---

## Optional fields (apply to all subtypes)

These are optional — the API does not require them. In the shell they are tab-completed
*after* the type and value, and may appear in any order.

| Field | Type | Required | Description |
|---|---|---|---|
| `description` | string (max 1023 chars) | optional | Human-readable description |
| `tag` | list of strings | optional | Tag names to associate; tags must exist in the same folder |

```text
set address WebServer ip-netmask 10.1.2.3/32  description <optional>  tag <optional>
```

> **Tab-driven entry.** ARC builds the prompts from `settings/command-structure.csv`.
> At each step Tab shows what to enter next: `<name>` → the type choices
> (`ip-netmask` / `ip-range` / `ip-wildcard` / `fqdn`) → the `<value>` for that type →
> the optional `description` / `tag` keywords. A required value never returns an empty
> list — it shows a hint describing what to type.

---

## Full syntax

```text
set address <name> ip-netmask  <value>   [description <optional>] [tag <optional>]
set address <name> ip-range    <value>   [description <optional>] [tag <optional>]
set address <name> ip-wildcard <value>   [description <optional>] [tag <optional>]
set address <name> fqdn        <value>   [description <optional>] [tag <optional>]
```

---

## Related commands

- `show address` — list address objects
- `delete address <name>` — remove an address object
- `set address-group <name> static <member>` — group addresses together
- `help set-address-group` — address group creation (static and dynamic variants)
