# set address-group

Create an address group in the active SCM folder.

**Source:** `POST /config/objects/v1/address-groups`  
**Schema:** address-groups (see `docs/scm-api/specs/ngfw-objects.yaml`)  
**Feature flag:** `create_address_group`

---

## Group type variants (oneOf — exactly one required)

The `address-groups` schema uses a `oneOf` to require either `static` or `dynamic`.

### static — Explicit member list

```text
set address-group <name> static <member1> [<member2> ...]
```

| Field | Type | Description |
|---|---|---|
| `static` | list of strings | Address object names that are members of this group |

Members must be existing address object names in the same folder (or inherited from parent folders/snippets).

```text
set address-group WebTier    static web1 web2 web3
set address-group DBServers  static mysql-primary mysql-replica
set address-group AllHosts   static 10.1.0.0-subnet 10.2.0.0-subnet  description "All internal"
```

---

### dynamic — Tag-based filter (evaluated at policy match time)

```text
set address-group <name> dynamic filter '<expression>'
```

| Field | Type | Description |
|---|---|---|
| `dynamic.filter` | string | Tag expression evaluated at runtime |

Filter expression syntax:

| Operator | Syntax | Meaning |
|---|---|---|
| AND | `'TagA and TagB'` | Object must have BOTH tags |
| OR | `'TagA or TagB'` | Object must have EITHER tag |
| NOT | `'TagA and not TagB'` | Has TagA but not TagB |
| Single | `'Production'` | Has the Production tag |

Tag values auto-update as objects are tagged/untagged — no policy recompile needed.

```text
set address-group ProdHosts    dynamic filter 'Production'
set address-group HighRisk     dynamic filter 'External and Critical'
set address-group AllEnvs      dynamic filter 'Production or Staging or Dev'
set address-group ProdNotDMZ   dynamic filter 'Production and not DMZ'
```

---

## Optional fields (apply to both group types)

| Field | Type | Description |
|---|---|---|
| `description` | string | Human-readable description |
| `tag` | list of strings | Tags to apply to the group itself |

---

## Full syntax

```text
set address-group <name> static  <member1> [member2 ...]   [description <text>] [tag <name>]
set address-group <name> dynamic filter '<expression>'      [description <text>] [tag <name>]
```

---

## Related commands

- `show address-group` — list address groups
- `delete address-group <name>` — remove an address group
- `show address` — list individual address objects
- `show tag` — list tags (used in dynamic filter expressions)
