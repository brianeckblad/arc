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

    def get_devices(self, folder: str = "Shared") -> list[dict]:
        """Return managed NGFW devices.

        pan.dev: GET /config/setup/v1/devices
        Spec: openapi-specs/scm/config/ngfw/setup/config-setup-feb-v1.yaml

        The folder param is accepted for interface compatibility; the endpoint
        returns all visible devices regardless of folder.
        Returns [] on 403 so callers can handle quietly.
        """
        try:
            data = self._get_setup("/devices")
            return data.get("data", [])
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
