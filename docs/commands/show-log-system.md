---
command: "show log system"
description: "Fleet-wide system log via SLS (lags minutes) — --remote for real-time on one device"
usage: "show log system [last <Nm|Nh|Nd>] [limit <n>]"
feature_flag: sls_logs
category: operations
scope: global
api: "(live device state — SSH via --remote)"
---

---
command: "show log system"
description: "Fleet-wide system log via SLS (lags minutes) — --remote for real-time on one device"
usage: "show log system [last <Nm|Nh|Nd>] [limit <n>]"
feature_flag: sls_logs
category: operations
scope: global
api: "(live device state — SSH via --remote)"
---

---
command: "show log system"
description: "Fleet-wide system log via SLS (lags minutes) — --remote for real-time on one device"
usage: "show log system [last <Nm|Nh|Nd>] [limit <n>]"
feature_flag: sls_logs
category: operations
scope: global
api: "SLS Query Service v2 — POST /query/v2/jobs (SQL over firewall.system)"
---

# show log system

Query the system log **fleet-wide** through the Strata Logging Service (SLS).
SLS is fleet-wide but ingestion lags minutes behind; use `--remote` for
real-time on one device. Full record: `show log detail <n>`; filter rendered
output with `| match <text>`. See `help show log traffic` for the full guide.

## Category

logs

## Default path

API mode through SCM REST when a translation exists; otherwise use SSH for live device output.

## Remote behavior

Supported

## Examples

```text
show log system
```

## Notes

Use `pwd` to confirm the current device and mode before running device-scoped commands.
