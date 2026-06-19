"""ARC feature flags — JSON-driven on/off switches for commands.

The source of truth is ``settings/features.json``.  Each key is a flag name,
each value is ``true`` (command visible + runnable) or ``false`` (hidden).
Keys starting with ``_`` are comments and ignored.

Precedence (last wins):
  1. settings/features.json
  2. ARC_FEATURE_<NAME>=1/0  environment variable (CI / one-shot)

When a flag is OFF for a command:
  - The command is hidden from ? help output
  - Running it prints "Feature '<x>' is not enabled" + how to enable
  - The CommandDef still exists in the registry (so smoke tests can see it)

Adding a new feature:
  1. Set ``feature_flag='your_flag'`` on the CommandDef (app/commands/*.py)
  2. Add ``"your_flag": false`` to settings/features.json
  3. Flip to ``true`` in settings/features.json when ready to ship

Inside ARC:
  feature show              list every flag and its on/off state
  feature enable <flag>     turn one on for this session
  feature disable <flag>    turn one off for this session
"""

from __future__ import annotations

import json
import logging
import os

from app.paths import FEATURES_FILE

logger = logging.getLogger(__name__)

# A loaded feature set is just a flag-name → enabled map.
FeatureMap = dict[str, bool]

_ENV_PREFIX = "ARC_FEATURE_"


def load_features() -> FeatureMap:
    """Read settings/features.json, then apply ARC_FEATURE_<NAME> env overrides.

    Returns a plain dict of flag_name → bool.  Comment keys (leading ``_``)
    are skipped.  Missing file → empty map (every flag then defaults off).
    """
    flags: FeatureMap = {}

    if FEATURES_FILE.exists():
        try:
            raw = json.loads(FEATURES_FILE.read_text(encoding="utf-8"))
            for key, val in raw.items():
                if key.startswith("_"):  # _README / _section_* comments
                    continue
                flags[key] = bool(val)
        except (json.JSONDecodeError, OSError) as exc:
            logger.warning("Could not read %s: %s", FEATURES_FILE, exc)

    # Environment overrides: ARC_FEATURE_SHOW_ADDRESS=1 → show_address on.
    for env_key, env_val in os.environ.items():
        if env_key.startswith(_ENV_PREFIX):
            name = env_key[len(_ENV_PREFIX):].lower()
            flags[name] = env_val.strip() not in ("0", "false", "no", "")

    return flags


def is_enabled(flags: FeatureMap, flag_name: str) -> bool:
    """Return True when *flag_name* is enabled in *flags*.

    An empty *flag_name* (the default on a CommandDef) always returns True —
    commands without a flag are never gated.  A flag absent from the map
    returns False (safe default: unlisted features are off).
    """
    if not flag_name:
        return True
    return bool(flags.get(flag_name, False))

