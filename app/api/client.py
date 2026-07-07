"""Strata Cloud Manager REST API client.

All endpoint paths and base URLs are sourced directly from the pan.dev
OpenAPI specifications:

  https://pan.app/scripts/scm/api/

Gateway map (from the OpenAPI ``servers`` field in each spec):

  Objects  (addresses, services, tags, …)
    https://api.strata.paloaltonetworks.com/config/objects/v1
    Spec: openapi-specs/scm/config/ngfw/objects/objects_v1.3_feb.yaml

  Security (security-rules, url-categories, decryption, …)
    https://api.strata.paloaltonetworks.com/config/security/v1
    Spec: openapi-specs/scm/config/ngfw/security/security-services-R2-2026.yaml

  Setup    (devices, folders, snippets, labels, jobs, …)
    https://api.strata.paloaltonetworks.com/config/setup/v1
    Spec: openapi-specs/scm/config/ngfw/setup/config-setup-feb-v1.yaml

  Network  (interfaces, zones, routing, HA, …)
    https://api.strata.paloaltonetworks.com/config/network/v1
    Spec: openapi-specs/scm/config/ngfw/network/  (verify exact file at pan.dev)

  IAM / Tenancy
    https://api.sase.paloaltonetworks.com
    Spec: openapi-specs/scm/iam/ServiceAccounts.yaml
          openapi-specs/scm/tenancy/TenantServiceGroup.yaml

  Authentication
    https://auth.apps.paloaltonetworks.com/auth/v1/oauth2/access_token
    Spec: openapi-specs/scm/auth/AuthService.yaml
"""

from __future__ import annotations

import time
from typing import Any, Optional

import httpx

from app.api._auth import oauth_token
from app.config import SCMConfig


class SCMError(Exception):
    """Raised when SCM authentication or API requests fail."""


