"""Config loader — reads from environment variables and the project config directory.

Sensitive credentials (bearer tokens, client secrets, SSH passwords) are
stored in the OS keychain via the ``keyring`` library:

  - macOS  : Keychain
  - Linux  : Secret Service (GNOME Keyring / KWallet)
  - Windows: Windows Credential Manager

Non-sensitive values (client_id, tsg_id, default_folder, SSH user/key/port)
are stored in ``<project_root>/config/<os_username>/config.json``, which is
always written with mode 0600.

Environment variables override both the keychain and the config file —
useful for CI/CD and short-lived overrides without touching stored values.

Named profiles allow multiple SCM service accounts to coexist — e.g. a
read-only account for day-to-day monitoring and a read-write account for
policy changes.  Use ``arc auth configure --profile <name>`` to create a profile
and ``account <name>`` in the ARC shell to switch between them.
"""

from __future__ import annotations

import getpass as _getpass
import json
import logging
import os
import stat
import threading
from dataclasses import dataclass, field
from pathlib import Path

import keyring
import keyring.errors

logger = logging.getLogger(__name__)

# Serializes read-modify-write access to config.json.  Both save_config() and
# save_prefs() (and delete_profile()) mutate the same file; this lock makes each
# read-modify-write atomic w.r.t. the others so concurrent writers (e.g. the
# threaded GUI server) can't clobber each other's blocks.
_CONFIG_WRITE_LOCK = threading.RLock()

# ---------------------------------------------------------------------------
# Config path — <project_root>/config/<os_username>/config.json
# ---------------------------------------------------------------------------

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_OS_USERNAME  = _getpass.getuser()

CONFIG_DIR  = _PROJECT_ROOT / "config" / _OS_USERNAME
CONFIG_FILE = CONFIG_DIR / "config.json"
# All auth data (ids + real token expiry; plaintext secrets only in "file" mode).
AUTH_FILE   = CONFIG_DIR / "auth.json"

_AUTH_WARNING = (
    "ARC auth store. In 'keychain' mode this holds only non-secret identifiers; "
    "in 'file' mode it ALSO holds plaintext secrets (client secret, bearer token, "
    "SSH password). Keep this file private (chmod 600) and out of version control."
)

# Legacy path (platformdirs-based — used by earlier ARC versions).
try:
    import platformdirs as _platformdirs
    _LEGACY_CONFIG_FILE: Path | None = Path(_platformdirs.user_config_dir("arc")) / "config.json"
except ImportError:
    _LEGACY_CONFIG_FILE = None

# ---------------------------------------------------------------------------
# Profile support
# ---------------------------------------------------------------------------

# The built-in profile name.  All legacy (single-profile) configs are treated
# as this profile; its keychain keys use the historic non-suffixed format.
_DEFAULT_PROFILE = "default"

# Keychain service name — all ARC entries group under this in macOS Keychain Access.
_KEYCHAIN_SERVICE = "arc"

# ---------------------------------------------------------------------------
# Keychain key names — these are the "Account" field in macOS Keychain Access.
# Naming convention: arc.<domain>.<role>
#   arc.bearer.token    — SCM pre-issued bearer token
#   arc.bearer.password — SCM OAuth client secret (used to generate bearer tokens)
#   arc.shell.username  — SSH username for device connections
#   arc.shell.password  — SSH password for device connections
#
# Profile-scoped variants append .<profile>:  arc.bearer.token.readwrite
# ---------------------------------------------------------------------------
_KEY_SCM_BEARER    = "arc.bearer.token"
_KEY_SCM_SECRET    = "arc.bearer.password"
_KEY_SSH_USER      = "arc.shell.username"
_KEY_SSH_PASSWORD  = "arc.shell.password"

# Legacy key names (used by older ARC versions — read during migration, cleared on save).
# Never write to these; only read them as fallback when the new keys are empty.
_LEGACY_KEY_SCM_BEARER   = "scm.bearer_token"
_LEGACY_KEY_SCM_SECRET   = "scm.client_secret"
_LEGACY_KEY_SSH_PASSWORD = "ssh.password"
# ssh.user was never in the keychain before — no legacy key needed.


def _profile_key(base: str, profile: str) -> str:
    """Return a profile-scoped keychain key.

    The ``default`` profile uses the historic non-suffixed keys so that
    existing keychain entries are read without migration.  All other profiles
    append a dot-separated profile name: ``scm.bearer_token.readwrite``.
    """
    if profile == _DEFAULT_PROFILE:
        return base
    return f"{base}.{profile}"


