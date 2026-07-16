"""ARC settings console — the ``arc gui-configure`` browser GUI.

A local, loopback-only web console (built on :class:`BaseGuiServer`) that manages
everything an ARC operator would otherwise edit by hand: user preferences, the
settings files (banner / goodbye / app-variables / panos-sources / scm-sources /
theme), config.json (folders, debug, GUI ports, profiles), OS-keychain secrets,
SCM authentication, and maintenance actions (update docs & commands, backup).

Every mutation routes through the SAME settings/config/keychain helpers the CLI
uses, so GUI edits and manual edits stay equivalent (the golden rule).
"""
from __future__ import annotations

import logging
from pathlib import Path

from app.web.gui_base import BaseGuiServer
# Reuse the shared GUI palette + colour validation from the feature editor.
from app.web.feature_server import _GUI_THEMES, GUI_THEME_TOKENS, _valid_color

logger = logging.getLogger(__name__)

_HTML_FILE = Path(__file__).with_name("arc_gui.html")

# Left-nav sections (SCM-style admin console).  Each maps to a client view.
_SECTIONS = [
    {"key": "dashboard", "label": "Dashboard", "icon": "◉"},
    {"key": "authentication", "label": "Authentication", "icon": "⚿"},
    {"key": "credentials", "label": "Credentials & Keychain", "icon": "🔑"},
    {"key": "connection", "label": "Connection / config.json", "icon": "⚙"},
    {"key": "preferences", "label": "Preferences", "icon": "☰"},
    {"key": "theme", "label": "Appearance / Theme", "icon": "◐"},
    {"key": "branding", "label": "Branding & Variables", "icon": "✎"},
    {"key": "sources", "label": "API Sources", "icon": "⇅"},
    {"key": "maintenance", "label": "Maintenance", "icon": "⟳"},
]

_SECTION_HELP = {
    "dashboard": (
        "<h3>Dashboard</h3><p>At-a-glance health of your ARC install — SCM "
        "connectivity, credential status, OS-keychain availability, the active "
        "profile / TSG / folder, and the browser-GUI ports.</p>"
    ),
    "theme": (
        "<h3>Appearance</h3><p>Pick a base palette and tweak individual colours "
        "for the ARC browser GUIs.  Saved to your <code>config.json</code> and "
        "applied to BOTH consoles (GUI only — the terminal shell uses "
        "<code>settings/theme.json</code>).</p>"
    ),
    "connection": (
        "<h3>Connection / config.json</h3><p>Non-secret settings stored in your "
        "per-user <code>config.json</code>: default folder, debug, and the local "
        "ports the two browser GUIs listen on (feature editor + this console).</p>"
    ),
    # --- per-item topics ---
    "item.default_folder": "<h3>Default folder</h3><p>The SCM folder ARC scopes to at startup. Change context in the shell with <code>cd folder &lt;name&gt;</code>.</p>",
    "item.debug": "<h3>Debug logging</h3><p>Verbose logging (equivalent to <code>ARC_DEBUG=1</code>). Leave off for normal use.</p>",
    "item.ports": "<h3>GUI ports</h3><p>Local loopback ports for the two browser consoles. They must differ. Changes apply the next time you launch a console.</p>",
    "item.terminal_length": "<h3>Terminal paging length</h3><p>Lines per page for long output. 0 disables paging (use your terminal scrollback).</p>",
    "item.terminal_width": "<h3>Terminal width</h3><p>Force a render width in columns. 0 = auto-detect from the terminal.</p>",
    "item.terminal_height": "<h3>Terminal height</h3><p>Force a render height. 0 = auto-detect.</p>",
    "item.spinner": "<h3>Spinner</h3><p>Show the “querying SCM…” spinner during API calls.</p>",
    "item.client_id": "<h3>Client ID</h3><p>SCM service-account OAuth client id (non-secret; stored in config.json).</p>",
    "item.tsg_id": "<h3>TSG ID</h3><p>Tenant Service Group id the token is scoped to.</p>",
    "item.client_secret": "<h3>Client secret</h3><p>Service-account OAuth secret. Stored in the OS keychain — never in config.json. Leave blank to keep the stored value.</p>",
    "item.bearer": "<h3>Bearer token</h3><p>A pre-issued SCM token. Overrides the service account when set. Stored in the OS keychain.</p>",
    "item.ssh_key_enabled": "<h3>SSH key</h3><p>Enable to authenticate to devices with a private key file; disable to use a password instead.</p>",
    "item.ssh_key_path": "<h3>SSH key path</h3><p>Path to the private key used for device SSH.</p>",
    "item.ssh_password": "<h3>SSH password</h3><p>Device SSH password. Stored in the OS keychain.</p>",
    "item.banner": "<h3>Banner</h3><p>Shown at startup. Supports <code>{{variable}}</code> tokens from App variables.</p>",
    "item.goodbye": "<h3>Goodbye lines</h3><p>One random line is shown on exit. Add or remove lines individually.</p>",
    "item.app_variables": "<h3>App variables</h3><p>Key/value substitutions referenced as <code>{{key}}</code> in the banner/goodbye. Comment/meta keys (starting with _) are preserved automatically.</p>",
    "item.panos_sources": "<h3>PAN-OS sources</h3><p>Doc pages pulled by <code>panosupdate</code>. Each row: key, URL, kind, version.</p>",
    "item.scm_sources": "<h3>SCM sources</h3><p>pan.dev registry for <code>docsupdate</code>. Mostly self-healing — specs/guides are auto-discovered. Edit repo/branch or pin a spec path; use Advanced for the raw JSON.</p>",
}


