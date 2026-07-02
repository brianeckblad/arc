---
command: "show config format set"
description: "Dump folder config as replayable set commands"
usage: "show config format set [address|address-group|service|service-group|tag|external-dynamic-list]"
feature_flag: config_view
category: operations
scope: folder
api: "GET /config/objects/v1/<resource>?folder=<active>"
---

# show config format set

Dump the **active folder's configuration as replayable `set` commands** —
the PAN-OS `show config … format set` experience for SCM. Every emitted line
replays through the corresponding curated `set` command in configure mode.

```
arc:Production > show config format set
set address WebServer ip-netmask 10.1.2.3/32
set address DMZ-Subnet ip-netmask 10.1.0.0/24 description "DMZ network" tag Production,DMZ
set address-group WebServers static web1 web2
set service HTTPS tcp port 443
set service-group Web-Services members HTTP HTTPS
set tag Production color "Forest Green" comments "Prod objects"
set external-dynamic-list Bad-IPs type ip url https://feeds.example.com/bad-ips frequency daily
```

Values containing spaces are double-quoted; list fields (tags) are
comma-joined. Only objects **defined in the active folder** are included —
objects inherited from ancestor folders or predefined snippets are skipped so
the dump replays cleanly.

## Single resource

```
arc:Production > show config format set address
arc:Production > show config format set tag
```

Supported resources: `address`, `address-group`, `service`, `service-group`,
`tag`, `external-dynamic-list` (aliases: plurals and `edl` accepted).

## Piping

Output is plain text lines, so PAN-OS-style filters apply naturally:

```
arc:Production > show config format set | match 10.1.
arc:Production > show config format set address | except fqdn
```

## Related

- `show config running <resource>` — same format, one resource
- `set address` / `set service` / … — the commands each line replays through