class ConfigSecurityError(Exception):
    """Raised when ARC refuses to persist secrets insecurely."""


# ---------------------------------------------------------------------------
# Keychain helpers
# ---------------------------------------------------------------------------

# Set when any keychain read raises — lets the shell warn once at startup
# instead of silently running with empty credentials.
_keychain_read_failed = False


def keychain_read_failed() -> bool:
    """True when at least one keychain read failed this process (backend down)."""
    return _keychain_read_failed


def _keychain_get(key: str) -> str:
    """Return a credential from the OS keychain, or '' if absent / unavailable."""
    global _keychain_read_failed
    try:
        value = keyring.get_password(_KEYCHAIN_SERVICE, key)
        return value or ""
    except keyring.errors.KeyringError as exc:
        _keychain_read_failed = True
        logger.debug("Keychain read failed for %s: %s", key, exc)
        return ""


def _keychain_set(key: str, value: str) -> bool:
    """Store *value* in the OS keychain.  Returns True on success.

    An empty value deletes the entry rather than storing a blank secret.
    """
    try:
        if value:
            keyring.set_password(_KEYCHAIN_SERVICE, key, value)
        else:
            _keychain_delete(key)
        return True
    except keyring.errors.KeyringError as exc:
        logger.warning("Keychain write failed for %s: %s", key, exc)
        return False


def _keychain_delete(key: str) -> None:
    """Remove a credential from the keychain.  Silently ignores missing entries."""
    try:
        keyring.delete_password(_KEYCHAIN_SERVICE, key)
    except keyring.errors.PasswordDeleteError:
        pass  # already absent — not an error
    except keyring.errors.KeyringError as exc:
        logger.debug("Keychain delete failed for %s: %s", key, exc)


def keychain_available() -> bool:
    """Return True when the OS keychain can be read/written."""
    try:
        keyring.get_password(_KEYCHAIN_SERVICE, "__probe__")
        return True
    except keyring.errors.KeyringError:
        return False


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class SCMConfig:
    """SCM API credentials.

    ARC supports either a pre-issued bearer token or OAuth client credentials.
    A bearer token takes precedence when both are present.

    Secrets (bearer_token, client_secret) are stored in the OS keychain.
    client_id and tsg_id are non-sensitive identifiers stored in config.json.
    """

    bearer_token: str = ""
    client_id: str = ""
    client_secret: str = ""
    tsg_id: str = ""
    # Real epoch-seconds expiry of the current bearer token (0 = unknown/none).
    token_expiry: int = 0

    @property
    def is_configured(self) -> bool:
        return bool(self.bearer_token or (self.client_id and self.client_secret and self.tsg_id))


@dataclass
class SSHConfig:
    """SSH connection defaults.

    ``password`` and ``user`` are stored in the OS keychain when available.
    ``key_path`` and ``port`` are non-sensitive and stored in config.json.

    Keychain keys (macOS Keychain Account field):
      arc.shell.username  — SSH username (e.g. admin)
      arc.shell.password  — SSH password
    """

    user: str = "admin"
    key_path: str = ""
    password: str = ""
    port: int = 22
    # Internal: username loaded from keychain; merged into `user` by load_config().
    # Not persisted directly — load_config() sets this before resolving `user`.
    user_from_keychain: str = ""


@dataclass
class FeaturesGuiConfig:
    """Settings for the browser-based feature-flag editor (`feature gui-configure`).

    Non-sensitive; stored at the top level of config.json (not per-profile).
      enabled — whether the `feature gui-configure` command is allowed to launch.
      port    — local port the on-demand HTTP server listens on (127.0.0.1).
    """

    enabled: bool = True
    port: int = 4445


@dataclass
class ArcGuiConfig:
    """Settings for the browser-based ARC settings console (`arc gui-configure`).

    Non-sensitive; stored at the top level of config.json (not per-profile).
      enabled — whether the `arc gui-configure` command is allowed to launch.
      port    — local port the on-demand HTTP server listens on (127.0.0.1).
    """

    enabled: bool = True
    port: int = 4444


@dataclass
class ArcConfig:
    scm: SCMConfig = field(default_factory=SCMConfig)
    ssh: SSHConfig = field(default_factory=SSHConfig)
    features_gui: FeaturesGuiConfig = field(default_factory=FeaturesGuiConfig)
    arc_gui: ArcGuiConfig = field(default_factory=ArcGuiConfig)
    debug: bool = False
    default_folder: str = "Shared"
    # Preferred SCM auth method: "service" (client-credentials) | "bearer".
    auth_method: str = "service"
    # Where auth secrets live: "keychain" (secure, default) | "file" (plaintext auth.json).
    auth_storage: str = "keychain"
    # Which named profile was loaded.  Set automatically by load_config().
    # Used by save_config() to write back to the correct profile slot.
    profile_name: str = _DEFAULT_PROFILE


