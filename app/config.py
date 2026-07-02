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
from dataclasses import dataclass, field
from pathlib import Path

import keyring
import keyring.errors

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Config path — <project_root>/config/<os_username>/config.json
# ---------------------------------------------------------------------------

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_OS_USERNAME  = _getpass.getuser()

CONFIG_DIR  = _PROJECT_ROOT / "config" / _OS_USERNAME
CONFIG_FILE = CONFIG_DIR / "config.json"

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
class ArcConfig:
    scm: SCMConfig = field(default_factory=SCMConfig)
    ssh: SSHConfig = field(default_factory=SSHConfig)
    debug: bool = False
    default_folder: str = "Shared"
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
    """Atomically write *raw* to CONFIG_FILE with mode 0600."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_DIR.chmod(stat.S_IRWXU)
    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
    fd = os.open(CONFIG_FILE, flags, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as handle:
        json.dump(raw, handle, indent=2)
        handle.write("\n")
    CONFIG_FILE.chmod(stat.S_IRUSR | stat.S_IWUSR)


def _to_new_format(raw: dict) -> dict:
    """Migrate a legacy single-profile config dict to the multi-profile format.

    The original top-level ``scm`` / ``ssh`` / ``default_folder`` keys become
    the ``default`` profile.  The original dict is not mutated.
    """
    if "profiles" in raw:
        return raw  # already in new format

    legacy_scm = {
        k: v for k, v in raw.get("scm", {}).items()
        if not k.startswith("_") and k not in ("bearer_token", "client_secret")
    }
    legacy_ssh = {
        k: v for k, v in raw.get("ssh", {}).items()
        if not k.startswith("_") and k != "password"
    }
    return {
        "active_profile": raw.get("active_profile", _DEFAULT_PROFILE),
        "profiles": {
            _DEFAULT_PROFILE: {
                "scm": legacy_scm,
                "ssh": legacy_ssh,
                "default_folder": raw.get("default_folder", "Shared"),
            }
        },
    }


# ---------------------------------------------------------------------------
# Profile management
# ---------------------------------------------------------------------------

def list_profiles() -> list[dict]:
    """Return metadata for every configured profile.

    Each entry is a dict with keys: ``name``, ``client_id``, ``tsg_id``,
    ``default_folder``, ``active`` (bool).

    When no config file exists, returns a single placeholder for ``default``.
    """
    raw = _read_config_file()
    active = raw.get("active_profile", _DEFAULT_PROFILE)

    if "profiles" in raw:
        result: list[dict] = []
        for name, pdata in raw["profiles"].items():
            scm_block = pdata.get("scm", {}) if isinstance(pdata, dict) else {}
            result.append({
                "name":           name,
                "client_id":      scm_block.get("client_id", ""),
                "tsg_id":         scm_block.get("tsg_id", ""),
                "default_folder": pdata.get("default_folder", "Shared") if isinstance(pdata, dict) else "Shared",
                "active":         name == active,
            })
        return result

    # Legacy single-profile format.
    scm_block = raw.get("scm", {})
    return [{
        "name":           _DEFAULT_PROFILE,
        "client_id":      scm_block.get("client_id", ""),
        "tsg_id":         scm_block.get("tsg_id", ""),
        "default_folder": raw.get("default_folder", "Shared"),
        "active":         True,
    }]


def get_active_profile() -> str:
    """Return the name of the currently active profile (default: ``"default"``)."""
    return _read_config_file().get("active_profile", _DEFAULT_PROFILE)


def set_active_profile(name: str) -> None:
    """Persist *name* as the active profile without touching credential data.

    Migrates a legacy config to the multi-profile format on first call if
    the config file has not been migrated yet.
    """
    raw = _to_new_format(_read_config_file())
    raw["active_profile"] = name
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
    raw = _read_config_file()

    # Determine which profile data block to load.
    if "profiles" in raw:
        active = raw.get("active_profile", _DEFAULT_PROFILE)
        target = profile or active
        pdata = raw["profiles"].get(target)
        if pdata is None:
            # Requested profile does not exist — fall back to active profile.
            logger.debug("Profile '%s' not found; falling back to '%s'", target, active)
            target = active
            pdata = raw["profiles"].get(target, {})
        scm_raw = pdata.get("scm", {}) if isinstance(pdata, dict) else {}
        ssh_raw = pdata.get("ssh", {}) if isinstance(pdata, dict) else {}
        cfg.default_folder = pdata.get("default_folder", "Shared") if isinstance(pdata, dict) else "Shared"
    else:
        # Legacy single-profile format.
        target  = _DEFAULT_PROFILE
        scm_raw = raw.get("scm", {})
        ssh_raw = raw.get("ssh", {})
        cfg.default_folder = raw.get("default_folder", "Shared")

    cfg.profile_name = target

    # --- Secrets from keychain (profile-scoped new key names) ---
    bearer_key   = _profile_key(_KEY_SCM_BEARER,   target)
    secret_key   = _profile_key(_KEY_SCM_SECRET,   target)
    ssh_user_key = _profile_key(_KEY_SSH_USER,     target)
    ssh_pass_key = _profile_key(_KEY_SSH_PASSWORD, target)

    cfg.scm.bearer_token  = _keychain_get(bearer_key)
    cfg.scm.client_secret = _keychain_get(secret_key)
    cfg.ssh.user_from_keychain = _keychain_get(ssh_user_key)  # may be empty
    cfg.ssh.password      = _keychain_get(ssh_pass_key)

    # --- Legacy key migration (read old keys when new keys are empty) ---
    # This lets users who configured ARC before the rename keep working.
    # The next save_config() call will write the new keys and clear the old ones.
    if target == _DEFAULT_PROFILE:
        if not cfg.scm.bearer_token:
            cfg.scm.bearer_token  = _keychain_get(_LEGACY_KEY_SCM_BEARER)
        if not cfg.scm.client_secret:
            cfg.scm.client_secret = _keychain_get(_LEGACY_KEY_SCM_SECRET)
        if not cfg.ssh.password:
            cfg.ssh.password      = _keychain_get(_LEGACY_KEY_SSH_PASSWORD)

    # Legacy profile-scoped keys (old format used suffixed variants of old names)
    if not cfg.scm.bearer_token:
        cfg.scm.bearer_token  = _keychain_get(_profile_key(_LEGACY_KEY_SCM_BEARER,   target))
    if not cfg.scm.client_secret:
        cfg.scm.client_secret = _keychain_get(_profile_key(_LEGACY_KEY_SCM_SECRET,   target))
    if not cfg.ssh.password:
        cfg.ssh.password      = _keychain_get(_profile_key(_LEGACY_KEY_SSH_PASSWORD, target))

    # --- Non-sensitive fields from config file ---
    cfg.scm.client_id = scm_raw.get("client_id", "")
    cfg.scm.tsg_id    = scm_raw.get("tsg_id", "")

    # Legacy plaintext secrets: used only when keychain returned nothing.
    # Stripped from disk on the next save_config() call.
    if not cfg.scm.bearer_token:
        cfg.scm.bearer_token  = scm_raw.get("bearer_token", "")
    if not cfg.scm.client_secret:
        cfg.scm.client_secret = scm_raw.get("client_secret", "")

    # SSH fields — keychain takes priority over config.json for username.
    # cfg.ssh.user_from_keychain was set above from the keychain.
    # Fall back to config.json "username" / legacy "user" key.
    cfg.ssh.user = (
        cfg.ssh.user_from_keychain
        or ssh_raw.get("username", ssh_raw.get("user", "admin"))
    )
    cfg.ssh.key_path = ssh_raw.get("key_path", "")
    cfg.ssh.port     = int(ssh_raw.get("port", 22))
    if not cfg.ssh.password:
        cfg.ssh.password = ssh_raw.get("password", "")

    # --- Environment variables always win ---
    cfg.scm.bearer_token  = os.environ.get("SCM_BEARER_TOKEN",  cfg.scm.bearer_token)
    cfg.scm.client_id     = os.environ.get("SCM_CLIENT_ID",     cfg.scm.client_id)
    cfg.scm.client_secret = os.environ.get("SCM_CLIENT_SECRET", cfg.scm.client_secret)
    cfg.scm.tsg_id        = os.environ.get("SCM_TSG_ID",        cfg.scm.tsg_id)
    cfg.ssh.user          = os.environ.get("ARC_SSH_USER",       cfg.ssh.user)
    cfg.ssh.key_path      = os.environ.get("ARC_SSH_KEY",        cfg.ssh.key_path)
    cfg.ssh.password      = os.environ.get("ARC_SSH_PASS",       cfg.ssh.password)
    cfg.debug             = os.environ.get("ARC_DEBUG", "0") == "1"

    return cfg


def save_config(cfg: ArcConfig, profile: str | None = None) -> None:
    """Persist config: secrets to OS keychain, non-sensitive values to config.json.

    *profile* overrides ``cfg.profile_name`` when supplied.  Defaults to
    ``cfg.profile_name`` (set by ``load_config``), which falls back to
    ``"default"`` if not set.

    The config file is always written in the multi-profile format.  A legacy
    single-profile file is migrated on the first save_config() call.

    Secrets are never written to disk.  If the OS keychain cannot store a
    non-empty secret, non-sensitive config is still saved and
    ``ConfigSecurityError`` is raised.
    """
    target = profile or cfg.profile_name or _DEFAULT_PROFILE

    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_DIR.chmod(stat.S_IRWXU)

    # Store secrets in the keychain under the new profile-scoped key names.
    # arc.bearer.token / arc.bearer.password / arc.shell.username / arc.shell.password
    failed_secret_keys: list[str] = []
    for key, value in (
        (_profile_key(_KEY_SCM_BEARER,   target), cfg.scm.bearer_token),
        (_profile_key(_KEY_SCM_SECRET,   target), cfg.scm.client_secret),
        (_profile_key(_KEY_SSH_USER,     target), cfg.ssh.user),
        (_profile_key(_KEY_SSH_PASSWORD, target), cfg.ssh.password),
    ):
        saved = _keychain_set(key, value)
        if value and not saved:
            failed_secret_keys.append(key)

    # Migrate: clear legacy key names so they don't linger in the keychain.
    # Only clear legacy keys for the default profile (they were only ever
    # written for the default profile under the old scheme).
    if target == _DEFAULT_PROFILE:
        for legacy_key in (_LEGACY_KEY_SCM_BEARER, _LEGACY_KEY_SCM_SECRET, _LEGACY_KEY_SSH_PASSWORD):
            _keychain_delete(legacy_key)

    # Build the on-disk profile block.
    # Secrets (bearer_token, client_secret, password) are in keychain — not on disk.
    # SSH user is now also in keychain, but we keep a copy in config.json as fallback
    # for systems without a keychain (headless/CI) and for readability.
    profile_data: dict = {
        "scm": {
            "client_id": cfg.scm.client_id,
            "tsg_id":    cfg.scm.tsg_id,
        },
        "ssh": {
            "username": cfg.ssh.user,   # kept for headless fallback; keychain is primary
            "key_path": cfg.ssh.key_path,
            "port":     cfg.ssh.port,
        },
        "default_folder": cfg.default_folder,
    }

    # Read existing config (to preserve other profiles), migrate if needed.
    raw = _to_new_format(_read_config_file())
    raw.setdefault("active_profile", target)
    raw.setdefault("profiles", {})
    raw["profiles"][target] = profile_data

    _write_config_file(raw)

    if failed_secret_keys:
        failed = ", ".join(failed_secret_keys)
        raise ConfigSecurityError(
            f"OS keychain could not store ARC secret(s): {failed}. "
            "Secrets were not written to config.json. "
            "Use `arc auth configure` on a machine with keychain access, or provide "
            "secrets through environment variables for this session."
        )


def delete_profile(name: str) -> None:
    """Remove a named profile from config.json and its keychain entries.

    Raises ``ValueError`` when attempting to delete the ``default`` profile
    or a profile that does not exist.
    """
    if name == _DEFAULT_PROFILE:
        raise ValueError("Cannot delete the 'default' profile.")

    raw = _to_new_format(_read_config_file())
    if name not in raw.get("profiles", {}):
        raise ValueError(f"Profile '{name}' does not exist.")

    del raw["profiles"][name]

    # If the deleted profile was active, fall back to default.
    if raw.get("active_profile") == name:
        raw["active_profile"] = _DEFAULT_PROFILE

    _write_config_file(raw)

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
