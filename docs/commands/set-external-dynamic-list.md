---
command: "set external-dynamic-list"
description: "Create EDL — set external-dynamic-list <name> type ip|domain|url url <fetch-url>"
feature_flag: create_edl
category: objects
scope: folder
api: "POST /config/objects/v1/external-dynamic-lists"
---

---
command: "set external-dynamic-list"
description: "Create EDL — set external-dynamic-list <name> type ip|domain|url url <fetch-url>"
feature_flag: create_edl
category: objects
scope: folder
api: "POST /config/objects/v1/external-dynamic-lists"
---

---
command: "set external-dynamic-list"
description: "Create EDL — set external-dynamic-list <name> type ip|domain|url url <fetch-url>"
usage: "set external-dynamic-list <name> type ip|domain|url url <fetch-url> [description <text>]"
feature_flag: create_edl
category: objects
scope: folder
api: "POST /config/objects/v1/external-dynamic-lists"
---

# set external-dynamic-list

Create an External Dynamic List (EDL) in the active SCM folder.

**Source:** `POST /config/objects/v1/external-dynamic-lists`  
**Schema:** external-dynamic-lists (see `docs/scm-api/specs/ngfw-objects.yaml`)  
**Feature flag:** `create_edl`

---

## EDL type variants (oneOf — exactly one type block required)

The `external-dynamic-lists` schema requires exactly one of `ip`, `domain`, `url`, `imsi`, or `imei` inside the `type` field.

### ip — IP address list

The device fetches a text file, one IP/CIDR per line, and blocks/allows those addresses.

```text
set external-dynamic-list <name> type ip url <fetch-url>
```

```text
set external-dynamic-list Threat-IPs   type ip url https://feeds.example.com/bad-ips.txt
set external-dynamic-list PrivateNets  type ip url https://internal.example.com/ranges.txt  description "RFC1918"
```

---

### domain — Domain name list

The device resolves and blocks/allows DNS lookups matching these domains.

```text
set external-dynamic-list <name> type domain url <fetch-url>
```

```text
set external-dynamic-list Block-Domains  type domain url https://feeds.example.com/domains.txt
set external-dynamic-list Malware-Hosts  type domain url https://malware-domains.example.com/list.txt  tag Security
```

---

### url — URL prefix list

The device blocks/allows HTTP/HTTPS requests to matching URL prefixes.

```text
set external-dynamic-list <name> type url url <fetch-url>
```

```text
set external-dynamic-list Phish-URLs   type url url https://openphish.com/feed.txt
set external-dynamic-list Block-URLs   type url url https://feeds.example.com/urls.txt  description "Phishing feed"
```

---

### imsi — IMSI identifier list (mobile subscribers)

Used in mobile network environments to block/allow by IMSI (International Mobile Subscriber Identity).

```text
set external-dynamic-list <name> type imsi url <fetch-url>
```

```text
set external-dynamic-list Block-IMSIs  type imsi url https://internal.example.com/bad-imsi.txt
```

---

### imei — IMEI identifier list (mobile equipment)

Used in mobile network environments to block/allow by IMEI (International Mobile Equipment Identity).

```text
set external-dynamic-list <name> type imei url <fetch-url>
```

```text
set external-dynamic-list Stolen-Devices  type imei url https://internal.example.com/stolen-imei.txt
```

---

## Fetch URL notes

The `url` field is where SCM/the device downloads the list content. The server must:
- Return plain text (one entry per line)
- Be reachable by the firewall or SCM service
- Support HTTP or HTTPS

---

## Optional fields

| Field | Type | Values | Description |
|---|---|---|---|
| `description` | string | — | Human-readable description |
| `tag` | list of strings | — | Tags to associate |
| `frequency` | keyword | `hourly` `daily` `weekly` `monthly` `5minute` | How often to refresh the list |

```text
set external-dynamic-list Threat-IPs  type ip url https://feed.example.com/ips.txt  description "Threat intel"  tag Security  frequency daily
```

---

## Full syntax

```text
set external-dynamic-list <name> type ip|domain|url|imsi|imei url <fetch-url>  [description <text>] [tag <name>] [frequency hourly|daily|weekly|monthly|5minute]
```

---

## Related commands

- `show external-dynamic-list` — list EDLs
- `delete external-dynamic-list <name>` — remove an EDL