# ---------------------------------------------------------------------------
# Raw config file I/O
# ---------------------------------------------------------------------------

def _read_config_file() -> dict:
    """Read the raw config.json from disk and return it as a dict.

    Falls back to the legacy platformdirs path if the primary path is missing.
    Returns an empty dict if no config file exists or parsing fails.
    """
    config_file = CONFIG_FILE
    if not config_file.exists() and _LEGACY_CONFIG_FILE and _LEGACY_CONFIG_FILE.exists():
        config_file = _LEGACY_CONFIG_FILE
        logger.debug(
            "Using legacy config path %s — run `arc auth configure` to migrate to %s",
            _LEGACY_CONFIG_FILE, CONFIG_FILE,
        )
    if config_file.exists():
        try:
            return json.loads(config_file.read_text())
        except (OSError, json.JSONDecodeError, TypeError, ValueError) as exc:
            logger.debug("Could not parse config file: %s", exc)
    return {}


def _write_config_file(raw: dict) -> None:
    """Write *raw* to CONFIG_FILE atomically, with mode 0600.

    Writes to a temporary file in the same directory, flushes+fsyncs it, then
    atomically replaces CONFIG_FILE via ``os.replace``.  A crash mid-write can
    therefore never leave a truncated/corrupt config.json — readers see either
    the old file or the complete new one.  Serialized by ``_CONFIG_WRITE_LOCK``.
    """
    import tempfile

    with _CONFIG_WRITE_LOCK:
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        CONFIG_DIR.chmod(stat.S_IRWXU)
        fd, tmp_path = tempfile.mkstemp(dir=str(CONFIG_DIR), prefix=".config-", suffix=".tmp")
        try:
            os.chmod(tmp_path, 0o600)
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                json.dump(raw, handle, indent=2)
                handle.write("\n")
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(tmp_path, CONFIG_FILE)
        except BaseException:
            # Best-effort cleanup of the temp file on any failure.
            try:
                os.unlink(tmp_path)
            except OSError:
                pass
            raise
        CONFIG_FILE.chmod(stat.S_IRUSR | stat.S_IWUSR)


# ---------------------------------------------------------------------------
# auth.json — the auth store (ids + real token expiry; secrets only in file mode)
# ---------------------------------------------------------------------------

def _read_auth_file() -> dict:
    """Read config/<user>/auth.json, or return an empty dict."""
    if AUTH_FILE.exists():
        try:
            data = json.loads(AUTH_FILE.read_text())
            return data if isinstance(data, dict) else {}
        except (OSError, json.JSONDecodeError, TypeError, ValueError) as exc:
            logger.debug("Could not parse auth.json: %s", exc)
    return {}


def _write_auth_file(raw: dict) -> None:
    """Write *raw* to AUTH_FILE atomically at mode 0600 (serialized by the lock)."""
    import tempfile

    payload = {"_warning": _AUTH_WARNING}
    payload.update({k: v for k, v in raw.items() if k != "_warning"})
    with _CONFIG_WRITE_LOCK:
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        CONFIG_DIR.chmod(stat.S_IRWXU)
        fd, tmp_path = tempfile.mkstemp(dir=str(CONFIG_DIR), prefix=".auth-", suffix=".tmp")
        try:
            os.chmod(tmp_path, 0o600)
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                json.dump(payload, handle, indent=2)
                handle.write("\n")
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(tmp_path, AUTH_FILE)
        except BaseException:
            try:
                os.unlink(tmp_path)
            except OSError:
                pass
            raise
        AUTH_FILE.chmod(stat.S_IRUSR | stat.S_IWUSR)


def _auth_storage_mode(config_raw: dict, auth_raw: dict) -> str:
    """Resolve the storage mode ("keychain" | "file") from config/auth files + env."""
    mode = ""
    auth_section = config_raw.get("auth") if isinstance(config_raw, dict) else None
    if isinstance(auth_section, dict):
        mode = str(auth_section.get("storage", "") or "")
    if not mode:
        mode = str(auth_raw.get("storage", "") or "")
    mode = os.environ.get("ARC_AUTH_STORAGE", mode).strip().lower()
    return "file" if mode == "file" else "keychain"



