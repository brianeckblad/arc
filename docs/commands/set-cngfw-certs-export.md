---
command: "set cngfw certs export"
description: "Export a certificate"
usage: "set cngfw certs export id <value> json|file <payload-or-path>"
feature_flag: create_cngfw_certs_export
category: cloudngfw
scope: global
api: "POST https://api.strata.paloaltonetworks.com/config/identity/v1/certificates/{id}:export"
---

# set cngfw certs export
