#!/usr/bin/env python3
"""Unit tests for app/api/sls.py and the SLS-backed log commands.

No SLS credentials exist in this environment, so the HTTP layer is replaced
with a scripted fake transport (same call surface as httpx.Client) — this
exercises the full job lifecycle (complete / failed / timeout), the SQL
query builder, error translation (401/403/404), and the operations.py
argument parser / row mapper / detail stash.

Run:  python dev/test_sls.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app.api import sls as sls_mod                      # noqa: E402
from app.api.sls import SLSClient, SLSError, build_query  # noqa: E402
from app.config import SCMConfig                        # noqa: E402
from app.commands import operations as ops              # noqa: E402

PASS = 0
FAIL = 0


def ok(msg: str) -> None:
    global PASS
    PASS += 1
    print(f"  ✓ {msg}")


def fail(msg: str, detail: str = "") -> None:
    global FAIL
    FAIL += 1
    print(f"  ✗ {msg}" + (f"\n      {detail}" if detail else ""))


def check(cond: bool, msg: str, detail: str = "") -> None:
    ok(msg) if cond else fail(msg, detail)


def expect_error(fn, contains: str, msg: str) -> None:
    try:
        fn()
    except (SLSError, ValueError) as exc:
        check(contains.lower() in str(exc).lower(), msg, f"got: {exc}")
    else:
        fail(msg, "no exception raised")


# ---------------------------------------------------------------------------
# Fake httpx-like transport
# ---------------------------------------------------------------------------

class FakeResponse:
    def __init__(self, status_code: int = 200, json_data=None, text: str = ""):
        self.status_code = status_code
        self._json = json_data if json_data is not None else {}
        self.text = text
        self.content = b"x" if json_data is not None else b""
        self.headers: dict = {}

    def json(self):
        return self._json

    def raise_for_status(self):
        if self.status_code >= 400:
            import httpx
            raise httpx.HTTPStatusError(
                f"{self.status_code}", request=None, response=None  # type: ignore[arg-type]
            )


class FakeHTTP:
    """Scripted stand-in for httpx.Client — records every request."""

    def __init__(self, script):
        # script: list of (method, path_substring, FakeResponse) consumed in order,
        # falling back to matching entries that may repeat.
        self.script = list(script)
        self.calls: list[tuple[str, str, dict]] = []

    def request(self, method, url, headers=None, params=None, json=None):
        self.calls.append((method, url, {"params": params, "json": json}))
        for index, (m, frag, resp) in enumerate(self.script):
            if m == method and frag in url:
                if len(self.script) > 1:
                    self.script.pop(index)
                return resp
        raise AssertionError(f"unexpected request: {method} {url}")

    def post(self, url, **kwargs):  # auth endpoint
        self.calls.append(("POST", url, kwargs))
        return FakeResponse(200, {"access_token": "tok"})


def make_client(script) -> tuple[SLSClient, FakeHTTP]:
    cfg = SCMConfig(bearer_token="test-token")   # skips the auth POST
    client = SLSClient(cfg, region="us", tenant_id="")
    fake = FakeHTTP(script)
    client._http = fake
    return client, fake


# ---------------------------------------------------------------------------
# 1. SQL query builder
# ---------------------------------------------------------------------------

print("\n== 1. build_query (SQL builder) ==")
NOW = 1_751_400_000  # fixed epoch for deterministic SQL

q1 = build_query("traffic", {"src": "10.1.1.5", "port": "443"},
                 limit=100, minutes_back=15, now=NOW)
check(
    q1 == "SELECT * FROM `firewall.traffic` "
          "WHERE time_generated >= 1751399100 AND source_ip.value = '10.1.1.5' "
          "AND dest_port = 443 ORDER BY time_generated DESC LIMIT 100",
    "traffic src+port last 15m", q1)

q2 = build_query("traffic", {"dst": "8.8.8.8", "rule": "Allow-Web", "app": "ssl"},
                 limit=500, minutes_back=120, tenant_id="2035xxxx", now=NOW)
check(
    q2 == "SELECT * FROM `2035xxxx.firewall.traffic` "
          "WHERE time_generated >= 1751392800 AND dest_ip.value = '8.8.8.8' "
          "AND rule_matched = 'Allow-Web' AND app = 'ssl' "
          "ORDER BY time_generated DESC LIMIT 500",
    "traffic dst+rule+app, tenant-qualified, last 2h limit 500", q2)

q3 = build_query("threat", {"app": "web-browsing"}, limit=9999, minutes_back=1440, now=NOW)
check(
    q3 == "SELECT * FROM `firewall.threat` "
          "WHERE time_generated >= 1751313600 AND app = 'web-browsing' "
          "ORDER BY time_generated DESC LIMIT 1000",
    "threat app filter, last 1d, limit capped at 1000", q3)

q4 = build_query("system", {}, limit=100, minutes_back=60, now=NOW)
check("`firewall.system`" in q4 and "time_generated >= 1751396400" in q4,
      "system logs — table + window only", q4)

q5 = build_query("traffic", {"rule": "o'brien"}, now=NOW)
check("rule_matched = 'o''brien'" in q5, "single quotes escaped in string filters", q5)

expect_error(lambda: build_query("system", {"src": "10.0.0.1"}, now=NOW),
             "not supported for 'system'", "system + src filter rejected")
expect_error(lambda: build_query("traffic", {"port": "https"}, now=NOW),
             "port must be a number", "non-numeric port rejected")
expect_error(lambda: build_query("url", {}, now=NOW),
             "unknown log type", "unknown log type rejected")

# ---------------------------------------------------------------------------
# 2. Job lifecycle — complete / failed / timeout
# ---------------------------------------------------------------------------

print("\n== 2. SLSClient job lifecycle ==")

# -- complete, with result pagination
client, fake = make_client([
    ("POST", "/query/v2/jobs", FakeResponse(201, {"jobId": "job-1"})),
    ("GET", "/query/v2/jobs/job-1", FakeResponse(200, {"jobId": "job-1", "state": "RUNNING"})),
    ("GET", "/query/v2/jobs/job-1", FakeResponse(200, {"jobId": "job-1", "state": "DONE"})),
    ("GET", "/query/v2/jobResults/job-1", FakeResponse(200, {
        "page": {"pageCursor": "c1", "result": {"data": [{"session_id": 1}, {"session_id": 2}]}}})),
    ("GET", "/query/v2/jobResults/job-1", FakeResponse(200, {
        "page": {"pageCursor": None, "result": {"data": [{"session_id": 3}]}}})),
])
job_id = client.query_start("SELECT 1")
check(job_id == "job-1", "query_start returns jobId")
final = client.wait(job_id, timeout_s=5, interval_s=0)
check(final.get("state") == "DONE", "wait polls RUNNING → DONE")
rows = client.query_results(job_id)
check(rows == [{"session_id": 1}, {"session_id": 2}, {"session_id": 3}],
      "query_results follows pageCursor across pages", repr(rows))
check(fake.calls[0][2]["json"] == {"params": {"query": "SELECT 1"}},
      "POST body wraps SQL in params.query", repr(fake.calls[0][2]["json"]))

# -- failed job surfaces the server message
client, fake = make_client([
    ("GET", "/query/v2/jobs/job-2",
     FakeResponse(200, {"jobId": "job-2", "state": "FAILED", "message": "table not found"})),
])
expect_error(lambda: client.wait("job-2", timeout_s=5, interval_s=0),
             "table not found", "FAILED job raises SLSError with server message")

# -- timeout cancels the job and says how to narrow the query
client, fake = make_client([
    ("GET", "/query/v2/jobs/job-3", FakeResponse(200, {"jobId": "job-3", "state": "RUNNING"})),
    ("GET", "/query/v2/jobs/job-3", FakeResponse(200, {"jobId": "job-3", "state": "RUNNING"})),
    ("DELETE", "/query/v2/jobs/job-3", FakeResponse(200, {})),
])
expect_error(lambda: client.wait("job-3", timeout_s=0, interval_s=0),
             "did not finish", "stuck job raises timeout SLSError")
check(any(m == "DELETE" for m, _, _ in fake.calls), "timeout issues a best-effort cancel")

# -- end-to-end query_logs sends the built SQL
client, fake = make_client([
    ("POST", "/query/v2/jobs", FakeResponse(201, {"jobId": "job-4"})),
    ("GET", "/query/v2/jobs/job-4", FakeResponse(200, {"state": "DONE"})),
    ("GET", "/query/v2/jobResults/job-4", FakeResponse(200, {
        "page": {"pageCursor": None, "result": {"data": [{"app": "ssl"}]}}})),
])
rows = client.query_logs("traffic", {"app": "ssl"}, limit=10, minutes_back=5,
                         timeout_s=5, poll_interval_s=0)
sent_sql = fake.calls[0][2]["json"]["params"]["query"]
check(rows == [{"app": "ssl"}], "query_logs returns result rows")
check("`firewall.traffic`" in sent_sql and "app = 'ssl'" in sent_sql and "LIMIT 10" in sent_sql,
      "query_logs submits the built SQL", sent_sql)

# ---------------------------------------------------------------------------
# 3. Error translation — actionable messages
# ---------------------------------------------------------------------------

print("\n== 3. Error translation ==")

client, _ = make_client([("POST", "/query/v2/jobs", FakeResponse(403, {}, text="forbidden"))])
expect_error(lambda: client.query_start("SELECT 1"),
             "logging service role", "403 → mentions Logging Service role/scope")

client, _ = make_client([("POST", "/query/v2/jobs", FakeResponse(404, {}, text="nope"))])
expect_error(lambda: client.query_start("SELECT 1"),
             "arc_sls_region", "404 → suggests checking ARC_SLS_REGION")

client, _ = make_client([("POST", "/query/v2/jobs", FakeResponse(201, {}))])
expect_error(lambda: client.query_start("SELECT 1"),
             "did not return a job id", "missing jobId in response is reported")

try:
    SLSClient(SCMConfig())
except SLSError as exc:
    check("scm_client_id" in str(exc).lower() or "scm credentials" in str(exc).lower(),
          "unconfigured SCMConfig → actionable SLSError", str(exc))
else:
    fail("unconfigured SCMConfig → actionable SLSError", "no exception raised")

# ---------------------------------------------------------------------------
# 4. operations.py — arg parsing, row mapping, detail stash
# ---------------------------------------------------------------------------

print("\n== 4. show log handlers (operations.py) ==")

filters, limit, minutes = ops._parse_log_args(
    {"_remainder": ["src", "10.1.1.5", "port", "443", "last", "15m", "limit", "2000"]})
check(filters == {"src": "10.1.1.5", "port": "443"} and limit == 1000 and minutes == 15,
      "arg parser: filters + last 15m + limit capped at 1000",
      f"{filters} limit={limit} minutes={minutes}")

filters, limit, minutes = ops._parse_log_args({"_remainder": []})
check(filters == {} and limit == 100 and minutes == 60,
      "arg parser defaults: last 1h, limit 100")

check(ops._parse_log_window("2h") == 120 and ops._parse_log_window("1d") == 1440
      and ops._parse_log_window("30m") == 30, "window parser: Nm/Nh/Nd")

expect_error(lambda: ops._parse_log_args({"_remainder": ["srcc", "1.2.3.4"]}),
             "usage: show log", "unknown keyword → usage message")
expect_error(lambda: ops._parse_log_args({"_remainder": ["src"]}),
             "needs a value", "dangling keyword → usage message")
expect_error(lambda: ops._parse_log_window("soon"),
             "bad time window", "bad window rejected")

sls_row = {
    "time_generated": 1751400000,
    "source_ip": {"value": "10.1.1.5"},
    "dest_ip": {"value": "8.8.8.8"},
    "dest_port": 443,
    "app": "ssl",
    "action": {"value": "allow"},
    "rule_matched": "Allow-Web",
    "session_id": 42,
}
mapped = ops._map_sls_row("traffic", sls_row)
check(mapped["src"] == "10.1.1.5" and mapped["dst"] == "8.8.8.8"
      and mapped["app"] == "ssl" and mapped["action"] == "allow"
      and mapped["rule"] == "Allow-Web" and mapped["port"] == 443,
      "row mapper unwraps SLS {'value': …} records → src/dst/app/action/rule", repr(mapped))
check(mapped["time"] == "2025-07-01 20:00:00Z", "epoch time_generated → readable UTC",
      mapped["time"])
check(list(mapped)[:3] == ["time", "src", "dst"]
      and list(mapped)[3:6] == ["app", "action", "rule"],
      "mapped key order puts app/action/rule in the rendered columns")

threat_mapped = ops._map_sls_row("threat", {**sls_row, "severity": "critical",
                                            "threat_name": "Log4Shell"})
check(threat_mapped["severity"] == "critical" and threat_mapped["description"] == "Log4Shell",
      "threat rows add severity + threat name")

# detail stash — module-level _LAST_ROWS
ops._LAST_ROWS[:] = [sls_row]
ops._LAST_QUERY_DESC = "traffic (last 60m)"
detail = ops._show_log_detail(None, {"id": "1"})
check(detail is sls_row, "show log detail 1 returns the FULL raw record")
expect_error(lambda: ops._show_log_detail(None, {"id": "9"}),
             "show log detail <n>", "out-of-range detail index → usage")
ops._LAST_ROWS.clear()
expect_error(lambda: ops._show_log_detail(None, {"id": "1"}),
             "run a query first", "detail with no prior query → actionable message")

# handler wiring
from app.commands.registry import COMMANDS, match_command  # noqa: E402
for key in ("show log traffic", "show log threat", "show log system", "show log detail"):
    cmd = COMMANDS.get(key)
    if cmd is None:
        fail(f"{key} registered")
        continue
    check(cmd.feature_flag == "sls_logs" and cmd.render in ("logs", "dict"),
          f"{key}: feature_flag=sls_logs, render={cmd.render}")
mk, mdef, margs = match_command(["show", "log", "traffic", "src", "10.0.0.1", "last", "2h"])
check(mk == "show log traffic"
      and margs["_remainder"] == ["src", "10.0.0.1", "last", "2h"],
      "match_command routes filters to the traffic handler", f"{mk} {margs.get('_remainder')}")
check(COMMANDS["show log traffic"].ssh_command == "show log traffic"
      and COMMANDS["show log threat"].ssh_command == "show log threat"
      and COMMANDS["show log system"].ssh_command == "show log system",
      "--remote SSH path kept on all three log commands")

# ---------------------------------------------------------------------------

print(f"\n{'=' * 60}\nSLS tests: {PASS} passed, {FAIL} failed")
sys.exit(1 if FAIL else 0)