def _to_new_format(raw: dict) -> dict:
    """Migrate a legacy single-profile config dict to the multi-profile format.

    The original top-level ``scm`` / ``ssh`` / ``default_folder`` keys become
    the ``default`` profile.  The original dict is not mutated.
    """
    if "profiles" in raw:
        return raw  # already in (at least) multi-profile format

    legacy_scm = {
        k: v for k, v in raw.get("scm", {}).items()
        if not k.startswith("_") and k not in ("bearer_token", "client_secret")
    }
    legacy_ssh = {
        k: v for k, v in raw.get("ssh", {}).items()
        if not k.startswith("_") and k != "password"
    }
    migrated = {
        "active_profile": raw.get("active_profile", _DEFAULT_PROFILE),
        "profiles": {
            _DEFAULT_PROFILE: {
                "scm": legacy_scm,
                "ssh": legacy_ssh,
                "default_folder": raw.get("default_folder", "Shared"),
            }
        },
    }
    if "features_gui" in raw:
        migrated["features_gui"] = raw["features_gui"]
    if "arc_gui" in raw:
        migrated["arc_gui"] = raw["arc_gui"]
    if "preferences" in raw:
        migrated["preferences"] = raw["preferences"]
    return migrated


def _active_profile_name(config_raw: dict) -> str:
    """Active profile name from the sectioned ``auth`` block, else legacy top-level."""
    auth = config_raw.get("auth") if isinstance(config_raw, dict) else None
    if isinstance(auth, dict) and auth.get("active_profile"):
        return str(auth["active_profile"])
    return str(config_raw.get("active_profile", _DEFAULT_PROFILE))


def _all_profile_names(config_raw: dict, auth_raw: dict) -> list[str]:
    """Configured profiles across auth.json + config.json, preserving order.

    Falls back to ``[default]`` ONLY when nothing is configured, so a user who
    created just named profiles doesn't see a phantom empty ``default`` entry.
    """
    names: list[str] = []
    for src in (auth_raw.get("profiles", {}), config_raw.get("profiles", {})):
        if isinstance(src, dict):
            for name in src:
                if name not in names:
                    names.append(name)
    if not names:
        names.append(_DEFAULT_PROFILE)
    return names


def _profile_auth_ids(config_raw: dict, auth_raw: dict, profile: str) -> tuple[dict, dict]:
    """Return (scm, ssh) auth dicts for *profile*.

    Prefers auth.json; falls back to migrating from the old config.json layout so
    a pre-auth.json install keeps working until the next save rewrites both files.
    """
    aprofiles = auth_raw.get("profiles", {}) if isinstance(auth_raw, dict) else {}
    entry = aprofiles.get(profile)
    if isinstance(entry, dict):
        return (entry.get("scm", {}) or {}, entry.get("ssh", {}) or {})
    cprofiles = config_raw.get("profiles", {}) if isinstance(config_raw, dict) else {}
    pdata = cprofiles.get(profile)
    if isinstance(pdata, dict):
        return (pdata.get("scm", {}) or {}, pdata.get("ssh", {}) or {})
    return (config_raw.get("scm", {}) or {}, config_raw.get("ssh", {}) or {})


def _default_folder_for(config_raw: dict, profile: str) -> str:
    """Per-profile default folder (config.json profiles), with legacy fallback."""
    cprofiles = config_raw.get("profiles", {}) if isinstance(config_raw, dict) else {}
    pdata = cprofiles.get(profile)
    if isinstance(pdata, dict) and pdata.get("default_folder"):
        return str(pdata["default_folder"])
    return str(config_raw.get("default_folder", "Shared"))


# ---------------------------------------------------------------------------
# Profile management
# ---------------------------------------------------------------------------

def list_profiles() -> list[dict]:
    """Return metadata for every configured profile.

    Each entry is a dict with keys: ``name``, ``client_id``, ``tsg_id``,
    ``default_folder``, ``active`` (bool).

    When no config file exists, returns a single placeholder for ``default``.
    """
    config_raw = _read_config_file()
    auth_raw = _read_auth_file()
    active = _active_profile_name(config_raw)
    result: list[dict] = []
    for name in _all_profile_names(config_raw, auth_raw):
        scm_block, _ssh = _profile_auth_ids(config_raw, auth_raw, name)
        result.append({
            "name":           name,
            "client_id":      scm_block.get("client_id", ""),
            "tsg_id":         scm_block.get("tsg_id", ""),
            "default_folder": _default_folder_for(config_raw, name),
            "active":         name == active,
        })
    return result or [{
        "name": _DEFAULT_PROFILE, "client_id": "", "tsg_id": "",
        "default_folder": "Shared", "active": True,
    }]


