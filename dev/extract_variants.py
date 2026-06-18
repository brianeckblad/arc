#!/usr/bin/env python3
"""Extract type variants (oneOf/anyOf) from all SCM OpenAPI specs.

Run: python dev/extract_variants.py

Shows every schema that has meaningful type variants beyond just the
container types (folder/snippet/device).  This is used to understand
which 'set' commands need subtype documentation.
"""
import glob
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

try:
    import yaml
except ImportError:
    print("PyYAML required: uv pip install pyyaml")
    sys.exit(1)

# Container/scope types that are NOT object subtypes (just deployment context)
_SKIP_TITLES = frozenset({"folder", "snippet", "device", "container_type"})


def find_type_variants(schema: dict, depth: int = 0) -> list[dict]:
    """Recursively find oneOf/anyOf type variant entries, skipping container variants."""
    if not isinstance(schema, dict) or depth > 6:
        return []
    results = []
    for key in ("oneOf", "anyOf"):
        for entry in schema.get(key, []):
            if not isinstance(entry, dict):
                continue
            title = entry.get("title", "")
            if title in _SKIP_TITLES:
                continue
            props = entry.get("properties", {})
            required = entry.get("required", [])
            if props or title:
                results.append({
                    "title": title,
                    "properties": list(props.keys()),
                    "required": required,
                    "description": entry.get("description", ""),
                    "examples": {k: v.get("example", "") for k, v in props.items() if "example" in v},
                })
            # Recurse
            nested = find_type_variants(entry, depth + 1)
            results.extend(nested)
    return results


def main() -> None:
    spec_files = sorted(glob.glob(str(ROOT / "docs/scm-api/specs/ngfw-*.yaml")))
    if not spec_files:
        print("No spec files found. Run: python dev/update_scm_docs.py")
        return

    total = 0
    for spec_file in spec_files:
        domain = Path(spec_file).stem.replace("ngfw-", "")
        with open(spec_file) as f:
            spec = yaml.safe_load(f)

        schemas = spec.get("components", {}).get("schemas", {})
        found_any = False
        for name, schema in sorted(schemas.items()):
            if not isinstance(schema, dict):
                continue
            variants = find_type_variants(schema)
            if not variants:
                continue
            if not found_any:
                print(f"\n{'='*60}")
                print(f"Domain: {domain}  ({spec_file})")
                print(f"{'='*60}")
                found_any = True
            print(f"\n  Schema: {name}")
            print(f"  {'─'*50}")
            for v in variants:
                title = v["title"] or "(unnamed)"
                req   = ", ".join(v["required"])
                desc  = v["description"]
                ex    = v["examples"]
                print(f"    Variant: {title}")
                if req:
                    print(f"      Required field(s): {req}")
                if ex:
                    for field, example in ex.items():
                        print(f"      Example: {field} = {example}")
                if desc:
                    print(f"      Description: {desc[:80]}")
            total += len(variants)

    print(f"\n\nTotal type variants found: {total}")


if __name__ == "__main__":
    main()

