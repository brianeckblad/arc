---
command: "set adnsr conn-sources subnets verify"
description: "Verify a subnet for a connection source"
usage: "set adnsr conn-sources subnets verify connection-source-id <value> subnet-id <value> json|file <payload-or-path>"
feature_flag: create_adnsr_conn_sources_subnets_verify
category: adnsr
scope: global
api: "POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources/{connection-source-id}/subnets/{subnet-id}:verify-update"
---

# set adnsr conn-sources subnets verify
