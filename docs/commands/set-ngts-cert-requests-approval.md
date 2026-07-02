---
command: "set ngts cert-requests approval"
description: "Approve or reject pending certificate request"
usage: "set ngts cert-requests approval id <value> decision <value> json|file <payload-or-path>"
feature_flag: create_ngts_cert_requests_approval
category: ngts
scope: global
api: "POST https://api.strata.paloaltonetworks.com/ngts/v1/certificaterequests/{id}/approval/{decision}"
---

# set ngts cert-requests approval