class SCMClient:
    """Strata Cloud Manager (SCM) REST API client.

    Uses three separate base URLs sourced from pan.dev OpenAPI specs —
    all share the same OAuth bearer token.
    """

    # pan.dev: openapi-specs/scm/auth/AuthService.yaml
    AUTH_URL = "https://auth.apps.paloaltonetworks.com/auth/v1/oauth2/access_token"

    # pan.dev: openapi-specs/scm/config/ngfw/objects/objects_v1.3_feb.yaml
    OBJECTS_URL = "https://api.strata.paloaltonetworks.com/config/objects/v1"

    # pan.dev: openapi-specs/scm/config/ngfw/security/security-services-R2-2026.yaml
    SECURITY_URL = "https://api.strata.paloaltonetworks.com/config/security/v1"

    # pan.dev: openapi-specs/scm/config/ngfw/setup/config-setup-feb-v1.yaml
    SETUP_URL = "https://api.strata.paloaltonetworks.com/config/setup/v1"

    # pan.dev: openapi-specs/scm/config/ngfw/network/  (verify exact spec file at pan.dev)
    NETWORK_URL = "https://api.strata.paloaltonetworks.com/config/network/v1"

    # pan.dev: openapi-specs/scm/config/ngfw/identity/identity-services-march.yaml
    IDENTITY_URL = "https://api.strata.paloaltonetworks.com/config/identity/v1"

    # pan.dev: openapi-specs/scm/config/ngfw/operations/config-operations-march.yaml
    OPERATIONS_URL = "https://api.strata.paloaltonetworks.com/config/operations/v1"

    # pan.dev: openapi-specs/scm/config/ngfw-operations/operations-R2-2026.yaml
    # Live-device operational data over SCM's device management tunnel
    # (async jobs: POST jobs/<op> -> poll device/jobs/{id}). No SSH involved.
    NGFW_OPS_URL = "https://api.strata.paloaltonetworks.com/operations/v1"

    # pan.dev: openapi-specs/scm/iam/ServiceAccounts.yaml
    #          openapi-specs/scm/tenancy/TenantServiceGroup.yaml
    IAM_URL = "https://api.sase.paloaltonetworks.com"

    # Keep BASE_URL pointing at the sase gateway for backward-compat with
    # any callers that use the generic .get() / .post() methods directly.
    BASE_URL = "https://api.sase.paloaltonetworks.com"

    def __init__(self, cfg: SCMConfig) -> None:
        self._cfg = cfg
        self._http = httpx.Client(timeout=30)
        self._token: str = ""
        # Optional progress callback — set by the execution layer during paginated
        # fetches so the spinner text updates as pages arrive.  Signature:
        #   _page_reporter(fetched_so_far: int, total: int) -> None
        self._page_reporter: Optional[callable] = None

        # Auth priority:
        #   1. OAuth client credentials (client_id + client_secret + tsg_id) — always
        #      preferred; produces a fresh token scoped to the correct TSG.
        #   2. Pre-issued bearer token — only when no client credentials exist.
        if cfg.client_id and cfg.client_secret and cfg.tsg_id:
            self._authenticate()
        elif cfg.bearer_token.strip():
            self._token = cfg.bearer_token.strip()
        else:
            # Produce a specific message identifying which field is missing so
            # the operator knows exactly what to fix rather than a generic error.
            missing: list[str] = []
            if not cfg.client_id:
                missing.append("client_id")
            if not cfg.client_secret:
                missing.append("client_secret")
            if not cfg.tsg_id:
                missing.append("tsg_id")
            if missing and not cfg.bearer_token:
                raise SCMError(
                    f"SCM is not configured — missing: {', '.join(missing)}. "
                    "Run [bold]arc auth configure[/bold] to set up credentials, "
                    "or provide them via environment variables "
                    "(SCM_CLIENT_ID / SCM_CLIENT_SECRET / SCM_TSG_ID)."
                )
            raise SCMError(
                "SCM is not configured. Provide client_id + client_secret + tsg_id "
                "(recommended), or a pre-issued SCM_BEARER_TOKEN."
            )

    def _authenticate(self) -> None:
        """Obtain an OAuth token via the client-credentials flow.

        pan.dev ref: https://pan.app/scripts/scm/api/auth/post-auth-v-1-oauth-2-access-token/
        """
        if not (self._cfg.client_id and self._cfg.client_secret and self._cfg.tsg_id):
            raise SCMError(
                "SCM is not configured. Set SCM_BEARER_TOKEN, or set "
                "SCM_CLIENT_ID / SCM_CLIENT_SECRET / SCM_TSG_ID."
            )
        try:
            self._token = oauth_token(
                self._http, self._cfg.client_id, self._cfg.client_secret, self._cfg.tsg_id
            )
        except httpx.HTTPStatusError as exc:
            raise SCMError(f"SCM authentication failed: {exc}") from exc
        except ValueError as exc:
            raise SCMError(f"SCM auth: {exc}.") from exc

    def _headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self._token}"}

    # ------------------------------------------------------------------
    # Generic request helpers
    # ------------------------------------------------------------------

    def _request(
        self,
        method: str,
        base_url: str,
        path: str,
        *,
        params: Optional[dict] = None,
        json: Any = None,
    ) -> Any:
        """Single HTTP core behind every per-domain wrapper.

        Sends *method* to ``base_url + path`` with the bearer token, raises
        httpx.HTTPStatusError on 4xx/5xx, and returns the parsed JSON body
        (or {} when the response has no content, e.g. 204 on DELETE).

        A 401 mid-session usually means the OAuth token expired: when client
        credentials are configured, re-authenticate once and retry (a loop,
        not recursion, so a swapped-in ``_request`` never re-enters itself).

        A 429 (rate limited) is retried up to 3 times, sleeping for the
        ``Retry-After`` header value when present and sane, else
        ``2.0 * attempt`` seconds — always capped at 15s.
        """
        can_reauth = bool(
            self._cfg.client_id and self._cfg.client_secret and self._cfg.tsg_id
        )
        reauthed = False
        rate_limit_retries = 0
        while True:
            resp = self._http.request(
                method,
                f"{base_url}{path}",
                headers=self._headers(),
                params=params,
                json=json,
            )
            if resp.status_code == 401 and not reauthed and can_reauth:
                reauthed = True
                self._authenticate()
                continue
            if resp.status_code == 429 and rate_limit_retries < 3:
                rate_limit_retries += 1
                delay = 2.0 * rate_limit_retries
                retry_after = resp.headers.get("Retry-After")
                if retry_after is not None:
                    try:
                        # Accept both float ("1.5") and integer ("60") values.
                        parsed = float(retry_after)
                        if parsed >= 0:
                            delay = parsed
                    except ValueError:
                        pass
                # Cap at 120s so we always respect reasonable Retry-After values
                # (SCM can legitimately say "wait 60s") without an unbounded wait.
                time.sleep(min(delay, 120.0))
                continue
            break
        resp.raise_for_status()
        return resp.json() if resp.content else {}

    # Safety cap on pagination requests per collection (first page included).
    _MAX_LIST_PAGES = 50

    def _collect_pages(
        self,
        base_url: str,
        path: str,
        params: Optional[dict],
        first: dict,
        on_page: Optional[callable] = None,
    ) -> list[dict]:
        """Follow limit/offset pagination after an already-fetched first page.

        *first* must be a dict whose ``data`` value is a list.  When the
        server-reported ``total`` exceeds the first page, keep requesting
        with explicit ``limit``/``offset`` until all ``total`` items are
        collected, a page comes back empty, or the page-count safety cap is
        hit (in which case whatever was fetched is returned — no exception).
        *params* is copied before mutation.

        *on_page*, if provided, is called after each follow-on page fetch with
        ``(fetched_so_far, total)`` so callers can update a progress display.
        """
        items: list[dict] = list(first["data"])
        total = first.get("total")
        if not isinstance(total, int) or total <= len(items):
            return items
        limit = first.get("limit")
        if not isinstance(limit, int) or limit <= 0:
            limit = len(items) or 200
        query = dict(params or {})
        pages = 1  # first page already fetched
        while len(items) < total and pages < self._MAX_LIST_PAGES:
            query["limit"] = limit
            query["offset"] = len(items)
            page = self._request("GET", base_url, path, params=query)
            rows = page.get("data") if isinstance(page, dict) else None
            if not rows:
                break
            items.extend(rows)
            pages += 1
            if on_page is not None:
                on_page(len(items), total)
            elif self._page_reporter is not None:
                self._page_reporter(len(items), total)
        if len(items) < total:
            import warnings
            warnings.warn(
                f"Pagination safety cap reached ({self._MAX_LIST_PAGES} pages): "
                f"returned {len(items)} of {total} items from {path}. "
                "Increase _MAX_LIST_PAGES or add server-side filters to see all results.",
                stacklevel=3,
            )
        return items

    def _list(self, base_url: str, path: str, params: Optional[dict] = None) -> list[dict]:
        """GET a collection, following limit/offset pagination to fetch ALL items."""
        # First request deliberately adds no limit/offset — some endpoints
        # reject them; pagination params only appear on follow-up pages.
        first = self._request("GET", base_url, path, params=params)
        if isinstance(first, list):
            return first
        if not isinstance(first, dict) or not isinstance(first.get("data"), list):
            return []
        return self._collect_pages(base_url, path, params, first)

    def get(self, path: str, params: Optional[dict] = None) -> Any:
        """GET against the IAM/sase gateway (api.sase.paloaltonetworks.com)."""
        return self._request("GET", self.BASE_URL, path, params=params)

    def post(self, path: str, json: Optional[dict] = None) -> Any:
        """POST against the IAM/sase gateway."""
        return self._request("POST", self.BASE_URL, path, json=json)

    def _get_objects(self, path: str, params: Optional[dict] = None) -> Any:
        """GET from api.strata.paloaltonetworks.com/config/objects/v1."""
        return self._request("GET", self.OBJECTS_URL, path, params=params)

    def _post_objects(self, path: str, json: Any = None) -> Any:
        """POST to api.strata.paloaltonetworks.com/config/objects/v1."""
        return self._request("POST", self.OBJECTS_URL, path, json=json)

    def _put_objects(self, path: str, json: Any = None) -> Any:
        """PUT to api.strata.paloaltonetworks.com/config/objects/v1."""
        return self._request("PUT", self.OBJECTS_URL, path, json=json)

    def _delete_objects(self, path: str, params: Optional[dict] = None) -> Any:
        """DELETE from api.strata.paloaltonetworks.com/config/objects/v1."""
        return self._request("DELETE", self.OBJECTS_URL, path, params=params)

    def _post_security(self, path: str, json: Any = None, params: Optional[dict] = None) -> Any:
        """POST to api.strata.paloaltonetworks.com/config/security/v1."""
        return self._request("POST", self.SECURITY_URL, path, json=json, params=params)

    def _put_security(self, path: str, json: Any = None) -> Any:
        """PUT to api.strata.paloaltonetworks.com/config/security/v1."""
        return self._request("PUT", self.SECURITY_URL, path, json=json)

    def _delete_security(self, path: str, params: Optional[dict] = None) -> Any:
        """DELETE from api.strata.paloaltonetworks.com/config/security/v1."""
        return self._request("DELETE", self.SECURITY_URL, path, params=params)

    def _post_network(self, path: str, json: Any = None, params: Optional[dict] = None) -> Any:
        """POST to api.strata.paloaltonetworks.com/config/network/v1."""
        return self._request("POST", self.NETWORK_URL, path, json=json, params=params)

    def _put_network(self, path: str, json: Any = None) -> Any:
        """PUT to api.strata.paloaltonetworks.com/config/network/v1."""
        return self._request("PUT", self.NETWORK_URL, path, json=json)

    def _delete_network(self, path: str, params: Optional[dict] = None) -> Any:
        """DELETE from api.strata.paloaltonetworks.com/config/network/v1."""
        return self._request("DELETE", self.NETWORK_URL, path, params=params)

    def _get_security(self, path: str, params: Optional[dict] = None) -> Any:
        """GET from api.strata.paloaltonetworks.com/config/security/v1."""
        return self._request("GET", self.SECURITY_URL, path, params=params)

    def _get_setup(self, path: str, params: Optional[dict] = None) -> Any:
        """GET from api.strata.paloaltonetworks.com/config/setup/v1."""
        return self._request("GET", self.SETUP_URL, path, params=params)

    def _post_setup(self, path: str, json: Optional[dict] = None) -> Any:
        """POST to api.strata.paloaltonetworks.com/config/setup/v1."""
        return self._request("POST", self.SETUP_URL, path, json=json or {})

    def _get_network(self, path: str, params: Optional[dict] = None) -> Any:
        """GET from api.strata.paloaltonetworks.com/config/network/v1.

        pan.dev: https://pan.app/scripts/scm/api/config/cloudngfw/network/
        """
        return self._request("GET", self.NETWORK_URL, path, params=params)

    # Keep the public alias used by shell.py _cmd_tsg and auth_test
    def get_setup(self, path: str, params: Optional[dict] = None) -> Any:
        """Public alias for _get_setup — kept for backward compatibility."""
        return self._get_setup(path, params)

    # ------------------------------------------------------------------
    # Generic folder-scoped config GET — powers auto-generated `show` commands
    # ------------------------------------------------------------------

    def get_config(
        self,
        domain: str,
        path: str,
        folder: str = "Shared",
        params: Optional[dict] = None,
    ) -> Any:
        """GET a folder-scoped config collection from any NGFW config domain.

        *domain* is one of ``objects`` / ``security`` / ``network`` / ``identity``;
        *path* is the resource path under that domain's ``/config/<domain>/v1``
        base (e.g. ``"/addresses"``).  The active ``folder`` is sent as the
        ``?folder=`` query parameter.  Returns the response's ``data`` list when
        present, otherwise the raw JSON.

        This is the single entry point used by the auto-generated ``show
        <resource>`` commands (see app/commands/generated.py) so ARC can expose
        every list endpoint in the pulled SCM specs without a hand-written
        method per resource.
        """
        base = {
            "objects": self.OBJECTS_URL,
            "security": self.SECURITY_URL,
            "network": self.NETWORK_URL,
            "identity": self.IDENTITY_URL,
            "setup": self.SETUP_URL,
        }.get(domain)
        if base is None:
            raise SCMError(f"Unknown config domain: {domain!r}")
        query = dict(params or {})
        query.setdefault("folder", folder)
        data = self._request("GET", base, path, params=query)
        if isinstance(data, dict) and isinstance(data.get("data"), list):
            return self._collect_pages(base, path, query, data)
        return data

    def request_api(
        self,
        base_url: str,
        method: str,
        path: str,
        params: Optional[dict] = None,
        json: Any = None,
    ) -> Any:
        """Execute a catalog-derived SCM API request.

        Inputs come from generated metadata in ``app.commands.resource_catalog``;
        callers do not pass arbitrary URLs.  This keeps the generic endpoint
        surface broad enough for spec coverage while still routing only to
        checked-in pan.dev base URLs.
        """
        norm_method = method.upper()
        norm_base = base_url.rstrip("/")
        norm_path = f"/{path.lstrip('/')}"
        data = self._request(
            norm_method,
            norm_base,
            norm_path,
            params=params or None,
            json=json,
        )
        if isinstance(data, dict) and isinstance(data.get("data"), list):
            if norm_method == "GET":
                return self._collect_pages(norm_base, norm_path, params, data)
            return data["data"]
        return data

    # ------------------------------------------------------------------
    # TSG switching
    # ------------------------------------------------------------------

    def reauthenticate(self, tsg_id: str) -> None:
        """Obtain a fresh OAuth token scoped to a different TSG.

        Used by the ``tsg <id>`` shell command.
        """
        if not (self._cfg.client_id and self._cfg.client_secret):
            raise SCMError(
                "Cannot re-authenticate: no client_id / client_secret configured. "
                "TSG switching requires OAuth client credentials."
            )
        import copy  # Deferred: avoids import at module level for a rarely-called path
        new_cfg = copy.copy(self._cfg)
        new_cfg.tsg_id = tsg_id
        self._cfg = new_cfg
        self._http.close()
        self._http = httpx.Client(timeout=30)
        self._authenticate()

    # ------------------------------------------------------------------
    # Tenancy / IAM  (api.sase.paloaltonetworks.com)
    # pan.dev: https://pan.app/scripts/scm/api/tenancy/
    # ------------------------------------------------------------------

    def get_tenants(self) -> list[dict]:
        """Return child TSG entries.

        pan.dev: GET /tenancy/v1/tenant_service_groups/{tsg_id}/operations/list_children
        Fallback: GET /tenancy/v1/tenant_service_groups (list all visible)

        Returns [] on any permission error so callers can handle gracefully.
        """
        # Strategy 1: list children of current TSG
        if self._cfg.tsg_id:
            try:
                resp = self._http.get(
                    f"{self.IAM_URL}/tenancy/v1/tenant_service_groups"
                    f"/{self._cfg.tsg_id}/operations/list_children",
                    headers=self._headers(),
                )
                if resp.status_code < 400:
                    data = resp.json()
                    entries = data.get("data", data.get("items", []))
                    if entries:
                        return entries
            except (httpx.HTTPError, ValueError, TypeError):
                pass

        # Strategy 2: flat list of all visible TSGs
        try:
            resp = self._http.get(
                f"{self.IAM_URL}/tenancy/v1/tenant_service_groups",
                headers=self._headers(),
            )
            if resp.status_code < 400:
                data = resp.json()
                return data.get("data", data.get("items", []))
        except (httpx.HTTPError, ValueError, TypeError):
            pass

        return []

    # ------------------------------------------------------------------
    # Setup  (api.strata.paloaltonetworks.com/config/setup/v1)
    # pan.dev: https://pan.app/scripts/scm/api/config/cloudngfw/setup/
    # ------------------------------------------------------------------

    def get_devices(self) -> list[dict]:
        """Return all managed NGFW devices, TSG-wide (no folder scope).

        pan.dev: GET /config/setup/v1/devices
        Spec: openapi-specs/scm/config/ngfw/setup/config-setup-feb-v1.yaml

        The endpoint accepts no folder parameter — it returns all devices
        visible to the token's TSG scope.  All pages are walked
        (limit/offset) so tenants with more than one page of devices are
        returned in full.
        Returns [] on 403 so callers can handle quietly.
        """
        try:
            return self._list(self.SETUP_URL, "/devices")
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 403:
                return []
            raise
        except (httpx.HTTPError, ValueError, TypeError):
            return []

    def get_folders(self) -> list[str]:
        """Return folder names for tab completion.

        pan.dev: GET /config/setup/v1/folders
        Spec: openapi-specs/scm/config/ngfw/setup/config-setup-feb-v1.yaml

        Falls back to common defaults on any error.
        """
        try:
            names = [
                f.get("name", "")
                for f in self._list(self.SETUP_URL, "/folders")
                if self._is_folder_record(f) and f.get("name")
            ]
            return names if names else ["Shared", "Global"]
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code in (403, 404):
                return ["Shared", "Global"]
            raise
        except (httpx.HTTPError, ValueError, TypeError):
            return ["Shared", "Global"]

    def get_jobs(self) -> list[dict]:
        """Return all SCM jobs (TSG-wide, no folder scope).

        pan.dev: GET /config/setup/v1/jobs
        Spec: openapi-specs/scm/config/ngfw/setup/config-setup-feb-v1.yaml

        Returns [] on any error so callers can handle gracefully.
        """
        try:
            return self._list(self.SETUP_URL, "/jobs")
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 403:
                return []
            raise
        except (httpx.HTTPError, ValueError, TypeError):
            return []

    def get_job(self, job_id: str) -> dict | None:
        """Return a single SCM job by ID (TSG-wide, no folder scope).

        pan.dev: GET /config/setup/v1/jobs/{id}
        Spec: openapi-specs/scm/config/ngfw/setup/config-setup-feb-v1.yaml

        Returns None if the job is not found or access is denied.
        """
        try:
            return self._get_setup(f"/jobs/{job_id}")
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code in (403, 404):
                return None
            raise
        except (httpx.HTTPError, ValueError, TypeError):
            return None

    def get_folders_full(self) -> list[dict]:
        """Return full folder records including their snippet lists.

        Each folder object carries a 'snippets' field (list of snippet name
        strings) that is the authoritative source for which snippets are
        attached to a folder.  This is the correct way to determine folder→
        snippet membership; the snippet list response does not carry folder
        references reliably.

        pan.dev: GET /config/setup/v1/folders
        Returns [] on any error so callers can handle gracefully.
        """
        try:
            folders = self._list(self.SETUP_URL, "/folders")
            return [f for f in folders if self._is_folder_record(f)]
        except (httpx.HTTPError, ValueError, TypeError):
            return []

    def get_snippets(self) -> list[dict]:
        """Return all SCM snippets.

        pan.dev: GET /config/setup/v1/snippets
        Spec: openapi-specs/scm/config/ngfw/setup/config-setup-feb-v1.yaml
        """
        try:
            return self._list(self.SETUP_URL, "/snippets")
        except (httpx.HTTPError, ValueError, TypeError):
            return []

    def get_snippet_detail(self, snippet_id: str) -> dict:
        """Return full detail for one snippet including attached folders.

        pan.dev: GET /config/setup/v1/snippets/{id}
        """
        return self._get_setup(f"/snippets/{snippet_id}")

    def get_snippet_objects(self, snippet_name: str) -> dict[str, list[dict]]:
        """Fetch all configured objects/rules scoped to a snippet.

        The SCM objects and security APIs accept a ?snippet=<name> query
        parameter that filters results to only items defined within that
        snippet.  This method queries all relevant endpoints and returns
        a dict keyed by object type.  Empty lists are omitted so the
        caller can tell at a glance what the snippet actually contains.

        pan.dev: GET /config/objects/v1/addresses?snippet=<name>  (and others)
        Per-endpoint 403/404 responses are tolerated (a missing object type in
        a snippet is normal) so one denied type doesn't hide the rest; any
        other error (401, 5xx, network) propagates to the caller.
        """
        p = {"snippet": snippet_name}
        sections: dict[str, list[dict]] = {}

        endpoints: list[tuple[str, str, str]] = [
            # (label, base, path)
            ("Addresses",           "objects",  "/addresses"),
            ("Address Groups",      "objects",  "/address-groups"),
            ("Services",            "objects",  "/services"),
            ("Service Groups",      "objects",  "/service-groups"),
            ("Tags",                "objects",  "/tags"),
            ("External Dynamic Lists", "objects", "/external-dynamic-lists"),
            ("Security Rules",      "security", "/security-rules"),
            ("URL Categories",      "security", "/url-categories"),
            ("Application Filters", "objects",  "/application-filters"),
            ("Application Groups",  "objects",  "/application-groups"),
            ("Log Forwarding",      "objects",  "/log-forwarding-profiles"),
        ]

        for label, base, path in endpoints:
            try:
                if base == "objects":
                    items = self._list(self.OBJECTS_URL, path, params=p)
                else:
                    items = self._list(self.SECURITY_URL, path, params=p)
                if items:
                    sections[label] = items
            except httpx.HTTPStatusError as exc:
                # Some object types may not exist in a given snippet; 404/403
                # per endpoint is normal.  Anything else (401, 5xx, …) is a
                # real failure and must propagate.
                if exc.response.status_code not in (403, 404):
                    raise

        return sections

    def get_folder_detail(self, folder_name: str) -> Optional[dict]:
        """Return the folder record whose name matches folder_name.

        Useful for finding a device's SCM folder record (which carries the
        snippet list).
        """
        try:
            for f in self._list(self.SETUP_URL, "/folders"):
                if self._is_folder_record(f) and f.get("name") == folder_name:
                    return f
            return None
        except (httpx.HTTPError, ValueError, TypeError):
            return None

    @staticmethod
    def _is_folder_record(record: dict) -> bool:
        """Return True when a /folders entry is an actual folder/container record.

        Some SCM tenants return managed-device entries in the /folders payload
        (type: on-prem). Those are valid context targets for devices, but they
        are not valid folder parents for folder-creation flows.
        """
        record_type = str(record.get("type") or "").lower()
        if not record_type:
            # Legacy/default entries without explicit type are treated as folders.
            return True
        return record_type == "container"

    def create_folder(self, name: str, parent: str) -> dict:
        """Create a new folder under the given parent folder.

        pan.dev: POST /config/setup/v1/folders
        Spec: openapi-specs/scm/config/ngfw/setup/config-setup-feb-v1.yaml

        Returns the created folder record.
        Raises httpx.HTTPStatusError on API errors (e.g. 409 already exists,
        403 permission denied).
        """
        return self._post_setup("/folders", json={"name": name, "parent": parent})

    # ------------------------------------------------------------------
    # Objects  (api.strata.paloaltonetworks.com/config/objects/v1)
    # pan.dev: https://pan.app/scripts/scm/api/config/cloudngfw/objects/
    # Spec: openapi-specs/scm/config/ngfw/objects/objects_v1.3_feb.yaml
    # ------------------------------------------------------------------

    def get_addresses(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/addresses"""
        return self._list(self.OBJECTS_URL, "/addresses", params={"folder": folder})

    def get_address_groups(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/address-groups"""
        return self._list(self.OBJECTS_URL, "/address-groups", params={"folder": folder})

    def get_services(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/services"""
        return self._list(self.OBJECTS_URL, "/services", params={"folder": folder})

    def get_tags(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/tags"""
        return self._list(self.OBJECTS_URL, "/tags", params={"folder": folder})

    def get_external_dynamic_lists(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/external-dynamic-lists"""
        return self._list(self.OBJECTS_URL, "/external-dynamic-lists", params={"folder": folder})

    # ------------------------------------------------------------------
    # Objects — CREATE / DELETE
    # pan.dev: POST /config/objects/v1/<resource>  |  DELETE /config/objects/v1/<resource>/{id}
    # ------------------------------------------------------------------

    def create_address(self, payload: dict) -> dict:
        """POST /config/objects/v1/addresses.  payload must include folder + name + one address type."""
        return self._post_objects("/addresses", json=payload)

    def delete_address(self, address_id: str) -> dict:
        """DELETE /config/objects/v1/addresses/{id}"""
        return self._delete_objects(f"/addresses/{address_id}")

    def create_address_group(self, payload: dict) -> dict:
        """POST /config/objects/v1/address-groups."""
        return self._post_objects("/address-groups", json=payload)

    def delete_address_group(self, group_id: str) -> dict:
        """DELETE /config/objects/v1/address-groups/{id}"""
        return self._delete_objects(f"/address-groups/{group_id}")

    def create_service(self, payload: dict) -> dict:
        """POST /config/objects/v1/services."""
        return self._post_objects("/services", json=payload)

    def delete_service(self, service_id: str) -> dict:
        """DELETE /config/objects/v1/services/{id}"""
        return self._delete_objects(f"/services/{service_id}")

    def create_service_group(self, payload: dict) -> dict:
        """POST /config/objects/v1/service-groups."""
        return self._post_objects("/service-groups", json=payload)

    def delete_service_group(self, group_id: str) -> dict:
        """DELETE /config/objects/v1/service-groups/{id}"""
        return self._delete_objects(f"/service-groups/{group_id}")

    def create_tag(self, payload: dict) -> dict:
        """POST /config/objects/v1/tags."""
        return self._post_objects("/tags", json=payload)

    def delete_tag(self, tag_id: str) -> dict:
        """DELETE /config/objects/v1/tags/{id}"""
        return self._delete_objects(f"/tags/{tag_id}")

    def create_external_dynamic_list(self, payload: dict) -> dict:
        """POST /config/objects/v1/external-dynamic-lists."""
        return self._post_objects("/external-dynamic-lists", json=payload)

    def delete_external_dynamic_list(self, edl_id: str) -> dict:
        """DELETE /config/objects/v1/external-dynamic-lists/{id}"""
        return self._delete_objects(f"/external-dynamic-lists/{edl_id}")

    # ------------------------------------------------------------------
    # Security — CREATE / DELETE
    # ------------------------------------------------------------------

    def create_security_rule(self, payload: dict, position: str = "pre") -> dict:
        """POST /config/security/v1/security-rules?position=<position>"""
        return self._post_security("/security-rules", json=payload, params={"position": position})

    def delete_security_rule(self, rule_id: str) -> dict:
        """DELETE /config/security/v1/security-rules/{id}"""
        return self._delete_security(f"/security-rules/{rule_id}")

    def create_url_category(self, payload: dict) -> dict:
        """POST /config/security/v1/url-categories"""
        return self._post_security("/url-categories", json=payload)

    def delete_url_category(self, cat_id: str) -> dict:
        """DELETE /config/security/v1/url-categories/{id}"""
        return self._delete_security(f"/url-categories/{cat_id}")

    def create_nat_rule(self, payload: dict) -> dict:
        """POST /config/network/v1/nat-rules"""
        return self._post_network("/nat-rules", json=payload)

    def delete_nat_rule(self, rule_id: str) -> dict:
        """DELETE /config/network/v1/nat-rules/{id}"""
        return self._delete_network(f"/nat-rules/{rule_id}")

    # Helper: find an object by name in a list response, return its id
    def _find_id_by_name(self, items: list[dict], name: str) -> Optional[str]:
        """Return the id of the first item whose 'name' field matches *name*.  None if not found."""
        for item in items:
            if item.get("name", "").lower() == name.lower():
                return item.get("id")
        return None

    def _find_by_name(self, items: list[dict], name: str) -> Optional[dict]:
        """Return the full dict of the first item matching *name*.  None if not found."""
        for item in items:
            if item.get("name", "").lower() == name.lower():
                return item
        return None

    # ------------------------------------------------------------------
    # Objects — UPDATE (PUT)
    # PUT requires the full object body; ARC does GET→merge→PUT internally.
    # ------------------------------------------------------------------

    def update_address(self, obj_id: str, payload: dict) -> dict:
        """PUT /config/objects/v1/addresses/{id}"""
        return self._put_objects(f"/addresses/{obj_id}", json=payload)

    def update_address_group(self, obj_id: str, payload: dict) -> dict:
        """PUT /config/objects/v1/address-groups/{id}"""
        return self._put_objects(f"/address-groups/{obj_id}", json=payload)

    def update_service(self, obj_id: str, payload: dict) -> dict:
        """PUT /config/objects/v1/services/{id}"""
        return self._put_objects(f"/services/{obj_id}", json=payload)

    def update_service_group(self, obj_id: str, payload: dict) -> dict:
        """PUT /config/objects/v1/service-groups/{id}"""
        return self._put_objects(f"/service-groups/{obj_id}", json=payload)

    def update_tag(self, obj_id: str, payload: dict) -> dict:
        """PUT /config/objects/v1/tags/{id}"""
        return self._put_objects(f"/tags/{obj_id}", json=payload)

    def update_external_dynamic_list(self, obj_id: str, payload: dict) -> dict:
        """PUT /config/objects/v1/external-dynamic-lists/{id}"""
        return self._put_objects(f"/external-dynamic-lists/{obj_id}", json=payload)

    # ------------------------------------------------------------------
    # Security — UPDATE (PUT)
    # ------------------------------------------------------------------

    def update_security_rule(self, rule_id: str, payload: dict) -> dict:
        """PUT /config/security/v1/security-rules/{id}"""
        return self._put_security(f"/security-rules/{rule_id}", json=payload)

    def update_url_category(self, cat_id: str, payload: dict) -> dict:
        """PUT /config/security/v1/url-categories/{id}"""
        return self._put_security(f"/url-categories/{cat_id}", json=payload)

    # ------------------------------------------------------------------
    # Network — UPDATE (PUT)
    # ------------------------------------------------------------------

    def update_nat_rule(self, rule_id: str, payload: dict) -> dict:
        """PUT /config/network/v1/nat-rules/{id}"""
        return self._put_network(f"/nat-rules/{rule_id}", json=payload)

    def update_zone(self, zone_id: str, payload: dict) -> dict:
        """PUT /config/network/v1/zones/{id}"""
        return self._put_network(f"/zones/{zone_id}", json=payload)

    # ------------------------------------------------------------------
    # Security  (api.strata.paloaltonetworks.com/config/security/v1)
    # pan.dev: https://pan.app/scripts/scm/api/config/cloudngfw/security/
    # Spec: openapi-specs/scm/config/ngfw/security/security-services-R2-2026.yaml
    # ------------------------------------------------------------------

    def get_security_policy(self, folder: str = "Shared", position: str = "pre") -> list[dict]:
        """pan.dev: GET /config/security/v1/security-rules"""
        return self._list(
            self.SECURITY_URL,
            "/security-rules",
            params={"folder": folder, "position": position},
        )

    def get_url_categories(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/url-categories"""
        return self._list(self.SECURITY_URL, "/url-categories", params={"folder": folder})

    def get_dns_security_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/dns-security-profiles"""
        return self._list(self.SECURITY_URL, "/dns-security-profiles", params={"folder": folder})

    # Additional security resources
    def get_decryption_rules(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/decryption-rules"""
        return self._list(self.SECURITY_URL, "/decryption-rules", params={"folder": folder})

    def get_dos_protection_rules(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/dos-protection-rules"""
        return self._list(self.SECURITY_URL, "/dos-protection-rules", params={"folder": folder})

    def get_dos_protection_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/dos-protection-profiles"""
        return self._list(self.SECURITY_URL, "/dos-protection-profiles", params={"folder": folder})

    def get_app_override_rules(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/app-override-rules"""
        return self._list(self.SECURITY_URL, "/app-override-rules", params={"folder": folder})

    def get_decryption_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/decryption-profiles"""
        return self._list(self.SECURITY_URL, "/decryption-profiles", params={"folder": folder})

    def get_profile_groups(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/profile-groups"""
        return self._list(self.SECURITY_URL, "/profile-groups", params={"folder": folder})

    def get_anti_spyware_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/anti-spyware-profiles"""
        return self._list(self.SECURITY_URL, "/anti-spyware-profiles", params={"folder": folder})

    def get_vulnerability_protection_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/vulnerability-protection-profiles"""
        return self._list(self.SECURITY_URL, "/vulnerability-protection-profiles", params={"folder": folder})

    def get_wildfire_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/wildfire-anti-virus-profiles"""
        return self._list(self.SECURITY_URL, "/wildfire-anti-virus-profiles", params={"folder": folder})

    def get_url_admin_override(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/url-admin-override"""
        return self._list(self.SECURITY_URL, "/url-admin-override", params={"folder": folder})

    # ------------------------------------------------------------------
    # Additional Objects
    # ------------------------------------------------------------------

    def get_service_groups(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/service-groups"""
        return self._list(self.OBJECTS_URL, "/service-groups", params={"folder": folder})

    def get_application_groups(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/application-groups"""
        return self._list(self.OBJECTS_URL, "/application-groups", params={"folder": folder})

    def get_application_filters(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/application-filters"""
        return self._list(self.OBJECTS_URL, "/application-filters", params={"folder": folder})

    def get_schedules(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/schedules"""
        return self._list(self.OBJECTS_URL, "/schedules", params={"folder": folder})

    def get_regions(self) -> list[dict]:
        """pan.dev: GET /config/objects/v1/regions  (global — no folder filter)"""
        return self._list(self.OBJECTS_URL, "/regions")

    def get_hip_objects(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/hip-objects"""
        return self._list(self.OBJECTS_URL, "/hip-objects", params={"folder": folder})

    def get_hip_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/hip-profiles"""
        return self._list(self.OBJECTS_URL, "/hip-profiles", params={"folder": folder})

    def get_log_forwarding_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/log-forwarding-profiles"""
        return self._list(self.OBJECTS_URL, "/log-forwarding-profiles", params={"folder": folder})

    # ------------------------------------------------------------------
    # Additional Network
    # ------------------------------------------------------------------

    def get_nat_rules(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/nat-rules"""
        return self._list(self.NETWORK_URL, "/nat-rules", params={"folder": folder})

    def get_pbf_rules(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/pbf-rules"""
        return self._list(self.NETWORK_URL, "/pbf-rules", params={"folder": folder})

    def get_ike_gateways(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/ike-gateways"""
        return self._list(self.NETWORK_URL, "/ike-gateways", params={"folder": folder})

    def get_ipsec_tunnels(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/ipsec-tunnels"""
        return self._list(self.NETWORK_URL, "/ipsec-tunnels", params={"folder": folder})

    def get_bgp_routing_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/bgp-address-family-profiles"""
        return self._list(self.NETWORK_URL, "/bgp-address-family-profiles", params={"folder": folder})

    def get_dns_proxies(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/dns-proxies"""
        return self._list(self.NETWORK_URL, "/dns-proxies", params={"folder": folder})

    def get_qos_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/qos-profiles"""
        return self._list(self.NETWORK_URL, "/qos-profiles", params={"folder": folder})

    def get_sdwan_rules(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/sdwan-rules"""
        return self._list(self.NETWORK_URL, "/sdwan-rules", params={"folder": folder})

    def get_tunnel_interfaces(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/tunnel-interfaces"""
        return self._list(self.NETWORK_URL, "/tunnel-interfaces", params={"folder": folder})

    def get_vlan_interfaces(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/vlan-interfaces"""
        return self._list(self.NETWORK_URL, "/vlan-interfaces", params={"folder": folder})

    # ------------------------------------------------------------------
    # Identity  (api.strata.paloaltonetworks.com/config/identity/v1)
    # pan.dev: https://pan.app/scripts/scm/api/config/cloudngfw/identity/
    # ------------------------------------------------------------------

    def _get_identity(self, path: str, params: Optional[dict] = None) -> Any:
        """GET from api.strata.paloaltonetworks.com/config/identity/v1."""
        return self._request("GET", self.IDENTITY_URL, path, params=params)

    def get_authentication_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/identity/v1/authentication-profiles"""
        return self._list(self.IDENTITY_URL, "/authentication-profiles", params={"folder": folder})

    def get_authentication_rules(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/identity/v1/authentication-rules"""
        return self._list(self.IDENTITY_URL, "/authentication-rules", params={"folder": folder})

    def get_certificate_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/identity/v1/certificate-profiles"""
        return self._list(self.IDENTITY_URL, "/certificate-profiles", params={"folder": folder})

    def get_local_users(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/identity/v1/local-users"""
        return self._list(self.IDENTITY_URL, "/local-users", params={"folder": folder})

    def get_local_user_groups(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/identity/v1/local-user-groups"""
        return self._list(self.IDENTITY_URL, "/local-user-groups", params={"folder": folder})

    def get_radius_server_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/identity/v1/radius-server-profiles"""
        return self._list(self.IDENTITY_URL, "/radius-server-profiles", params={"folder": folder})

    def get_tls_service_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/identity/v1/tls-service-profiles"""
        return self._list(self.IDENTITY_URL, "/tls-service-profiles", params={"folder": folder})

    def get_mfa_servers(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/identity/v1/mfa-servers"""
        return self._list(self.IDENTITY_URL, "/mfa-servers", params={"folder": folder})

    # ------------------------------------------------------------------
    # Network  (api.strata.paloaltonetworks.com/config/network/v1)
    # pan.dev: https://pan.app/scripts/scm/api/config/cloudngfw/network/
    # Spec: openapi-specs/scm/config/ngfw/network/  (verify exact file at pan.dev)
    # ------------------------------------------------------------------

    def get_interfaces(self, folder: str = "Shared") -> list[dict]:
        """Return ethernet interfaces configured in the active folder.

        pan.dev: GET /config/network/v1/ethernet?folder=<folder>
        Returns [] on 403/404 so callers degrade gracefully.
        """
        try:
            return self._list(self.NETWORK_URL, "/ethernet", params={"folder": folder})
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code in (403, 404):
                return []
            raise
        except (httpx.HTTPError, ValueError, TypeError):
            return []

    def get_aggregate_interfaces(self, folder: str = "Shared") -> list[dict]:
        """Return aggregate (AE) interfaces configured in the active folder.

        pan.dev: GET /config/network/v1/aggregate-ethernet?folder=<folder>
        """
        try:
            return self._list(self.NETWORK_URL, "/aggregate-ethernet", params={"folder": folder})
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code in (403, 404):
                return []
            raise
        except (httpx.HTTPError, ValueError, TypeError):
            return []

    def get_loopback_interfaces(self, folder: str = "Shared") -> list[dict]:
        """Return loopback interfaces configured in the active folder.

        pan.dev: GET /config/network/v1/loopback-interfaces?folder=<folder>
        """
        try:
            return self._list(self.NETWORK_URL, "/loopback-interfaces", params={"folder": folder})
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code in (403, 404):
                return []
            raise
        except (httpx.HTTPError, ValueError, TypeError):
            return []

    def get_zones(self, folder: str = "Shared") -> list[dict]:
        """Return security zones configured in the active folder.

        pan.dev: GET /config/network/v1/zones?folder=<folder>
        Returns [] on 403/404 so callers degrade gracefully.
        """
        try:
            return self._list(self.NETWORK_URL, "/zones", params={"folder": folder})
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code in (403, 404):
                return []
            raise
        except (httpx.HTTPError, ValueError, TypeError):
            return []

    def get_static_routes(self, folder: str = "Shared") -> list[dict]:
        """Return static routes configured in the active folder.

        pan.dev: GET /config/network/v1/routing/static-routes?folder=<folder>
        Returns [] on 403/404.
        """
        try:
            return self._list(self.NETWORK_URL, "/routing/static-routes", params={"folder": folder})
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code in (403, 404):
                return []
            raise
        except (httpx.HTTPError, ValueError, TypeError):
            return []

    def get_routing_profiles(self, folder: str = "Shared") -> list[dict]:
        """Return routing profiles / virtual routers in the active folder.

        pan.dev: GET /config/network/v1/virtual-routers?folder=<folder>
        Returns [] on 403/404.
        """
        try:
            return self._list(self.NETWORK_URL, "/virtual-routers", params={"folder": folder})
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code in (403, 404):
                return []
            raise
        except (httpx.HTTPError, ValueError, TypeError):
            return []

    def get_ha_config(self, folder: str = "Shared") -> list[dict]:
        """Return HA configuration in the active folder.

        pan.dev: GET /config/network/v1/ha?folder=<folder>
        Returns [] on 403/404.
        """
        try:
            data = self._get_network("/ha", params={"folder": folder})
            # HA may return a single object or a list — normalise to list
            if isinstance(data, list):
                return data
            if isinstance(data, dict):
                items = data.get("data", [])
                return items if items else ([data] if data else [])
            return []
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code in (403, 404):
                return []
            raise
        except (httpx.HTTPError, ValueError, TypeError):
            return []

    # ------------------------------------------------------------------
    # Commit / push config  (api.strata.paloaltonetworks.com/config/setup/v1)
    # pan.dev: https://pan.app/scripts/scm/api/config/cloudngfw/setup/
    # ------------------------------------------------------------------

    def push_config(
        self,
        folders: Optional[list[str]] = None,
        devices: Optional[list[str]] = None,
        description: str = "",
    ) -> dict:
        """Push the candidate configuration to managed devices.

        Creates an SCM push job.  Returns the job record so the caller can
        display the job ID and check progress with 'show jobs id <n>'.

        pan.dev: POST /config/setup/v1/config-versions/candidate:push
        """
        payload: dict = {}
        if folders:
            payload["folders"] = folders
        if devices:
            payload["devices"] = devices
        if description:
            payload["description"] = description
        return self._post_setup("/config-versions/candidate:push", json=payload)

    def discard_candidate(self) -> Any:
        """Discard the TSG's candidate configuration (revert to running config).

        Removes ALL staged (uncommitted) changes in the tenant — including any
        made outside this ARC session, e.g. in the SCM web UI.

        pan.dev: DELETE /config/operations/v1/config-versions/candidate
        """
        return self._request("DELETE", self.OPERATIONS_URL, "/config-versions/candidate")

    # ------------------------------------------------------------------
    # Config versions — history, running config, rollback
    # Spec: docs/scm-api/specs/ngfw-config-operations.md
    # ------------------------------------------------------------------

    def get_config_versions(self) -> list[dict]:
        """List the tenant's configuration versions (newest history first).

        pan.dev: GET /config/operations/v1/config-versions
        """
        return self._list(self.OPERATIONS_URL, "/config-versions")

    def get_config_version(self, version: int | str) -> dict:
        """Return one configuration version record by id.

        pan.dev: GET /config/operations/v1/config-versions/{version}
        """
        return self._request("GET", self.OPERATIONS_URL, f"/config-versions/{version}")

    def get_running_config_version(self) -> Any:
        """Return the running configuration version(s) for the tenant.

        pan.dev: GET /config/operations/v1/config-versions/running
        """
        return self._request("GET", self.OPERATIONS_URL, "/config-versions/running")

    def load_config_version(self, version: int) -> Any:
        """Load *version* as the candidate configuration (rollback).

        Replaces the tenant's candidate config in SCM immediately — the
        caller must still `commit` (candidate:push) for devices to change.

        pan.dev: POST /config/operations/v1/config-versions:load  body {"version": n}
        """
        return self._request(
            "POST", self.OPERATIONS_URL, "/config-versions:load", json={"version": version}
        )

    # ------------------------------------------------------------------
    # Live-device operations over the SCM management tunnel (async jobs)
    # ------------------------------------------------------------------

    def ops_job_start(self, op: str, serials: list[str], advanced: bool = False) -> str:
        """Start a live-device operations job; returns the job UUID.

        pan.dev: POST /operations/v1/jobs/{op}  body {"devices": [serials]}
        The device answers over its existing management tunnel to SCM — no
        SSH, no device credentials. `advanced` applies to route/fib jobs only.
        """
        body: dict = {"devices": serials}
        if advanced:
            body["advanced"] = True
        data = self._request("POST", self.NGFW_OPS_URL, f"/jobs/{op}", json=body)
        job_id = str(data.get("job_id") or "") if isinstance(data, dict) else ""
        if not job_id:
            raise SCMError(f"operations job '{op}' returned no job_id: {data!r}")
        return job_id

    def ops_job_status(self, job_id: str) -> dict:
        """Return a live-device operations job record.

        pan.dev: GET /operations/v1/device/jobs/{id}
        Job state: pending | in_progress | complete | failed; per-device
        results are inline at results[].details.result.
        """
        data = self._request("GET", self.NGFW_OPS_URL, f"/device/jobs/{job_id}")
        return data if isinstance(data, dict) else {}

    def close(self) -> None:
        self._http.close()
