"""ARC feature flags — JSON-driven command switches with a development tier.

The source of truth is ``settings/features.json``.  Each key is a flag name,
each value is one of three states:

    true   → ON   — command is visible and runnable for everyone
    "dev"  → DEV  — command is under development: hidden for normal users,
                    revealed only when development mode is active
    false  → OFF  — command is hidden and blocked for everyone

Keys starting with ``_`` are comments and ignored.

Development mode lets a team ship work-in-progress commands behind the hidden
``dev`` shell command (or the ``ARC_DEV_MODE`` env var for CI/CD) without
confusing normal users — a ``"dev"`` command only appears once development mode
is switched on.

Precedence (last wins):
  1. settings/features.json
  2. ARC_FEATURE_<NAME>=on|off|dev  environment variable (CI / one-shot)

When a flag is hidden (OFF, or DEV outside development mode):
  - The command is hidden from ? help output
  - Running it prints how to enable it (and mentions ``dev`` for DEV flags)
  - The CommandDef still exists in the registry (so smoke tests can see it)

Adding a new feature:
  1. Set ``feature_flag='your_flag'`` on the CommandDef (app/commands/*.py)
  2. Add ``"your_flag": "dev"`` to settings/features.json while building it
  3. Flip to ``true`` in settings/features.json when ready to ship

Inside ARC:
  feature show              list every flag and its on/dev/off state
  feature enable <flag>     turn one ON for this session
  feature disable <flag>    turn one OFF for this session
  feature dev <flag>        mark one as DEV for this session
  dev                       toggle development mode (reveals DEV commands)
"""

from __future__ import annotations

import json
import logging
import os

from app.paths import FEATURES_FILE

logger = logging.getLogger(__name__)

# The three states a flag can hold.  These strings are used everywhere a flag's
# state is compared or displayed, so keep them stable.
STATE_ON = "on"
STATE_DEV = "dev"
STATE_OFF = "off"

# A loaded feature set maps flag-name → state ("on" | "dev" | "off").
FeatureMap = dict[str, str]

_ENV_PREFIX = "ARC_FEATURE_"

# Synonyms accepted in features.json values and ARC_FEATURE_* env vars.
_ON_WORDS = {"on", "true", "1", "yes", "enabled"}
_DEV_WORDS = {"dev", "development", "beta", "wip"}


def _coerce_state(value: object) -> str:
    """Normalize a raw features.json value into "on" | "dev" | "off".

    Accepts booleans (``true``/``false``) and strings (``"dev"``, ``"on"`` …).
    Anything unrecognized is treated as OFF — the safe default.
    """
    if isinstance(value, bool):
        return STATE_ON if value else STATE_OFF
    token = str(value).strip().lower()
    if token in _DEV_WORDS:
        return STATE_DEV
    if token in _ON_WORDS:
        return STATE_ON
    return STATE_OFF


def load_features() -> FeatureMap:
    """Read settings/features.json, then apply ARC_FEATURE_<NAME> env overrides.

    Returns a plain dict of flag_name → state string.  Comment keys (leading
    ``_``) are skipped.  Missing file → empty map (every flag then defaults off).
    """
    flags: FeatureMap = {}

    if FEATURES_FILE.exists():
        try:
            raw = json.loads(FEATURES_FILE.read_text(encoding="utf-8"))
            for key, val in raw.items():
                if key.startswith("_"):  # _README / _section_* comments
                    continue
                flags[key] = _coerce_state(val)
        except (json.JSONDecodeError, OSError) as exc:
            logger.warning("Could not read %s: %s", FEATURES_FILE, exc)

    # Environment overrides: ARC_FEATURE_SHOW_ADDRESS=on|dev|off.
    for env_key, env_val in os.environ.items():
        if env_key.startswith(_ENV_PREFIX):
            name = env_key[len(_ENV_PREFIX):].lower()
            flags[name] = _coerce_state(env_val)

    return flags


def feature_state(flags: FeatureMap, flag_name: str) -> str:
    """Return the raw state of *flag_name* — "on", "dev", or "off".

    An empty *flag_name* (the default on a CommandDef) is always "on" — commands
    without a flag are never gated.  A flag absent from the map is "off".
    """
    if not flag_name:
        return STATE_ON
    return flags.get(flag_name, STATE_OFF)


def is_enabled(flags: FeatureMap, flag_name: str, dev_mode: bool = False) -> bool:
    """Return True when *flag_name* is usable in the current mode.

    * ON   flags are always usable.
    * DEV  flags are usable only when *dev_mode* is True.
    * OFF  flags are never usable.

    An empty *flag_name* always returns True (ungated command).
    """
    state = feature_state(flags, flag_name)
    if state == STATE_ON:
        return True
    if state == STATE_DEV:
        return dev_mode
    return False


def dev_mode_from_env() -> bool:
    """Return True when ARC_DEV_MODE is set to a truthy value (CI/CD hook)."""
    return os.environ.get("ARC_DEV_MODE", "").strip().lower() in _ON_WORDS

