"""Strata Cloud Manager REST API client.

All endpoint paths and base URLs are sourced directly from the pan.dev
OpenAPI specifications:

  https://pan.dev/scm/api/

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

from typing import Any, Optional

import httpx

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

        # Auth priority:
        #   1. OAuth client credentials (client_id + client_secret + tsg_id) — always
        #      preferred; produces a fresh token scoped to the correct TSG.
        #   2. Pre-issued bearer token — only when no client credentials exist.
        if cfg.client_id and cfg.client_secret and cfg.tsg_id:
            self._authenticate()
        elif cfg.bearer_token.strip():
            self._token = cfg.bearer_token.strip()
        else:
            raise SCMError(
                "SCM is not configured. Provide client_id + client_secret + tsg_id "
                "(recommended), or a pre-issued SCM_BEARER_TOKEN."
            )

    def _authenticate(self) -> None:
        """Obtain an OAuth token via the client-credentials flow.

        pan.dev ref: https://pan.dev/scm/api/auth/post-auth-v-1-oauth-2-access-token/
        """
        if not (self._cfg.client_id and self._cfg.client_secret and self._cfg.tsg_id):
            raise SCMError(
                "SCM is not configured. Set SCM_BEARER_TOKEN, or set "
                "SCM_CLIENT_ID / SCM_CLIENT_SECRET / SCM_TSG_ID."
            )
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
            raise SCMError(f"SCM authentication failed: {exc}") from exc
        self._token = resp.json().get("access_token", "")
        if not self._token:
            raise SCMError("SCM auth returned no access_token.")

    def _headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self._token}"}

    # ------------------------------------------------------------------
    # Generic request helpers
    # ------------------------------------------------------------------

    def get(self, path: str, params: Optional[dict] = None) -> Any:
        """GET against the IAM/sase gateway (api.sase.paloaltonetworks.com)."""
        resp = self._http.get(
            f"{self.BASE_URL}{path}",
            headers=self._headers(),
            params=params,
        )
        resp.raise_for_status()
        return resp.json()

    def post(self, path: str, json: Optional[dict] = None) -> Any:
        """POST against the IAM/sase gateway."""
        resp = self._http.post(
            f"{self.BASE_URL}{path}",
            headers=self._headers(),
            json=json,
        )
        resp.raise_for_status()
        return resp.json()

    def _get_objects(self, path: str, params: Optional[dict] = None) -> Any:
        """GET from api.strata.paloaltonetworks.com/config/objects/v1."""
        resp = self._http.get(
            f"{self.OBJECTS_URL}{path}",
            headers=self._headers(),
            params=params,
        )
        resp.raise_for_status()
        return resp.json()

    def _post_objects(self, path: str, json: Any = None) -> Any:
        """POST to api.strata.paloaltonetworks.com/config/objects/v1."""
        resp = self._http.post(
            f"{self.OBJECTS_URL}{path}",
            headers=self._headers(),
            json=json,
        )
        resp.raise_for_status()
        return resp.json()

    def _put_objects(self, path: str, json: Any = None) -> Any:
        """PUT to api.strata.paloaltonetworks.com/config/objects/v1."""
        resp = self._http.put(
            f"{self.OBJECTS_URL}{path}",
            headers=self._headers(),
            json=json,
        )
        resp.raise_for_status()
        return resp.json()

    def _delete_objects(self, path: str, params: Optional[dict] = None) -> Any:
        """DELETE from api.strata.paloaltonetworks.com/config/objects/v1."""
        resp = self._http.delete(
            f"{self.OBJECTS_URL}{path}",
            headers=self._headers(),
            params=params,
        )
        resp.raise_for_status()
        return resp.json() if resp.content else {}

    def _post_security(self, path: str, json: Any = None, params: Optional[dict] = None) -> Any:
        """POST to api.strata.paloaltonetworks.com/config/security/v1."""
        resp = self._http.post(
            f"{self.SECURITY_URL}{path}",
            headers=self._headers(),
            json=json,
            params=params,
        )
        resp.raise_for_status()
        return resp.json()

    def _put_security(self, path: str, json: Any = None) -> Any:
        """PUT to api.strata.paloaltonetworks.com/config/security/v1."""
        resp = self._http.put(
            f"{self.SECURITY_URL}{path}",
            headers=self._headers(),
            json=json,
        )
        resp.raise_for_status()
        return resp.json()

    def _delete_security(self, path: str, params: Optional[dict] = None) -> Any:
        """DELETE from api.strata.paloaltonetworks.com/config/security/v1."""
        resp = self._http.delete(
            f"{self.SECURITY_URL}{path}",
            headers=self._headers(),
            params=params,
        )
        resp.raise_for_status()
        return resp.json() if resp.content else {}

    def _post_network(self, path: str, json: Any = None, params: Optional[dict] = None) -> Any:
        """POST to api.strata.paloaltonetworks.com/config/network/v1."""
        resp = self._http.post(
            f"{self.NETWORK_URL}{path}",
            headers=self._headers(),
            json=json,
            params=params,
        )
        resp.raise_for_status()

    def _put_network(self, path: str, json: Any = None) -> Any:
        """PUT to api.strata.paloaltonetworks.com/config/network/v1."""
        resp = self._http.put(
            f"{self.NETWORK_URL}{path}",
            headers=self._headers(),
            json=json,
        )
        resp.raise_for_status()
        return resp.json()
        return resp.json()

    def _delete_network(self, path: str, params: Optional[dict] = None) -> Any:
        """DELETE from api.strata.paloaltonetworks.com/config/network/v1."""
        resp = self._http.delete(
            f"{self.NETWORK_URL}{path}",
            headers=self._headers(),
            params=params,
        )
        resp.raise_for_status()
        return resp.json() if resp.content else {}

    def _get_security(self, path: str, params: Optional[dict] = None) -> Any:
        """GET from api.strata.paloaltonetworks.com/config/security/v1."""
        resp = self._http.get(
            f"{self.SECURITY_URL}{path}",
            headers=self._headers(),
            params=params,
        )
        resp.raise_for_status()
        return resp.json()

    def _get_setup(self, path: str, params: Optional[dict] = None) -> Any:
        """GET from api.strata.paloaltonetworks.com/config/setup/v1."""
        resp = self._http.get(
            f"{self.SETUP_URL}{path}",
            headers=self._headers(),
            params=params,
        )
        resp.raise_for_status()
        return resp.json()

    def _post_setup(self, path: str, json: Optional[dict] = None) -> Any:
        """POST to api.strata.paloaltonetworks.com/config/setup/v1."""
        resp = self._http.post(
            f"{self.SETUP_URL}{path}",
            headers=self._headers(),
            json=json or {},
        )
        resp.raise_for_status()
        return resp.json()

    def _get_network(self, path: str, params: Optional[dict] = None) -> Any:
        """GET from api.strata.paloaltonetworks.com/config/network/v1.

        pan.dev: https://pan.dev/scm/api/config/cloudngfw/network/
        """
        resp = self._http.get(
            f"{self.NETWORK_URL}{path}",
            headers=self._headers(),
            params=params,
        )
        resp.raise_for_status()
        return resp.json()

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
        resp = self._http.get(f"{base}{path}", headers=self._headers(), params=query)
        resp.raise_for_status()
        data = resp.json()
        if isinstance(data, dict) and isinstance(data.get("data"), list):
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
    # pan.dev: https://pan.dev/scm/api/tenancy/
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
    # pan.dev: https://pan.dev/scm/api/config/cloudngfw/setup/
    # ------------------------------------------------------------------

    def get_devices(self) -> list[dict]:
        """Return all managed NGFW devices, TSG-wide (no folder scope).

        pan.dev: GET /config/setup/v1/devices
        Spec: openapi-specs/scm/config/ngfw/setup/config-setup-feb-v1.yaml

        The endpoint accepts no folder parameter — it returns all devices
        visible to the token's TSG scope.  Default page limit is 200; this
        method walks all pages (offset-based) so tenants with more than 200
        devices are returned in full.
        Returns [] on 403 so callers can handle quietly.
        """
        _PAGE_LIMIT = 200
        all_devices: list[dict] = []
        offset = 0
        try:
            while True:
                data = self._get_setup(
                    "/devices",
                    params={"limit": _PAGE_LIMIT, "offset": offset},
                )
                page = data.get("data", [])
                all_devices.extend(page)

                total = data.get("total", len(all_devices))
                offset += len(page)
                # Stop when we have all records or the page came back empty.
                if not page or offset >= total:
                    break
            return all_devices
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
            data = self._get_setup("/folders")
            names = [
                f.get("name", "")
                for f in data.get("data", [])
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
            data = self._get_setup("/jobs")
            return data.get("data", [])
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
            data = self._get_setup("/folders")
            return [f for f in data.get("data", []) if self._is_folder_record(f)]
        except (httpx.HTTPError, ValueError, TypeError):
            return []

    def get_snippets(self) -> list[dict]:
        """Return all SCM snippets.

        pan.dev: GET /config/setup/v1/snippets
        Spec: openapi-specs/scm/config/ngfw/setup/config-setup-feb-v1.yaml
        """
        try:
            data = self._get_setup("/snippets")
            return data.get("data", [])
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
        Returns {} on any total failure; per-endpoint failures are swallowed
        so a 403 on one type doesn't prevent other types from loading.
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
                    data = self._get_objects(path, params=p)
                else:
                    data = self._get_security(path, params=p)
                items = data.get("data", [])
                if items:
                    sections[label] = items
            except Exception:
                # Individual endpoint failures are swallowed — some object
                # types may not exist in a given snippet; 404/403 is normal.
                pass

        return sections

    def get_folder_detail(self, folder_name: str) -> Optional[dict]:
        """Return the folder record whose name matches folder_name.

        Useful for finding a device's SCM folder record (which carries the
        snippet list).
        """
        try:
            data = self._get_setup("/folders")
            for f in data.get("data", []):
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
    # pan.dev: https://pan.dev/scm/api/config/cloudngfw/objects/
    # Spec: openapi-specs/scm/config/ngfw/objects/objects_v1.3_feb.yaml
    # ------------------------------------------------------------------

    def get_addresses(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/addresses"""
        data = self._get_objects("/addresses", params={"folder": folder})
        return data.get("data", [])

    def get_address_groups(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/address-groups"""
        data = self._get_objects("/address-groups", params={"folder": folder})
        return data.get("data", [])

    def get_services(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/services"""
        data = self._get_objects("/services", params={"folder": folder})
        return data.get("data", [])

    def get_tags(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/tags"""
        data = self._get_objects("/tags", params={"folder": folder})
        return data.get("data", [])

    def get_external_dynamic_lists(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/external-dynamic-lists"""
        data = self._get_objects("/external-dynamic-lists", params={"folder": folder})
        return data.get("data", [])

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
    # pan.dev: https://pan.dev/scm/api/config/cloudngfw/security/
    # Spec: openapi-specs/scm/config/ngfw/security/security-services-R2-2026.yaml
    # ------------------------------------------------------------------

    def get_security_policy(self, folder: str = "Shared", position: str = "pre") -> list[dict]:
        """pan.dev: GET /config/security/v1/security-rules"""
        data = self._get_security(
            "/security-rules",
            params={"folder": folder, "position": position},
        )
        return data.get("data", [])

    def get_url_categories(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/url-categories"""
        data = self._get_security("/url-categories", params={"folder": folder})
        return data.get("data", [])

    def get_dns_security_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/dns-security-profiles"""
        data = self._get_security("/dns-security-profiles", params={"folder": folder})
        return data.get("data", [])

    # Additional security resources
    def get_decryption_rules(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/decryption-rules"""
        data = self._get_security("/decryption-rules", params={"folder": folder})
        return data.get("data", [])

    def get_dos_protection_rules(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/dos-protection-rules"""
        data = self._get_security("/dos-protection-rules", params={"folder": folder})
        return data.get("data", [])

    def get_dos_protection_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/dos-protection-profiles"""
        data = self._get_security("/dos-protection-profiles", params={"folder": folder})
        return data.get("data", [])

    def get_app_override_rules(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/app-override-rules"""
        data = self._get_security("/app-override-rules", params={"folder": folder})
        return data.get("data", [])

    def get_decryption_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/decryption-profiles"""
        data = self._get_security("/decryption-profiles", params={"folder": folder})
        return data.get("data", [])

    def get_profile_groups(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/profile-groups"""
        data = self._get_security("/profile-groups", params={"folder": folder})
        return data.get("data", [])

    def get_anti_spyware_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/anti-spyware-profiles"""
        data = self._get_security("/anti-spyware-profiles", params={"folder": folder})
        return data.get("data", [])

    def get_vulnerability_protection_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/vulnerability-protection-profiles"""
        data = self._get_security("/vulnerability-protection-profiles", params={"folder": folder})
        return data.get("data", [])

    def get_wildfire_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/wildfire-anti-virus-profiles"""
        data = self._get_security("/wildfire-anti-virus-profiles", params={"folder": folder})
        return data.get("data", [])

    def get_url_admin_override(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/url-admin-override"""
        data = self._get_security("/url-admin-override", params={"folder": folder})
        return data.get("data", [])

    # ------------------------------------------------------------------
    # Additional Objects
    # ------------------------------------------------------------------

    def get_service_groups(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/service-groups"""
        data = self._get_objects("/service-groups", params={"folder": folder})
        return data.get("data", [])

    def get_application_groups(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/application-groups"""
        data = self._get_objects("/application-groups", params={"folder": folder})
        return data.get("data", [])

    def get_application_filters(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/application-filters"""
        data = self._get_objects("/application-filters", params={"folder": folder})
        return data.get("data", [])

    def get_schedules(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/schedules"""
        data = self._get_objects("/schedules", params={"folder": folder})
        return data.get("data", [])

    def get_regions(self) -> list[dict]:
        """pan.dev: GET /config/objects/v1/regions  (global — no folder filter)"""
        data = self._get_objects("/regions")
        return data.get("data", [])

    def get_hip_objects(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/hip-objects"""
        data = self._get_objects("/hip-objects", params={"folder": folder})
        return data.get("data", [])

    def get_hip_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/hip-profiles"""
        data = self._get_objects("/hip-profiles", params={"folder": folder})
        return data.get("data", [])

    def get_log_forwarding_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/log-forwarding-profiles"""
        data = self._get_objects("/log-forwarding-profiles", params={"folder": folder})
        return data.get("data", [])

    # ------------------------------------------------------------------
    # Additional Network
    # ------------------------------------------------------------------

    def get_nat_rules(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/nat-rules"""
        try:
            data = self._get_network("/nat-rules", params={"folder": folder})
            return data.get("data", [])
        except Exception:
            return []

    def get_pbf_rules(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/pbf-rules"""
        try:
            data = self._get_network("/pbf-rules", params={"folder": folder})
            return data.get("data", [])
        except Exception:
            return []

    def get_ike_gateways(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/ike-gateways"""
        try:
            data = self._get_network("/ike-gateways", params={"folder": folder})
            return data.get("data", [])
        except Exception:
            return []

    def get_ipsec_tunnels(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/ipsec-tunnels"""
        try:
            data = self._get_network("/ipsec-tunnels", params={"folder": folder})
            return data.get("data", [])
        except Exception:
            return []

    def get_bgp_routing_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/bgp-address-family-profiles"""
        try:
            data = self._get_network("/bgp-address-family-profiles", params={"folder": folder})
            return data.get("data", [])
        except Exception:
            return []

    def get_dns_proxies(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/dns-proxies"""
        try:
            data = self._get_network("/dns-proxies", params={"folder": folder})
            return data.get("data", [])
        except Exception:
            return []

    def get_qos_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/qos-profiles"""
        try:
            data = self._get_network("/qos-profiles", params={"folder": folder})
            return data.get("data", [])
        except Exception:
            return []

    def get_sdwan_rules(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/sdwan-rules"""
        try:
            data = self._get_network("/sdwan-rules", params={"folder": folder})
            return data.get("data", [])
        except Exception:
            return []

    def get_tunnel_interfaces(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/tunnel-interfaces"""
        try:
            data = self._get_network("/tunnel-interfaces", params={"folder": folder})
            return data.get("data", [])
        except Exception:
            return []

    def get_vlan_interfaces(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/network/v1/vlan-interfaces"""
        try:
            data = self._get_network("/vlan-interfaces", params={"folder": folder})
            return data.get("data", [])
        except Exception:
            return []

    # ------------------------------------------------------------------
    # Identity  (api.strata.paloaltonetworks.com/config/identity/v1)
    # pan.dev: https://pan.dev/scm/api/config/cloudngfw/identity/
    # ------------------------------------------------------------------

    def _get_identity(self, path: str, params: Optional[dict] = None) -> Any:
        """GET from api.strata.paloaltonetworks.com/config/identity/v1."""
        resp = self._http.get(
            f"{self.IDENTITY_URL}{path}",
            headers=self._headers(),
            params=params,
        )
        resp.raise_for_status()
        return resp.json()

    def get_authentication_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/identity/v1/authentication-profiles"""
        try:
            data = self._get_identity("/authentication-profiles", params={"folder": folder})
            return data.get("data", [])
        except Exception:
            return []

    def get_authentication_rules(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/identity/v1/authentication-rules"""
        try:
            data = self._get_identity("/authentication-rules", params={"folder": folder})
            return data.get("data", [])
        except Exception:
            return []

    def get_certificate_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/identity/v1/certificate-profiles"""
        try:
            data = self._get_identity("/certificate-profiles", params={"folder": folder})
            return data.get("data", [])
        except Exception:
            return []

    def get_local_users(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/identity/v1/local-users"""
        try:
            data = self._get_identity("/local-users", params={"folder": folder})
            return data.get("data", [])
        except Exception:
            return []

    def get_local_user_groups(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/identity/v1/local-user-groups"""
        try:
            data = self._get_identity("/local-user-groups", params={"folder": folder})
            return data.get("data", [])
        except Exception:
            return []

    def get_radius_server_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/identity/v1/radius-server-profiles"""
        try:
            data = self._get_identity("/radius-server-profiles", params={"folder": folder})
            return data.get("data", [])
        except Exception:
            return []

    def get_tls_service_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/identity/v1/tls-service-profiles"""
        try:
            data = self._get_identity("/tls-service-profiles", params={"folder": folder})
            return data.get("data", [])
        except Exception:
            return []

    def get_mfa_servers(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/identity/v1/mfa-servers"""
        try:
            data = self._get_identity("/mfa-servers", params={"folder": folder})
            return data.get("data", [])
        except Exception:
            return []

    # ------------------------------------------------------------------
    # Network  (api.strata.paloaltonetworks.com/config/network/v1)
    # pan.dev: https://pan.dev/scm/api/config/cloudngfw/network/
    # Spec: openapi-specs/scm/config/ngfw/network/  (verify exact file at pan.dev)
    # ------------------------------------------------------------------

    def get_interfaces(self, folder: str = "Shared") -> list[dict]:
        """Return ethernet interfaces configured in the active folder.

        pan.dev: GET /config/network/v1/ethernet?folder=<folder>
        Returns [] on 403/404 so callers degrade gracefully.
        """
        try:
            data = self._get_network("/ethernet", params={"folder": folder})
            return data.get("data", [])
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
            data = self._get_network("/aggregate-ethernet", params={"folder": folder})
            return data.get("data", [])
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
            data = self._get_network("/loopback-interfaces", params={"folder": folder})
            return data.get("data", [])
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
            data = self._get_network("/zones", params={"folder": folder})
            return data.get("data", [])
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
            data = self._get_network("/routing/static-routes", params={"folder": folder})
            return data.get("data", [])
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
            data = self._get_network("/virtual-routers", params={"folder": folder})
            return data.get("data", [])
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
    # pan.dev: https://pan.dev/scm/api/config/cloudngfw/setup/
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

    def close(self) -> None:
        self._http.close()
