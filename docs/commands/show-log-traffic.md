---
command: "show log traffic"
description: "Fleet-wide traffic log via SLS (lags minutes) — --remote for real-time on one device"
usage: "show log traffic [src <ip>] [dst <ip>] [port <n>] [rule <name>] [app <name>] [last <Nm|Nh|Nd>] [limit <n>]"
feature_flag: sls_logs
category: operations
scope: global
api: "SLS Query Service v2 — POST /query/v2/jobs (SQL over firewall.traffic)"
---

# show log traffic

Query the **traffic log fleet-wide** through the Strata Logging Service (SLS,
formerly Cortex Data Lake) — one query covers every firewall that forwards
logs to your tenant's SLS instance. No device context is needed.

**SLS is fleet-wide but ingestion lags minutes behind; use `--remote` for
real-time on one device.**

## Filters

All filters are optional `keyword value` pairs, in any order:

| Filter  | Meaning                             | Example          |
|---------|-------------------------------------|------------------|
| `src`   | Source IP                           | `src 10.1.1.5`   |
| `dst`   | Destination IP                      | `dst 8.8.8.8`    |
| `port`  | Destination port                    | `port 443`       |
| `rule`  | Security rule that matched          | `rule Allow-Web` |
| `app`   | Application                         | `app ssl`        |
| `last`  | Time window `Nm`/`Nh`/`Nd` (default `1h`) | `last 15m` |
| `limit` | Max rows, default 100, cap 1000     | `limit 500`      |

## Examples

```text
show log traffic
show log traffic src 10.1.1.5 last 15m
show log traffic dst 8.8.8.8 port 443 last 2h limit 500
show log traffic app ssl rule Allow-Web last 1d
show log traffic src 10.1.1.5 | match deny
show log traffic last 30m | match 10.2.0. | count
```

The table shows time / src / dst / app / action / rule. Narrow the rendered
output with the standard pipe filters: `| match <text>`, `| except <text>`,
`| count`, or `| json` for the raw records.

## Detail view

Each row keeps its **full SLS record** for the rest of the session. Row 1 is
the top (newest) row of the last table:

```text
show log traffic src 10.1.1.5 last 1h
show log detail 3          # full record for row 3 of that result
```

## SLS vs --remote

| Path                        | Coverage            | Freshness              |
|-----------------------------|---------------------|------------------------|
| `show log traffic` (SLS)    | Whole fleet         | Lags ingestion by minutes |
| `show log traffic --remote` | One device (SSH)    | Real-time              |

Use SLS to hunt across every firewall at once; use `--remote` when you are
watching a single device live (requires a device context — `cd <device>`).

## Requirements

- SCM credentials (`SCM_CLIENT_ID` / `SCM_CLIENT_SECRET` / `SCM_TSG_ID`) — the
  same OAuth flow the rest of ARC uses.
- The service account needs a **Logging Service role** for the tenant
  (hub.paloaltonetworks.com → Identity & Access). An SCM config-only role
  returns 403.
- If your SLS instance is not in the US region, set `ARC_SLS_REGION`
  (e.g. `nl`, `uk`, `sg`, `jp`). Optionally set `ARC_SLS_TENANT_ID` to your
  CDL instance ID to fully qualify table names.

## Notes

- Related: `show log threat`, `show log system`, `show log detail <n>`.
- Feature flag: `sls_logs`.
