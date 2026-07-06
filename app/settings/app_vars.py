"""Application variable loader and template resolver.

``settings/app-variables.json`` stores static variables and metadata about
dynamic ones. Both are merged at runtime into a flat ``{name: value}`` dict
and substituted into any text using ``{{variable_name}}`` syntax.

Use this for:
  - ``settings/banner.txt``   — show version, tagline, etc. on startup
  - ``settings/goodbye.txt``  — personalised exit messages
  - Any future settings file that needs live application values

Dynamic variables (always resolved fresh):
  {{app_version}}      — current version (app/__init__.py)
  {{docs_date}}        — last docsupdate date (docs/scm-api/MANIFEST.md)
  {{python_version}}   — Python runtime version
  {{platform}}         — OS name + release

Static variables (from settings/app-variables.json, keys without _ prefix):
  {{app_name}}         — "ARC"
  {{app_full_name}}    — "Assisted Remote Console"
  {{app_description}}  — short description
  {{app_company}}      — "Palo Alto Networks"
  {{app_tagline}}      — subtitle line
  {{app_url}}          — repository URL
  {{app_support}}      — support / help hint

Adding a new variable:
  1. Add it to settings/app-variables.json (no _ prefix).
  2. Reference it anywhere with {{my_variable}}.
  No code change needed for purely static values.
  For dynamic values, add resolution logic to _dynamic_vars() below.
"""
from __future__ import annotations

import json
import logging
import platform
import re
import sys
from typing import Optional

logger = logging.getLogger(__name__)

# Cache so repeated calls (e.g. banner + goodbye in one session) don't reread files.
_vars_cache: Optional[dict[str, str]] = None


def _dynamic_vars() -> dict[str, str]:
    """Resolve dynamic variables that change at runtime."""
    from app import __version__
    from app.paths import REPO_ROOT

    dyn: dict[str, str] = {
        "app_version":    __version__,
        "python_version": sys.version.split()[0],
        "platform":       f"{platform.system()} {platform.release()}",
        "docs_date":      "unknown",
    }

    # Last docsupdate date from MANIFEST.md
    manifest = REPO_ROOT / "docs" / "scm-api" / "MANIFEST.md"
    if manifest.exists():
        try:
            txt = manifest.read_text(encoding="utf-8")
            m = re.search(r"Pulled on (\d{4}-\d{2}-\d{2})", txt)
            if m:
                dyn["docs_date"] = m.group(1)
        except Exception:
            pass

    return dyn


def load_app_vars() -> dict[str, str]:
    """Return merged ``{name: value}`` for all application variables.

    Priority: dynamic (always wins) > settings/app-variables.json > empty string.
    Values are always strings. Keys starting with ``_`` are skipped (comments).
    Result is cached per-session; call ``invalidate_cache()`` to force reload.
    """
    global _vars_cache
    if _vars_cache is not None:
        return _vars_cache

    from app.paths import APP_VARIABLES_JSON
    static: dict[str, str] = {}
    if APP_VARIABLES_JSON.exists():
        try:
            raw = json.loads(APP_VARIABLES_JSON.read_text(encoding="utf-8"))
            static = {
                k: str(v)
                for k, v in raw.items()
                if not k.startswith("_") and isinstance(v, (str, int, float, bool))
            }
        except (json.JSONDecodeError, OSError) as exc:
            logger.warning("app-variables.json parse error: %s", exc)

    merged = {**static, **_dynamic_vars()}  # dynamic wins
    _vars_cache = merged
    return merged


def resolve(text: str) -> str:
    """Replace ``{{variable_name}}`` placeholders in *text* with their values.

    Unknown variables are left as-is so typos don't break banners silently.
    """
    if "{{" not in text:
        return text
    variables = load_app_vars()

    def _replace(m: re.Match) -> str:
        key = m.group(1).strip()
        return variables.get(key, m.group(0))  # leave unknown as-is

    return re.sub(r"\{\{(\w+)\}\}", _replace, text)


def invalidate_cache() -> None:
    """Force a re-read on next access."""
    global _vars_cache
    _vars_cache = None
