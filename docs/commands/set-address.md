# set address

Create an address object in the active SCM folder.

**Source:** `POST /config/objects/v1/addresses`  
**Schema:** addresses.addresses_create (see `docs/scm-api/specs/ngfw-objects.yaml`)  
**Feature flag:** `create_address` — enable with `feature enable create_address`

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

| Field | Type | Description |
|---|---|---|
| `description` | string (max 1023 chars) | Human-readable description |
| `tag` | list of strings | Tag names to associate; tags must exist in the same folder |

```text
set address WebServer ip-netmask 10.1.2.3/32  description "Web tier host"  tag Production
```

---

## Full syntax

```text
set address <name> ip-netmask  <value>   [description <text>] [tag <name>]
set address <name> ip-range    <value>   [description <text>] [tag <name>]
set address <name> ip-wildcard <value>   [description <text>] [tag <name>]
set address <name> fqdn        <value>   [description <text>] [tag <name>]
```

---

## Related commands

- `show address` — list address objects
- `delete address <name>` — remove an address object
- `set address-group <name> static <member>` — group addresses together
- `help set-address-group` — address group creation (static and dynamic variants)
