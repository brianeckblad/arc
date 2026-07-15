"""Human-readable names for the ARC feature editor — shared by GUI and CLI.

Feature flags and command categories carry terse, API-derived keys
(``adnsr_conn_sources_read``, ``cloudngfw``).  This module turns them into
natural language so a human who doesn't know the API can understand the editor:

    area_label("adnsr")            -> "Advanced DNS Security"
    flag_label("adnsr_conn_sources_read", flag_cmds)
        -> {"title": "Connection Sources", "subtitle": "List Connection Sources",
            "action": "read"}

The label maps live in ``settings/feature-labels.json`` (user-editable, and
auto-augmented edit-safe by ``generate_feature_flags.py``).  Flag titles are
derived at runtime from the *descriptions* of the commands each flag gates —
those descriptions are already human-readable, so no extra data is stored.

Both the CLI (``feature show`` / ``feature info`` / ``feature area``) and the
browser editor import from here, so the two always show identical names.
"""

from __future__ import annotations

import json
import logging

from app.paths import FEATURE_LABELS_JSON

logger = logging.getLogger(__name__)

# Action a flag represents, inferred from its name suffix or gated verbs.
_READ_HINTS = ("read", "show", "list", "get")
_WRITE_HINTS = ("write", "create", "set", "update", "delete", "edit")


def _titlecase(key: str) -> str:
    """Fallback human label for an unmapped key (e.g. "device-onboarding")."""
    return key.replace("-", " ").replace("_", " ").strip().title()


def load_labels() -> dict:
    """Load settings/feature-labels.json -> {"areas": {...}, "acronyms": {...}}.

    Returns empty maps if the file is missing or malformed (callers fall back
    to title-casing), so the editor never hard-fails on a bad labels file.
    """
    try:
        raw = json.loads(FEATURE_LABELS_JSON.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        logger.debug("feature-labels.json unavailable: %s", exc)
        return {"areas": {}, "acronyms": {}}
    if not isinstance(raw, dict):
        return {"areas": {}, "acronyms": {}}
    areas = raw.get("areas") if isinstance(raw.get("areas"), dict) else {}
    acronyms = raw.get("acronyms") if isinstance(raw.get("acronyms"), dict) else {}
    return {"areas": areas, "acronyms": acronyms}


def area_label(category: str, labels: dict | None = None) -> str:
    """Human name for a command category / area key.  Title-case fallback."""
    labels = labels or load_labels()
    return labels["areas"].get(category) or _titlecase(category)


def file_label(stem: str, labels: dict | None = None) -> str:
    """Human name for a settings/features file stem (e.g. scm-cloudngfw-objects).

    Strips the ``scm-`` prefix and expands each hyphen-separated part via the
    acronym/area maps, joining multi-part names with " · " so files read as
    "Cloud NGFW · Objects" rather than "Cloudngfw Objects".
    """
    labels = labels or load_labels()
    special = {
        "panos-ops": "PAN-OS Operations",
        "panos-config": "PAN-OS Config (break-glass)",
        "curated": "Curated",
        "local": "Local overrides",
    }
    if stem in special:
        return special[stem]
    body = stem[4:] if stem.startswith("scm-") else stem
    acronyms = labels.get("acronyms", {})
    areas = labels.get("areas", {})
    parts = []
    for token in body.split("-"):
        low = token.lower()
        parts.append(acronyms.get(low) or areas.get(low) or _titlecase(token))
    return " · ".join(parts)


def _flag_action(flag: str, gated: list[str]) -> str:
    """Classify a flag as 'read', 'write', or '' (mixed/unknown)."""
    low = flag.lower()
    for hint in _WRITE_HINTS:
        if low.endswith("_" + hint) or low.endswith(hint):
            return "write"
    for hint in _READ_HINTS:
        if low.endswith("_" + hint) or low.endswith(hint):
            return "read"
    # Fall back to the verbs of the gated commands.
    verbs = {c.split()[0] for c in gated if c}
    if verbs and verbs <= {"show"}:
        return "read"
    if verbs and verbs <= {"set", "create", "update", "delete"}:
        return "write"
    return ""


def _primary_command(gated: list[str]) -> str | None:
    """Pick the most representative command for a flag (prefer the base 'show').

    The base command (fewest tokens, 'show' verb preferred) usually carries the
    clearest description, e.g. 'show adnsr conn-sources' -> "List Connection
    Sources" rather than the '... id' variant "Get a Connection Source".
    """
    if not gated:
        return None
    shows = [c for c in gated if c.startswith("show ")]
    pool = shows or gated
    return min(pool, key=lambda c: (len(c.split()), len(c)))


def flag_label(flag: str, flag_cmds: dict[str, list[str]], *,
               commands=None, labels: dict | None = None) -> dict:
    """Return a natural-language label for a feature flag.

    ``flag_cmds``  — {flag -> [command_key, ...]} reverse map.
    ``commands``   — the COMMANDS registry (defaults to app.commands.registry).

    Result: ``{"title": str, "subtitle": str, "action": "read"|"write"|""}``.
    The *title* is a short resource name; the *subtitle* is the primary gated
    command's description (already human-readable).
    """
    if commands is None:
        from app.commands.registry import COMMANDS as commands
    labels = labels or load_labels()

    gated = flag_cmds.get(flag, [])
    action = _flag_action(flag, gated)
    primary = _primary_command(gated)

    if primary and primary in commands:
        desc = (commands[primary].description or "").strip()
    else:
        desc = ""

    # Title: derive a resource name.  Prefer the last segment of the primary
    # command (the resource), expanded via acronyms and title-cased.
    if primary:
        resource = primary.split()[-1] if len(primary.split()) > 1 else primary
        title = _expand(resource, labels)
    else:
        # No gated command — de-slug the flag, dropping the action suffix.
        stem = flag
        for hint in _WRITE_HINTS + _READ_HINTS:
            if stem.lower().endswith("_" + hint):
                stem = stem[: -(len(hint) + 1)]
                break
        title = _expand(stem, labels)

    return {"title": title, "subtitle": desc, "action": action}


def _expand(token: str, labels: dict) -> str:
    """Expand acronyms within a hyphen/underscore token and title-case it."""
    acronyms = labels.get("acronyms", {})
    parts = token.replace("-", " ").replace("_", " ").split()
    out = []
    for p in parts:
        low = p.lower()
        out.append(acronyms.get(low, p[:1].upper() + p[1:] if p else p))
    return " ".join(out).strip() or _titlecase(token)