def has_configured_profiles() -> bool:
    """True if any real credential profile has been persisted.

    Distinguishes a fresh install (no profiles materialized — ``_all_profile_names``
    would only return the synthetic ``default`` fallback) from one that already has
    at least one saved profile.  Used to decide whether first-time setup may
    auto-name the initial profile after the account.
    """
    config_raw = _read_config_file()
    auth_raw = _read_auth_file()
    for src in (auth_raw.get("profiles"), config_raw.get("profiles")):
        if isinstance(src, dict) and src:
            return True
    return False


def get_active_profile() -> str:
    """Return the name of the currently active profile (default: ``"default"``)."""
    return _active_profile_name(_read_config_file())


def set_active_profile(name: str) -> None:
    """Persist *name* as the active profile without touching credential data."""
    with _CONFIG_WRITE_LOCK:
        raw = _read_config_file()
        auth = raw.get("auth")
        if not isinstance(auth, dict):
            auth = {}
        auth["active_profile"] = name
        raw["auth"] = auth
        raw.pop("active_profile", None)  # drop legacy top-level key
        _write_config_file(raw)


# ---------------------------------------------------------------------------
# Load / save
# ---------------------------------------------------------------------------

def load_config(profile: str | None = None) -> ArcConfig:
    """Load config for the named *profile* (or the active profile when None).

    Priority (later overrides earlier):
      1. OS keychain (profile-scoped secrets)
      2. config.json profile block (non-sensitive fields; legacy plaintext as fallback)
      3. Environment variables (always win)
    """
    cfg = ArcConfig()
    config_raw = _read_config_file()
    auth_raw = _read_auth_file()

    active = _active_profile_name(config_raw)
    target = profile or active
    # Fall back to active if the requested profile is unknown to both stores.
    if target not in _all_profile_names(config_raw, auth_raw):
        logger.debug("Profile '%s' not found; falling back to '%s'", target, active)
        target = active
    cfg.profile_name = target

    storage = _auth_storage_mode(config_raw, auth_raw)
    cfg.auth_storage = storage

    # Preferred auth method (config.json auth section).
    auth_section = config_raw.get("auth") if isinstance(config_raw, dict) else None
    if isinstance(auth_section, dict) and auth_section.get("preferred_method"):
        cfg.auth_method = str(auth_section["preferred_method"])

    scm_raw, ssh_raw = _profile_auth_ids(config_raw, auth_raw, target)
    cfg.default_folder = _default_folder_for(config_raw, target)

    # --- Non-secret ids (auth.json / migrated legacy config) ---
    cfg.scm.client_id = scm_raw.get("client_id", "")
    cfg.scm.tsg_id    = scm_raw.get("tsg_id", "")
    try:
        cfg.scm.token_expiry = int(scm_raw.get("token_expiry", 0) or 0)
    except (TypeError, ValueError):
        cfg.scm.token_expiry = 0

    # --- Secrets: from auth.json (file mode) or the OS keychain (keychain mode) ---
    if storage == "file":
        cfg.scm.bearer_token  = scm_raw.get("bearer_token", "") or scm_raw.get("token", "")
        cfg.scm.client_secret = scm_raw.get("client_secret", "")
        cfg.ssh.password      = ssh_raw.get("password", "")
    else:
        bearer_key   = _profile_key(_KEY_SCM_BEARER,   target)
        secret_key   = _profile_key(_KEY_SCM_SECRET,   target)
        ssh_pass_key = _profile_key(_KEY_SSH_PASSWORD, target)
        cfg.scm.bearer_token  = _keychain_get(bearer_key)
        cfg.scm.client_secret = _keychain_get(secret_key)
        cfg.ssh.password      = _keychain_get(ssh_pass_key)
        # Legacy keychain key migration (pre-rename / pre-auth.json installs).
        if target == _DEFAULT_PROFILE:
            if not cfg.scm.bearer_token:
                cfg.scm.bearer_token  = _keychain_get(_LEGACY_KEY_SCM_BEARER)
            if not cfg.scm.client_secret:
                cfg.scm.client_secret = _keychain_get(_LEGACY_KEY_SCM_SECRET)
            if not cfg.ssh.password:
                cfg.ssh.password      = _keychain_get(_LEGACY_KEY_SSH_PASSWORD)
        if not cfg.scm.bearer_token:
            cfg.scm.bearer_token  = _keychain_get(_profile_key(_LEGACY_KEY_SCM_BEARER, target))
        if not cfg.scm.client_secret:
            cfg.scm.client_secret = _keychain_get(_profile_key(_LEGACY_KEY_SCM_SECRET, target))
        if not cfg.ssh.password:
            cfg.ssh.password      = _keychain_get(_profile_key(_LEGACY_KEY_SSH_PASSWORD, target))
        # Legacy plaintext secrets in an old config.json (pre-auth.json) — last resort.
        if not cfg.scm.bearer_token:
            cfg.scm.bearer_token  = scm_raw.get("bearer_token", "")
        if not cfg.scm.client_secret:
            cfg.scm.client_secret = scm_raw.get("client_secret", "")

    # SSH non-secret fields (auth.json uses "user"; legacy config used "username").
    cfg.ssh.user = ssh_raw.get("user", ssh_raw.get("username", "admin"))
    cfg.ssh.key_path = ssh_raw.get("key_path", "")
    try:
        cfg.ssh.port = int(ssh_raw.get("port", 22))
    except (TypeError, ValueError):
        cfg.ssh.port = 22

    # --- Environment variables always win ---
    cfg.scm.bearer_token  = os.environ.get("SCM_BEARER_TOKEN",  cfg.scm.bearer_token)
    cfg.scm.client_id     = os.environ.get("SCM_CLIENT_ID",     cfg.scm.client_id)
    cfg.scm.client_secret = os.environ.get("SCM_CLIENT_SECRET", cfg.scm.client_secret)
    cfg.scm.tsg_id        = os.environ.get("SCM_TSG_ID",        cfg.scm.tsg_id)
    cfg.ssh.user          = os.environ.get("ARC_SSH_USER",       cfg.ssh.user)
    cfg.ssh.key_path      = os.environ.get("ARC_SSH_KEY",        cfg.ssh.key_path)
    cfg.ssh.password      = os.environ.get("ARC_SSH_PASS",       cfg.ssh.password)
    cfg.debug             = os.environ.get("ARC_DEBUG", "0") == "1"

    # --- GUI blocks: sectioned config.json `gui.{features,arc}`, legacy fallback ---
    gui_section = config_raw.get("gui") if isinstance(config_raw, dict) else None
    gui_section = gui_section if isinstance(gui_section, dict) else {}
    feat_raw = gui_section.get("features") or config_raw.get("features_gui") or {}
    if isinstance(feat_raw, dict):
        cfg.features_gui.enabled = bool(feat_raw.get("enabled", True))
        try:
            cfg.features_gui.port = int(feat_raw.get("port", 4445))
        except (TypeError, ValueError):
            cfg.features_gui.port = 4445
    arc_raw = gui_section.get("arc") or config_raw.get("arc_gui") or {}
    if isinstance(arc_raw, dict):
        cfg.arc_gui.enabled = bool(arc_raw.get("enabled", True))
        try:
            cfg.arc_gui.port = int(arc_raw.get("port", 4444))
        except (TypeError, ValueError):
            cfg.arc_gui.port = 4444

    return cfg


