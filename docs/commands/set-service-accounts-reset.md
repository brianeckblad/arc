---
command: "set service-accounts reset"
description: "Reset a service account"
usage: "set service-accounts reset id <value> json|file <payload-or-path>"
feature_flag: create_service_accounts_reset
category: iam
scope: global
api: "POST https://api.sase.paloaltonetworks.com/iam/v1/service_accounts/{id}/operations/reset"
---

# set service-accounts reset
