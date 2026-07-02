"""Strata Logging Service (SLS, formerly Cortex Data Lake) query client.

Fleet-wide log queries — traffic / threat / system — across every firewall
that forwards logs to the tenant's SLS instance.

SPEC PROVENANCE
    The pan.dev repo (PaloAltoNetworks/pan.dev, master) publishes NO OpenAPI
    spec for the SLS / CDL Query Service — checked 2026-07 via the GitHub
    tree API (the only CDL specs are openapi-specs/cdl/logforwarding/*).
    This client therefore implements the documented CDL Query Service v2
    REST contract (https://pan.dev/cdl/ — "Query Service"):

        POST   /query/v2/jobs                 create a SQL query job
        GET    /query/v2/jobs/{jobId}         poll job state
        GET    /query/v2/jobResults/{jobId}   page finished results
        DELETE /query/v2/jobs/{jobId}         cancel a job

    Base URL is regional:  https://api.{region}.cdl.paloaltonetworks.com
    (region default "us"; override with env ARC_SLS_REGION, e.g. "nl", "uk",
    "sg", "jp", "au", "ca", "de", "in", "ch", "pl", "fr", "qa", "il", "sa",
    "id", "tw", "kr", "es", "it").

AUTH
    Same TSG-scoped OAuth client-credentials flow as SCMClient
    (auth.apps.paloaltonetworks.com) — see app/api/client.py.  The service
    account must additionally hold a Logging Service role for the tenant;
    a config-only SCM role yields 403 here.

QUERY LANGUAGE
    SQL over the tenant's log tables, e.g.

        SELECT * FROM `firewall.traffic`
        WHERE time_generated >= 1751400000 AND source_ip.value = '10.1.1.5'
        ORDER BY time_generated DESC LIMIT 100

    When a CDL instance ID is known (env ARC_SLS_TENANT_ID) the table is
    fully qualified as `<tenant>.firewall.traffic` per the documented
    examples; otherwise the token's tenant scope resolves the bare name.
"""

from __future__ import annotations

import os
import time
from typing import Any, Optional

import httpx

from app.config import SCMConfig


class SLSError(Exception):
    """Raised when SLS authentication, query submission, or polling fails."""


# ---------------------------------------------------------------------------
# SQL query builder — pure function, unit-testable without a client
# ---------------------------------------------------------------------------

# Filter keyword → SLS column expression, per log type.  Traffic and threat
# share the firewall session schema; system logs have no session fields, so
# an unsupported filter raises instead of silently returning everything.
_SESSION_FIELDS: dict[str, str] = {
    "src":  "source_ip.value",
    "dst":  "dest_ip.value",
    "port": "dest_port",
    "rule": "rule_matched",
    "app":  "app",
}

FILTER_FIELDS: dict[str, dict[str, str]] = {
    "traffic": _SESSION_FIELDS,
    "threat":  _SESSION_FIELDS,
    "system":  {},   # firewall.system has no src/dst/port/rule/app columns
}

#: Log types this client knows how to query.
LOG_TABLES: dict[str, str] = {
    "traffic": "firewall.traffic",
    "threat":  "firewall.threat",
    "system":  "firewall.system",
}

MAX_LIMIT = 1000


def _sql_quote(value: str) -> str:
    """Return *value* as a single-quoted SQL string literal ('' escaping)."""
    return "'" + str(value).replace("'", "''") + "'"


def build_query(
    log_type: str,
    filters: dict[str, Any],
    *,
    limit: int = 100,
    minutes_back: int = 60,
    tenant_id: str = "",
    now: Optional[float] = None,
) -> str:
    """Build the SLS SQL statement for a log query.

    *filters* keys come from the shell syntax (src/dst/port/rule/app) and are
    translated to SLS column names per *log_type*.  Unknown filter keys and
    non-numeric ports raise SLSError so the operator gets a message, not an
    empty result.  *now* is injectable for tests (epoch seconds).
    """
    table = LOG_TABLES.get(log_type)
    if table is None:
        raise SLSError(
            f"Unknown log type {log_type!r} — supported: {', '.join(sorted(LOG_TABLES))}."
        )
    if tenant_id:
        table = f"{tenant_id}.{table}"

    limit = max(1, min(int(limit), MAX_LIMIT))
    since = int((now if now is not None else time.time()) - minutes_back * 60)
    clauses = [f"time_generated >= {since}"]

    field_map = FILTER_FIELDS[log_type]
    for key, value in filters.items():
        if value in (None, ""):
            continue
        column = field_map.get(key)
        if column is None:
            raise SLSError(
                f"Filter {key!r} is not supported for '{log_type}' logs — "
                f"supported filters: {', '.join(sorted(field_map)) or '(none)'}."
            )
        if key == "port":
            try:
                clauses.append(f"{column} = {int(str(value))}")
            except ValueError:
                raise SLSError(f"Port must be a number, got {value!r}.") from None
        else:
            clauses.append(f"{column} = {_sql_quote(value)}")

    return (
        f"SELECT * FROM `{table}` "
        f"WHERE {' AND '.join(clauses)} "
        f"ORDER BY time_generated DESC LIMIT {limit}"
    )