def save_config(cfg: ArcConfig, profile: str | None = None) -> None:
    """Persist config: secrets to OS keychain, non-sensitive values to config.json.

    *profile* overrides ``cfg.profile_name`` when supplied.  Defaults to
    ``cfg.profile_name`` (set by ``load_config``), which falls back to
    ``"default"`` if not set.

    The config file is always written in the sectioned format; auth values go to
    auth.json (secrets there only in "file" storage mode, else the OS keychain).

    In keychain mode, if the OS keychain cannot store a non-empty secret, the rest
    is still saved and ``ConfigSecurityError`` is raised.
    """
    target = profile or cfg.profile_name or _DEFAULT_PROFILE
    storage = (cfg.auth_storage or "keychain").strip().lower()
    storage = "file" if storage == "file" else "keychain"

    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_DIR.chmod(stat.S_IRWXU)

    failed_secret_keys: list[str] = []
    if storage == "keychain":
        # Secrets → OS keychain (profile-scoped). SSH user is non-secret (auth.json).
        for key, value in (
            (_profile_key(_KEY_SCM_BEARER,   target), cfg.scm.bearer_token),
            (_profile_key(_KEY_SCM_SECRET,   target), cfg.scm.client_secret),
            (_profile_key(_KEY_SSH_PASSWORD, target), cfg.ssh.password),
        ):
            saved = _keychain_set(key, value)
            if value and not saved:
                failed_secret_keys.append(key)
        if target == _DEFAULT_PROFILE:
            for legacy_key in (_LEGACY_KEY_SCM_BEARER, _LEGACY_KEY_SCM_SECRET, _LEGACY_KEY_SSH_PASSWORD):
                _keychain_delete(legacy_key)
    else:
        # File mode: secrets live in auth.json — purge any keychain copies so the
        # two stores never disagree.
        for base in (_KEY_SCM_BEARER, _KEY_SCM_SECRET, _KEY_SSH_USER, _KEY_SSH_PASSWORD):
            _keychain_delete(_profile_key(base, target))

    # --- auth.json: all auth ids + real token_expiry; secrets only in file mode ---
    scm_entry: dict = {"client_id": cfg.scm.client_id, "tsg_id": cfg.scm.tsg_id}
    if cfg.scm.token_expiry:
        scm_entry["token_expiry"] = int(cfg.scm.token_expiry)
    ssh_entry: dict = {"user": cfg.ssh.user, "key_path": cfg.ssh.key_path, "port": cfg.ssh.port}
    if storage == "file":
        if cfg.scm.client_secret:
            scm_entry["client_secret"] = cfg.scm.client_secret
        if cfg.scm.bearer_token:
            scm_entry["bearer_token"] = cfg.scm.bearer_token
        if cfg.ssh.password:
            ssh_entry["password"] = cfg.ssh.password

    with _CONFIG_WRITE_LOCK:
        auth_raw = _read_auth_file()
        auth_raw["storage"] = storage
        profiles = auth_raw.get("profiles")
        if not isinstance(profiles, dict):
            profiles = {}
        profiles[target] = {"scm": scm_entry, "ssh": ssh_entry}
        if storage == "keychain":
            # keychain mode keeps long-lived secrets out of auth.json. Switching
            # the (global) storage mode file→keychain must also scrub cleartext
            # secrets left in OTHER profiles by a previous file-mode session — not
            # just the profile being saved. (A per-profile session bearer_token is
            # ephemeral state, so it is left alone.)
            for pdata in profiles.values():
                if not isinstance(pdata, dict):
                    continue
                pscm = pdata.get("scm")
                if isinstance(pscm, dict):
                    pscm.pop("client_secret", None)
                pssh = pdata.get("ssh")
                if isinstance(pssh, dict):
                    pssh.pop("password", None)
        auth_raw["profiles"] = profiles
        _write_auth_file(auth_raw)

        # --- config.json: sectioned, non-secret only ---
        raw = _read_config_file()
        # Drop legacy top-level auth/profile shapes that we've now migrated
        # (default_folder now lives per-profile under profiles.<name>).
        for legacy in ("scm", "ssh", "features_gui", "arc_gui", "active_profile",
                       "oauth", "default_folder"):
            raw.pop(legacy, None)
        auth_section = raw.get("auth")
        if not isinstance(auth_section, dict):
            auth_section = {}
        auth_section["preferred_method"] = cfg.auth_method or "service"
        auth_section["storage"] = storage
        auth_section.setdefault("active_profile", target)
        raw["auth"] = auth_section
        raw["gui"] = {
            "features": {"enabled": cfg.features_gui.enabled, "port": cfg.features_gui.port},
            "arc":      {"enabled": cfg.arc_gui.enabled, "port": cfg.arc_gui.port},
        }
        profs = raw.get("profiles")
        if not isinstance(profs, dict):
            profs = {}
        # Reset the profile block to the non-secret default folder, dropping any
        # auth ids that lingered in an old config.json.
        profs[target] = {"default_folder": cfg.default_folder}
        raw["profiles"] = profs
        _order = ["preferences", "auth", "gui", "profiles"]
        raw = {**{k: raw[k] for k in _order if k in raw},
               **{k: v for k, v in raw.items() if k not in _order}}
        _write_config_file(raw)

    if failed_secret_keys:
        failed = ", ".join(failed_secret_keys)
        raise ConfigSecurityError(
            f"OS keychain could not store ARC secret(s): {failed}. "
            "Secrets were not written to disk. "
            "Use a machine with keychain access, choose file storage, or provide "
            "secrets through environment variables for this session."
        )