def _item_help(topic: str):
    return _SECTION_HELP.get(topic)


class ArcGuiServer(BaseGuiServer):
    """Blocking, on-demand HTTP server for the ARC settings console."""

    HTML_FILE = _HTML_FILE
    LABEL = "ARC settings console"

    def __init__(self, shell, port: int = 4444, host: str = "127.0.0.1") -> None:
        super().__init__(shell, port=port, host=host)

    # -- routing -----------------------------------------------------------

    def route_get(self, path, qs):
        if path == "/api/nav":
            return {"sections": _SECTIONS}
        if path == "/api/theme":
            return self._build_theme()
        if path == "/api/status":
            return self._status()
        if path == "/api/prefs":
            return self._get_prefs()
        if path == "/api/config":
            return self._get_config()
        if path == "/api/sources":
            return self._get_sources((qs.get("which") or [""])[0])
        if path == "/api/branding":
            return self._get_branding()
        if path == "/api/credentials":
            return self._get_credentials()
        if path == "/api/help":
            topic = (qs.get("topic") or [""])[0]
            if topic in _SECTION_HELP:
                return {"kind": "topic", "html": _SECTION_HELP[topic]}
            return {"error": "no help for that target"}
        return None

    def route_post(self, path, data):
        if path == "/api/theme":
            base = str(data.get("base", "")).strip()
            overrides = data.get("overrides") or {}
            if not isinstance(overrides, dict):
                overrides = {}
            return self._apply_theme(base, overrides)
        if path == "/api/prefs":
            return self._apply_prefs(data)
        if path == "/api/config":
            return self._apply_config(data)
        if path == "/api/sources":
            return self._apply_sources(str(data.get("which", "")), data)
        if path == "/api/branding":
            return self._apply_branding(data)
        if path == "/api/credentials":
            return self._apply_credentials(data)
        if path == "/api/test-auth":
            return self._test_auth()
        if path == "/api/maintenance":
            return self._run_maintenance(str(data.get("action", "")))
        return None

    # -- theme (per-user GUI theme, shared palette) -----------------------

    def _build_theme(self) -> dict:
        # Read fresh from disk so a theme saved in either console shows up on the
        # next launch without restarting ARC (keeps shell._prefs in sync too).
        from app.settings.user_prefs import load_prefs

        try:
            prefs = load_prefs()
        except Exception:  # noqa: BLE001 — never let a bad prefs load 500 the GUI
            prefs = None
        active = getattr(prefs, "gui_theme", None) or {}
        if prefs is not None and getattr(self._shell, "_prefs", None) is not None:
            self._shell._prefs.gui_theme = active
        base = active.get("base") if isinstance(active, dict) else None
        overrides = active.get("overrides") if isinstance(active, dict) else {}
        if base not in _GUI_THEMES:
            base = "Default"
        if not isinstance(overrides, dict):
            overrides = {}
        return {
            "tokens": GUI_THEME_TOKENS,
            "themes": [{"name": n, "colors": c} for n, c in _GUI_THEMES.items()],
            "active": {"base": base, "overrides": overrides},
        }

    def _apply_theme(self, base: str, overrides: dict) -> dict:
        from app.settings.user_prefs import save_prefs

        if base not in _GUI_THEMES:
            raise ValueError(f"unknown theme: {base!r}")
        clean: dict[str, str] = {}
        for token, val in (overrides or {}).items():
            if token in GUI_THEME_TOKENS and _valid_color(val):
                clean[token] = str(val).strip()
        prefs = getattr(self._shell, "_prefs", None)
        if prefs is None:
            raise RuntimeError("preferences unavailable (no prefs)")
        with self._lock:
            prefs.gui_theme = {"base": base, "overrides": clean}
            save_prefs(prefs)
        return {"base": base, "overrides": clean}

    # -- dashboard ---------------------------------------------------------

    def _status(self) -> dict:
        """Health snapshot for the dashboard — no secrets leave the process."""
        from app.config import keychain_available, keychain_read_failed

        shell = self._shell
        cfg = getattr(shell, "_config", None)
        state = getattr(shell, "_state", None)
        scm = getattr(shell, "_scm", None)

        scm_cfg = getattr(cfg, "scm", None) if cfg else None
        has_bearer = bool(getattr(scm_cfg, "bearer_token", "")) if scm_cfg else False
        has_oauth = bool(
            getattr(scm_cfg, "client_id", "") and getattr(scm_cfg, "client_secret", "")
            and getattr(scm_cfg, "tsg_id", "")
        ) if scm_cfg else False

        return {
            "scm_connected": scm is not None,
            "scm_configured": bool(has_bearer or has_oauth),
            "auth_method": "bearer" if has_bearer else ("service-account" if has_oauth else "none"),
            "keychain_available": keychain_available(),
            "keychain_read_failed": keychain_read_failed(),
            "profile": getattr(cfg, "profile_name", "default") if cfg else "default",
            "tsg": (getattr(state, "tsg_id", "") if state else "")
                   or (getattr(scm_cfg, "tsg_id", "") if scm_cfg else ""),
            "folder": getattr(state, "folder", "Shared") if state else "Shared",
            "device": bool(getattr(state, "device", None)) if state else False,
            "debug": bool(getattr(cfg, "debug", False)) if cfg else False,
            "features_gui_port": getattr(getattr(cfg, "features_gui", None), "port", 4445) if cfg else 4445,
            "arc_gui_port": getattr(getattr(cfg, "arc_gui", None), "port", 4444) if cfg else 4444,
            "token_expiry": getattr(scm_cfg, "token_expiry", 0) if scm_cfg else 0,
            "auth_storage": getattr(cfg, "auth_storage", "keychain") if cfg else "keychain",
        }

    # -- preferences -------------------------------------------------------

    def _get_prefs(self) -> dict:
        p = getattr(self._shell, "_prefs", None)
        return {
            "terminal_length": getattr(p, "terminal_length", 0),
            "terminal_width": getattr(p, "terminal_width", 0),
            "terminal_height": getattr(p, "terminal_height", 0),
            "spinner": bool(getattr(p, "spinner", True)),
            "aliases": dict(getattr(p, "aliases", {}) or {}),
        }

    def _apply_prefs(self, data: dict) -> dict:
        from app.settings.user_prefs import save_prefs

        p = getattr(self._shell, "_prefs", None)
        if p is None:
            raise RuntimeError("preferences unavailable")
        with self._lock:
            for key in ("terminal_length", "terminal_width", "terminal_height"):
                if key in data:
                    try:
                        val = int(data[key])
                    except (TypeError, ValueError):
                        raise ValueError(f"{key} must be a non-negative integer")
                    # Clamp to a sane range (0 = auto/disabled; upper bound guards
                    # against absurd values that would break rendering/paging).
                    setattr(p, key, max(0, min(val, 10000)))
            if "spinner" in data:
                p.spinner = bool(data["spinner"])
            save_prefs(p)
        return self._get_prefs()

    # -- config.json -------------------------------------------------------

    def _get_config(self) -> dict:
        from app.config import _read_config_file, _to_new_format

        cfg = getattr(self._shell, "_config", None)
        raw = _to_new_format(_read_config_file())
        profiles = sorted((raw.get("profiles") or {}).keys()) or ["default"]
        return {
            "default_folder": getattr(cfg, "default_folder", "Shared") if cfg else "Shared",
            "debug": bool(getattr(cfg, "debug", False)) if cfg else False,
            "profile": getattr(cfg, "profile_name", "default") if cfg else "default",
            "profiles": profiles,
            "features_gui": {
                "enabled": bool(getattr(getattr(cfg, "features_gui", None), "enabled", True)) if cfg else True,
                "port": getattr(getattr(cfg, "features_gui", None), "port", 4445) if cfg else 4445,
            },
            "arc_gui": {
                "enabled": bool(getattr(getattr(cfg, "arc_gui", None), "enabled", True)) if cfg else True,
                "port": getattr(getattr(cfg, "arc_gui", None), "port", 4444) if cfg else 4444,
            },
        }

    def _apply_config(self, data: dict) -> dict:
        from app.config import save_config

        cfg = getattr(self._shell, "_config", None)
        if cfg is None:
            raise RuntimeError("config unavailable")

        def _port(v, lo=1, hi=65535):
            try:
                n = int(v)
            except (TypeError, ValueError):
                raise ValueError("port must be a number")
            if not (lo <= n <= hi):
                raise ValueError(f"port must be {lo}–{hi}")
            return n

        with self._lock:
            if "default_folder" in data:
                cfg.default_folder = str(data["default_folder"]).strip() or "Shared"
            if "debug" in data:
                cfg.debug = bool(data["debug"])
            fg = data.get("features_gui") or {}
            if "enabled" in fg:
                cfg.features_gui.enabled = bool(fg["enabled"])
            if "port" in fg:
                cfg.features_gui.port = _port(fg["port"])
            ag = data.get("arc_gui") or {}
            if "enabled" in ag:
                cfg.arc_gui.enabled = bool(ag["enabled"])
            if "port" in ag:
                cfg.arc_gui.port = _port(ag["port"])
            if cfg.features_gui.port == cfg.arc_gui.port:
                raise ValueError("feature editor and settings console must use different ports")
            save_config(cfg)
        return self._get_config()

    # -- API sources (panos / scm) ----------------------------------------

    def _sources_path(self, which: str):
        from app.paths import PANOS_SOURCES_FILE, SCM_SOURCES_FILE

        if which == "panos":
            return PANOS_SOURCES_FILE
        if which == "scm":
            return SCM_SOURCES_FILE
        raise ValueError("which must be 'panos' or 'scm'")

    def _get_sources(self, which: str) -> dict:
        import json as _json

        path = self._sources_path(which)
        try:
            data = _json.loads(path.read_text(encoding="utf-8"))
        except (OSError, _json.JSONDecodeError):
            data = {}
        raw = _json.dumps(data, indent=2)
        if which == "panos":
            return {
                "which": which, "path": str(path), "raw": raw,
                "site": data.get("_site", ""),
                "pages": data.get("pages", []),
            }
        # scm — structured view + raw fallback
        settings = data.get("settings", {}) if isinstance(data.get("settings"), dict) else {}
        return {
            "which": which, "path": str(path), "raw": raw,
            "repo": data.get("repo", ""),
            "branch": data.get("branch", ""),
            "settings": {
                "specs_root": settings.get("specs_root", ""),
                "guides_root": settings.get("guides_root", ""),
                "mirror_all_specs": bool(settings.get("mirror_all_specs", False)),
                "mirror_all_guides": bool(settings.get("mirror_all_guides", False)),
            },
            "specs": data.get("specs", {}) if isinstance(data.get("specs"), dict) else {},
            "guides": data.get("guides", {}) if isinstance(data.get("guides"), dict) else {},
        }

    def _apply_sources(self, which: str, data: dict) -> dict:
        import json as _json

        path = self._sources_path(which)
        # Raw override wins when supplied (Advanced editor).
        if data.get("raw") is not None:
            try:
                parsed = _json.loads(data["raw"])
            except _json.JSONDecodeError as exc:
                raise ValueError(f"invalid JSON: {exc}")
            with self._lock:
                path.write_text(_json.dumps(parsed, indent=2) + "\n", encoding="utf-8")
            return self._get_sources(which)

        try:
            current = _json.loads(path.read_text(encoding="utf-8"))
        except (OSError, _json.JSONDecodeError):
            current = {}

        if which == "panos":
            if "site" in data:
                current["_site"] = data["site"]
            if "pages" in data:
                pages = []
                for p in data["pages"]:
                    if not isinstance(p, dict) or not p.get("url"):
                        continue
                    pages.append({
                        "key": str(p.get("key", "")).strip(),
                        "url": str(p.get("url", "")).strip(),
                        "kind": str(p.get("kind", "")).strip(),
                        "version": str(p.get("version", "")).strip(),
                    })
                current["pages"] = pages
        else:  # scm — merge structured fields, preserve everything else
            if "repo" in data:
                current["repo"] = str(data["repo"]).strip()
            if "branch" in data:
                current["branch"] = str(data["branch"]).strip()
            s = data.get("settings") or {}
            if s:
                cur_s = current.get("settings") if isinstance(current.get("settings"), dict) else {}
                for k in ("specs_root", "guides_root"):
                    if k in s:
                        cur_s[k] = str(s[k]).strip()
                for k in ("mirror_all_specs", "mirror_all_guides"):
                    if k in s:
                        cur_s[k] = bool(s[k])
                current["settings"] = cur_s
            for mapkey in ("specs", "guides"):
                if mapkey in data and isinstance(data[mapkey], dict):
                    current[mapkey] = {str(k): str(v) for k, v in data[mapkey].items() if k}
        with self._lock:
            path.write_text(_json.dumps(current, indent=2) + "\n", encoding="utf-8")
        return self._get_sources(which)

    # -- branding & variables ---------------------------------------------

    def _get_branding(self) -> dict:
        import json as _json
        from app.paths import APP_VARIABLES_JSON, BANNER_FILE, GOODBYE_FILE

        def _read(p):
            try:
                return p.read_text(encoding="utf-8")
            except OSError:
                return ""

        # goodbye.txt: leading '##' comment lines are the header; the rest are
        # the random lines shown on exit.
        header, glines = [], []
        for line in _read(GOODBYE_FILE).splitlines():
            if line.strip().startswith("##") and not glines:
                header.append(line)
            elif line.strip():
                glines.append(line)

        # app-variables.json: editable = non-underscore keys; underscore keys
        # (comments/meta) are preserved server-side and shown read-only.
        try:
            av = _json.loads(APP_VARIABLES_JSON.read_text(encoding="utf-8"))
        except (OSError, _json.JSONDecodeError):
            av = {}
        av_entries = [
            {"key": k, "value": v}
            for k, v in av.items()
            if not str(k).startswith("_") and isinstance(v, str)
        ]
        return {
            "banner": _read(BANNER_FILE),
            "goodbye_header": "\n".join(header),
            "goodbye_lines": glines,
            "app_variables": av_entries,
        }

    def _apply_branding(self, data: dict) -> dict:
        import json as _json
        from app.paths import APP_VARIABLES_JSON, BANNER_FILE, GOODBYE_FILE

        with self._lock:
            if "banner" in data:
                BANNER_FILE.write_text(str(data["banner"]), encoding="utf-8")
            if "goodbye_lines" in data:
                header = str(data.get("goodbye_header", "")).strip()
                lines = [str(x) for x in data["goodbye_lines"] if str(x).strip()]
                out = ([header] if header else ["## ARC goodbye lines (one random line shown on exit)"]) + lines
                GOODBYE_FILE.write_text("\n".join(out) + "\n", encoding="utf-8")
            if "app_variables" in data:
                # Preserve underscore/meta keys + order; update/replace the
                # editable (non-underscore) keys from the submitted entries.
                try:
                    current = _json.loads(APP_VARIABLES_JSON.read_text(encoding="utf-8"))
                except (OSError, _json.JSONDecodeError):
                    current = {}
                submitted = {}
                for e in data["app_variables"]:
                    if isinstance(e, dict) and str(e.get("key", "")).strip() and not str(e["key"]).startswith("_"):
                        submitted[str(e["key"]).strip()] = str(e.get("value", ""))
                rebuilt = {}
                for k, v in current.items():
                    if str(k).startswith("_"):
                        rebuilt[k] = v
                    elif k in submitted:
                        rebuilt[k] = submitted.pop(k)
                    # dropped keys are omitted
                for k, v in submitted.items():  # newly added keys
                    rebuilt[k] = v
                APP_VARIABLES_JSON.write_text(_json.dumps(rebuilt, indent=2) + "\n", encoding="utf-8")
        return self._get_branding()

    # -- credentials & keychain -------------------------------------------

    def _get_credentials(self) -> dict:
        from app.config import keychain_available

        cfg = getattr(self._shell, "_config", None)
        scm = getattr(cfg, "scm", None)
        ssh = getattr(cfg, "ssh", None)
        has_bearer = bool(getattr(scm, "bearer_token", "")) if scm else False
        has_secret = bool(getattr(scm, "client_secret", "")) if scm else False
        has_oauth = bool(
            getattr(scm, "client_id", "") and has_secret and getattr(scm, "tsg_id", "")
        ) if scm else False
        return {
            "keychain_available": keychain_available(),
            "auth_method": getattr(cfg, "auth_method", "service") if cfg else "service",
            "auth_storage": getattr(cfg, "auth_storage", "keychain") if cfg else "keychain",
            "token_expiry": getattr(scm, "token_expiry", 0) if scm else 0,
            "scm": {
                "client_id": getattr(scm, "client_id", "") if scm else "",
                "tsg_id": getattr(scm, "tsg_id", "") if scm else "",
                "has_secret": has_secret,
                "has_bearer": has_bearer,
                "auth_method": "bearer" if has_bearer else ("service-account" if has_oauth else "none"),
            },
            "ssh": {
                "user": getattr(ssh, "user", "") if ssh else "",
                "key_path": getattr(ssh, "key_path", "") if ssh else "",
                "key_enabled": bool(getattr(ssh, "key_path", "")) if ssh else False,
                "port": getattr(ssh, "port", 22) if ssh else 22,
                "has_password": bool(getattr(ssh, "password", "")) if ssh else False,
            },
        }

    def _apply_credentials(self, data: dict) -> dict:
        """Update credentials; secrets go to the OS keychain or auth.json per mode."""
        from app.config import ConfigSecurityError, save_config

        cfg = getattr(self._shell, "_config", None)
        if cfg is None:
            raise RuntimeError("config unavailable")
        scm = data.get("scm") or {}
        ssh = data.get("ssh") or {}
        # Blank secret fields are treated as "leave unchanged" (the GUI never
        # reads secrets back, so an empty field must not wipe a stored one).
        with self._lock:
            # Storage mode (the GUI's only auth toggle). auth_method is derived
            # from which credentials exist, not sent by the credentials form.
            if data.get("auth_storage") in ("keychain", "file"):
                cfg.auth_storage = data["auth_storage"]
            if "client_id" in scm:
                cfg.scm.client_id = str(scm["client_id"]).strip()
            if "tsg_id" in scm:
                cfg.scm.tsg_id = str(scm["tsg_id"]).strip()
            if scm.get("client_secret"):
                cfg.scm.client_secret = str(scm["client_secret"]).strip()
            if scm.get("bearer_token"):
                cfg.scm.bearer_token = str(scm["bearer_token"]).strip()
            if scm.get("clear_bearer"):
                cfg.scm.bearer_token = ""
            if "user" in ssh:
                cfg.ssh.user = str(ssh["user"]).strip()
            # SSH key toggle: when disabled, clear the key path (password auth).
            if ssh.get("key_enabled") is False:
                cfg.ssh.key_path = ""
            elif "key_path" in ssh:
                cfg.ssh.key_path = str(ssh["key_path"]).strip()
            if "port" in ssh:
                try:
                    cfg.ssh.port = int(ssh["port"])
                except (TypeError, ValueError):
                    raise ValueError("SSH port must be a number")
            if ssh.get("password"):
                cfg.ssh.password = str(ssh["password"])
            try:
                save_config(cfg)
            except ConfigSecurityError as exc:
                raise RuntimeError(str(exc))
        return self._get_credentials()

    def _test_auth(self) -> dict:
        """Attempt SCM authentication with the current credentials."""
        from app.api.client import SCMClient

        cfg = getattr(self._shell, "_config", None)
        scm_cfg = getattr(cfg, "scm", None)
        if scm_cfg is None or not scm_cfg.is_configured:
            return {"ok": False, "message": "SCM is not configured — add a bearer token or service-account credentials."}
        try:
            client = SCMClient(scm_cfg)
            client.get_folders()  # lightweight authenticated call
            return {"ok": True, "message": "Authentication succeeded — SCM is reachable."}
        except Exception as exc:  # noqa: BLE001
            return {"ok": False, "message": f"Authentication failed: {exc}"}

    # -- maintenance -------------------------------------------------------

    def _run_maintenance(self, action: str) -> dict:
        """Run a maintenance script (docs/commands update, catalog rebuild)."""
        import subprocess
        import sys
        from app.paths import REPO_ROOT

        scripts = {
            "docs": ["app/scripts/docsupdate.py"],
            "commands": ["app/scripts/commandupdate.py"],
            "update-all": ["app/scripts/docsupdate.py", "app/scripts/commandupdate.py"],
            "rebuild": ["app/scripts/generate_resource_catalog.py"],
        }
        if action not in scripts:
            raise ValueError(f"unknown maintenance action: {action!r}")

        repo_root = REPO_ROOT.resolve()
        outputs: list[str] = []
        ok = True
        for rel in scripts[action]:
            # Resolve to an absolute path and confirm it stays inside the repo
            # and exists before executing — defense-in-depth even though the
            # action set above is a fixed allowlist.
            script = (repo_root / rel).resolve()
            if not (script.is_file() and script.is_relative_to(repo_root)):
                ok = False
                outputs.append(f"$ {rel}\n[error] script not found under repo")
                break
            try:
                proc = subprocess.run(
                    [sys.executable, str(script)],
                    cwd=str(repo_root), capture_output=True, text=True, timeout=600,
                )
                outputs.append(f"$ {rel}\n{proc.stdout}\n{proc.stderr}".strip())
                if proc.returncode != 0:
                    ok = False
                    break
            except subprocess.TimeoutExpired:
                ok = False
                outputs.append(f"$ {rel}\n[timed out after 600s]")
                break
            except Exception as exc:  # noqa: BLE001
                ok = False
                outputs.append(f"$ {rel}\n[error] {exc}")
                break
        return {"ok": ok, "action": action, "output": "\n\n".join(outputs)}