# ---------------------------------------------------------------------------
# Client
# ---------------------------------------------------------------------------

class SLSClient:
    """Strata Logging Service Query Service v2 client.

    Constructed from the same SCMConfig used by SCMClient and authenticates
    with the identical OAuth client-credentials flow (TSG-scoped token).
    """

    # pan.dev: openapi-specs/scm/auth/AuthService.yaml (same endpoint SCMClient uses)
    AUTH_URL = "https://auth.apps.paloaltonetworks.com/auth/v1/oauth2/access_token"

    # Documented CDL Query Service v2 gateway — regional.
    BASE_URL_TEMPLATE = "https://api.{region}.cdl.paloaltonetworks.com"

    # Job states per the documented contract.
    _DONE_STATES   = {"DONE"}
    _FAILED_STATES = {"FAILED", "CANCELED", "CANCELLED", "TIMED_OUT"}

    def __init__(
        self,
        cfg: SCMConfig,
        *,
        region: str = "",
        tenant_id: str = "",
    ) -> None:
        self._cfg = cfg
        self.region = region or os.environ.get("ARC_SLS_REGION", "us")
        self.tenant_id = tenant_id or os.environ.get("ARC_SLS_TENANT_ID", "")
        self.base_url = self.BASE_URL_TEMPLATE.format(region=self.region)
        self._http = httpx.Client(timeout=30)
        self._token: str = ""

        # Same auth priority as SCMClient: client credentials preferred,
        # pre-issued bearer token as fallback.
        if cfg.client_id and cfg.client_secret and cfg.tsg_id:
            self._authenticate()
        elif cfg.bearer_token.strip():
            self._token = cfg.bearer_token.strip()
        else:
            raise SLSError(
                "SLS needs SCM credentials. Set SCM_CLIENT_ID / SCM_CLIENT_SECRET / "
                "SCM_TSG_ID (recommended) or SCM_BEARER_TOKEN, then retry."
            )

    # -- auth ----------------------------------------------------------------

    def _authenticate(self) -> None:
        """OAuth client-credentials flow — mirrors SCMClient._authenticate."""
        resp = self._http.post(
            self.AUTH_URL,
            data={
                "grant_type": "client_credentials",
                "scope": f"tsg_id:{self._cfg.tsg_id}",
            },
            auth=(self._cfg.client_id, self._cfg.client_secret),
        )
        try:
            resp.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise SLSError(
                f"SLS authentication failed: {exc}. Verify SCM_CLIENT_ID / "
                "SCM_CLIENT_SECRET / SCM_TSG_ID (same credentials SCM uses)."
            ) from exc
        self._token = resp.json().get("access_token", "")
        if not self._token:
            raise SLSError("SLS auth returned no access_token.")

    def _headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self._token}"}

    # -- HTTP core -----------------------------------------------------------

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[dict] = None,
        json: Any = None,
    ) -> Any:
        """Send one Query Service request; translate failures into SLSError."""
        can_reauth = bool(
            self._cfg.client_id and self._cfg.client_secret and self._cfg.tsg_id
        )
        reauthed = False
        while True:
            try:
                resp = self._http.request(
                    method,
                    f"{self.base_url}{path}",
                    headers=self._headers(),
                    params=params,
                    json=json,
                )
            except httpx.HTTPError as exc:
                raise SLSError(
                    f"Cannot reach SLS at {self.base_url}: {exc}. "
                    "Check network/VPN, and that ARC_SLS_REGION matches your "
                    f"tenant's SLS region (current: {self.region!r})."
                ) from exc
            if resp.status_code == 401 and not reauthed and can_reauth:
                reauthed = True
                self._authenticate()
                continue
            break

        if resp.status_code in (401, 403):
            raise SLSError(
                f"SLS rejected the request ({resp.status_code}). SLS may need the "
                "Logging Service role/scope on your service account — check with: "
                "hub.paloaltonetworks.com → Identity & Access → your service "
                "account → assign a Logging Service / Strata Logging Service role "
                "for this tenant. An SCM config-only role cannot query logs."
            )
        if resp.status_code == 404:
            raise SLSError(
                f"SLS endpoint not found ({method} {path}) — the tenant may have "
                f"no SLS instance in region {self.region!r}. Set ARC_SLS_REGION "
                "to your tenant's region (e.g. us, nl, uk, sg, jp) and retry."
            )
        try:
            resp.raise_for_status()
        except httpx.HTTPStatusError as exc:
            detail = " ".join((resp.text or "").split())[:200]
            raise SLSError(
                f"SLS API error ({resp.status_code}): {detail or exc}"
            ) from exc
        return resp.json() if resp.content else {}

    # -- Query Service v2 job lifecycle ---------------------------------------

    def query_start(self, sql_or_query: str | dict) -> str:
        """POST /query/v2/jobs — submit a SQL string (or a raw params dict).

        Returns the job ID.
        """
        if isinstance(sql_or_query, str):
            body: dict = {"params": {"query": sql_or_query}}
        else:
            body = sql_or_query if "params" in sql_or_query else {"params": sql_or_query}
        data = self._request("POST", "/query/v2/jobs", json=body)
        job_id = str(data.get("jobId") or data.get("id") or "")
        if not job_id:
            raise SLSError(f"SLS did not return a job ID for the query (got: {data!r}).")
        return job_id

    def query_poll(self, job_id: str) -> dict:
        """GET /query/v2/jobs/{jobId} — return the job record (incl. 'state')."""
        data = self._request("GET", f"/query/v2/jobs/{job_id}")
        return data if isinstance(data, dict) else {}

    def query_results(
        self,
        job_id: str,
        *,
        page_size: int = MAX_LIMIT,
        max_rows: int = MAX_LIMIT,
    ) -> list[dict]:
        """GET /query/v2/jobResults/{jobId} — collect result rows (paged).

        Follows ``page.pageCursor`` until exhausted or *max_rows* is reached.
        """
        rows: list[dict] = []
        cursor: Optional[str] = None
        while True:
            params: dict[str, Any] = {
                "resultFormat": "valuesDictionary",
                "pageSize": min(page_size, max_rows - len(rows)),
            }
            if cursor:
                params["pageCursor"] = cursor
            data = self._request("GET", f"/query/v2/jobResults/{job_id}", params=params)
            page = data.get("page") or {}
            result = page.get("result") or {}
            batch = result.get("data") or []
            rows.extend(r for r in batch if isinstance(r, dict))
            cursor = page.get("pageCursor")
            if not cursor or not batch or len(rows) >= max_rows:
                break
        return rows[:max_rows]

    def query_cancel(self, job_id: str) -> None:
        """DELETE /query/v2/jobs/{jobId} — best-effort cancel."""
        try:
            self._request("DELETE", f"/query/v2/jobs/{job_id}")
        except SLSError:
            pass  # cancel is a courtesy on timeout — never mask the real error

    def wait(self, job_id: str, *, timeout_s: float = 60.0, interval_s: float = 1.0) -> dict:
        """Poll until the job reaches a terminal state; return the final record."""
        deadline = time.monotonic() + timeout_s
        while True:
            job = self.query_poll(job_id)
            state = str(job.get("state", "")).upper()
            if state in self._DONE_STATES:
                return job
            if state in self._FAILED_STATES:
                message = (
                    job.get("message")
                    or (job.get("error") or {}).get("message")
                    or "no error detail from SLS"
                )
                raise SLSError(f"SLS query job {job_id} {state}: {message}")
            if time.monotonic() >= deadline:
                self.query_cancel(job_id)
                raise SLSError(
                    f"SLS query job {job_id} did not finish within {timeout_s:.0f}s "
                    f"(last state: {state or 'unknown'}). Narrow the time window "
                    "('last 15m') or add filters (src/dst/app) and retry."
                )
            time.sleep(interval_s)

    # -- High-level entry point ------------------------------------------------

    def query_logs(
        self,
        log_type: str,
        filters: dict[str, Any],
        *,
        limit: int = 100,
        minutes_back: int = 60,
        timeout_s: float = 60.0,
        poll_interval_s: float = 1.0,
    ) -> list[dict]:
        """Run one fleet-wide log query end to end and return the rows.

        Builds the SQL from *filters* (src/dst/port/rule/app), submits the
        job, waits for completion, and pages the results.
        """
        sql = build_query(
            log_type,
            filters,
            limit=limit,
            minutes_back=minutes_back,
            tenant_id=self.tenant_id,
        )
        job_id = self.query_start(sql)
        self.wait(job_id, timeout_s=timeout_s, interval_s=poll_interval_s)
        return self.query_results(job_id, max_rows=max(1, min(int(limit), MAX_LIMIT)))