def save_session_token(
    profile: str,
    *,
    client_id: str,
    tsg_id: str,
    bearer_token: str,
    token_expiry: int,
) -> None:
    """Persist a manually-minted SESSION token to auth.json — non-destructively.

    Persists an ephemeral, already-minted bearer token (as opposed to a stored
    client secret).  The ephemeral bearer token (like
    ``token_expiry``) is session state, so it is written to auth.json regardless
    of the storage mode and read back by ``load_config``'s auth.json fallback.

    This deliberately does NOT: change the storage mode, touch the OS keychain,
    write or delete any stored client secret / SSH settings, or affect any other
    profile.  The password (client secret) is never captured here.
    """
    with _CONFIG_WRITE_LOCK:
        auth_raw = _read_auth_file()
        profiles = auth_raw.get("profiles")
        if not isinstance(profiles, dict):
            profiles = {}
        entry = profiles.get(profile)
        if not isinstance(entry, dict):
            entry = {}
        scm = entry.get("scm")
        if not isinstance(scm, dict):
            scm = {}
        scm["client_id"] = client_id
        scm["tsg_id"] = tsg_id
        scm["bearer_token"] = bearer_token
        if token_expiry:
            scm["token_expiry"] = int(token_expiry)
        else:
            scm.pop("token_expiry", None)
        scm.pop("client_secret", None)  # the password is never persisted
        entry["scm"] = scm
        profiles[profile] = entry
        auth_raw["profiles"] = profiles
        _write_auth_file(auth_raw)

        # Record active profile + preferred method (non-secret); leave the
        # storage mode and every other config.json section untouched.
        raw = _read_config_file()
        auth_section = raw.get("auth")
        if not isinstance(auth_section, dict):
            auth_section = {}
        auth_section["preferred_method"] = "bearer"
        auth_section.setdefault("active_profile", profile)
        raw["auth"] = auth_section
        raw.pop("active_profile", None)  # drop any legacy top-level key
        _write_config_file(raw)


