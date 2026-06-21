---
command: "set sase authentication-settings move"
description: "Move a GlobalProtect authentication setting"
usage: "set sase authentication-settings move name <value> json|file <payload-or-path>"
feature_flag: create_sase_authentication_settings_move
category: sase
scope: global
api: "POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/authentication-settings/{name}:move"
---

# set sase authentication-settings move
