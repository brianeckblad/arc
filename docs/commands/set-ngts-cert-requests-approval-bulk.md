---
command: "set ngts cert-requests approval bulk"
description: "Approve or reject multiple pending approval"
usage: "set ngts cert-requests approval bulk decision <value> json|file <payload-or-path>"
feature_flag: create_ngts_cert_requests_approval_bulk
category: ngts
scope: global
api: "POST https://api.strata.paloaltonetworks.com/ngts/v1/certificaterequests/approval/bulk/{decision}"
---

# set ngts cert-requests approval bulk