def delete_profile(name: str) -> None:
    """Remove a named profile from config.json and its keychain entries.

    Raises ``ValueError`` when attempting to delete the ``default`` profile
    or a profile that does not exist.
    """
    if name == _DEFAULT_PROFILE:
        raise ValueError("Cannot delete the 'default' profile.")

    with _CONFIG_WRITE_LOCK:
        raw = _read_config_file()
        auth_raw = _read_auth_file()
        cprofs = raw.get("profiles", {}) if isinstance(raw.get("profiles"), dict) else {}
        aprofs = auth_raw.get("profiles", {}) if isinstance(auth_raw.get("profiles"), dict) else {}
        if name not in cprofs and name not in aprofs:
            raise ValueError(f"Profile '{name}' does not exist.")
        cprofs.pop(name, None)
        aprofs.pop(name, None)
        raw["profiles"] = cprofs
        auth_raw["profiles"] = aprofs
        # If the deleted profile was active, fall back to default.
        if _active_profile_name(raw) == name:
            auth_section = raw.get("auth")
            if not isinstance(auth_section, dict):
                auth_section = {}
            auth_section["active_profile"] = _DEFAULT_PROFILE
            raw["auth"] = auth_section
            raw.pop("active_profile", None)
        _write_config_file(raw)
        _write_auth_file(auth_raw)

    # Remove profile-scoped keychain entries (new and legacy key names).
    for base in (_KEY_SCM_BEARER, _KEY_SCM_SECRET, _KEY_SSH_USER, _KEY_SSH_PASSWORD):
        _keychain_delete(_profile_key(base, name))
    # Also clear any legacy-format keys for this profile.
    for base in (_LEGACY_KEY_SCM_BEARER, _LEGACY_KEY_SCM_SECRET, _LEGACY_KEY_SSH_PASSWORD):
        _keychain_delete(_profile_key(base, name))


def clear_keychain(profile: str | None = None) -> None:
    """Remove ARC secrets from the OS keychain.

    When *profile* is supplied only that profile's secrets are removed.
    When *profile* is None all known profile secrets are removed, including
    legacy keys from older ARC versions.

    Called by ``arc auth clear``.  Does not touch the config file.

    Clears both current key names (arc.bearer.token etc.) and legacy names
    (scm.bearer_token etc.) so the keychain is fully cleaned either way.
    """
    _ALL_CURRENT_KEYS = (_KEY_SCM_BEARER, _KEY_SCM_SECRET, _KEY_SSH_USER, _KEY_SSH_PASSWORD)
    _ALL_LEGACY_KEYS  = (_LEGACY_KEY_SCM_BEARER, _LEGACY_KEY_SCM_SECRET, _LEGACY_KEY_SSH_PASSWORD)

    if profile:
        for base in _ALL_CURRENT_KEYS:
            _keychain_delete(_profile_key(base, profile))
        if profile == _DEFAULT_PROFILE:
            for key in _ALL_LEGACY_KEYS:
                _keychain_delete(key)
    else:
        # Clear legacy keys (default profile, pre-rename format).
        for key in _ALL_LEGACY_KEYS:
            _keychain_delete(key)
        # Clear all profile-scoped current keys.
        for p in list_profiles():
            pname = p["name"]
            for base in _ALL_CURRENT_KEYS:
                _keychain_delete(_profile_key(base, pname))
