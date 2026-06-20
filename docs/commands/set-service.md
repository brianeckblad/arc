---
command: "set service"
description: "Create service — set service <name> tcp|udp port <n> [source-port <n>]"
usage: "set service <name> tcp|udp port <n> [source-port <n>] [description <text>] [tag <name>]"
feature_flag: create_service
category: objects
scope: folder
api: "POST /config/objects/v1/services"
---

# set service

Create a service object (TCP or UDP) in the active SCM folder.

**Source:** `POST /config/objects/v1/services`  
**Schema:** services (see `docs/scm-api/specs/ngfw-objects.yaml`)  
**Feature flag:** `create_service`

---

## Protocol variants (oneOf — exactly one required)

The `services` schema requires `protocol.tcp` OR `protocol.udp` — never both.

### tcp — TCP service

```text
set service <name> tcp port <destination-port>
set service <name> tcp port <destination-port> source-port <source-port>
```

| Field | Type | maxLength | Description |
|---|---|---|---|
| `protocol.tcp.port` | string | 1023 chars | Destination port(s) — **required** |
| `protocol.tcp.source_port` | string | 1023 chars | Source port(s) — optional |

Port value formats:

| Format | Example | Meaning |
|---|---|---|
| Single | `80` | Port 80 only |
| Range | `8080-8090` | Ports 8080 through 8090 inclusive |
| List | `80,443,8080` | Comma-separated, no spaces |
| Any | `0-65535` | All ports |

```text
set service HTTP      tcp port 80
set service HTTPS     tcp port 443
set service HTTP-ALT  tcp port 8080-8090
set service APP-PORTS tcp port 8080,8443,9000
set service APP       tcp port 8443  source-port 1024-65535
set service HTTPS-Tag tcp port 443   description "Web TLS"  tag Production
```

---

### udp — UDP service

```text
set service <name> udp port <destination-port>
set service <name> udp port <destination-port> source-port <source-port>
```

| Field | Type | maxLength | Description |
|---|---|---|---|
| `protocol.udp.port` | string | 1023 chars | Destination port(s) — **required** |
| `protocol.udp.source_port` | string | 1023 chars | Source port(s) — optional |

```text
set service DNS         udp port 53
set service DHCP-Client udp port 68
set service NTP         udp port 123
set service SNMP        udp port 161,162
set service SYSLOG      udp port 514  description "Syslog receiver"  tag Monitoring
set service RPC         udp port 111  source-port 1024-65535
```

---

## Optional fields (apply to both protocols)

| Field | Type | Description |
|---|---|---|
| `description` | string | Human-readable description |
| `tag` | list of strings | Tag names to associate |

---

## Full syntax

```text
set service <name> tcp port <n>  [source-port <n>]  [description <text>] [tag <name>]
set service <name> udp port <n>  [source-port <n>]  [description <text>] [tag <name>]
```

---

## Related commands

- `show service` — list service objects
- `delete service <name>` — remove a service object
- `set service-group <name> members <svc1> [svc2...]` — group services together
