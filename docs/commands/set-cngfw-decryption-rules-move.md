---
command: "set cngfw decryption-rules move"
description: "Move a decryption rule"
usage: "set cngfw decryption-rules move id <value> json|file <payload-or-path>"
feature_flag: create_cngfw_decryption_rules_move
category: cloudngfw
scope: global
api: "POST https://api.strata.paloaltonetworks.com/config/security/v1/decryption-rules/{id}:move"
---

# set cngfw decryption-rules move
