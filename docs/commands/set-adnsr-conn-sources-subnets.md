---
command: "set adnsr conn-sources subnets"
description: "Create a Connection Source subnet"
usage: "set adnsr conn-sources subnets connection-source-id <value> json|file <payload-or-path>"
feature_flag: create_adnsr_conn_sources_subnets
category: adnsr
scope: global
api: "POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources/{connection-source-id}/subnets"
---

# set adnsr conn-sources subnets
