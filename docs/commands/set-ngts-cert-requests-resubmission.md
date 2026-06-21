---
command: "set ngts cert-requests resubmission"
description: "Resubmit a certificate request"
usage: "set ngts cert-requests resubmission id <value> json|file <payload-or-path>"
feature_flag: create_ngts_cert_requests_resubmission
category: ngts
scope: global
api: "POST https://api.strata.paloaltonetworks.com/outagedetection/v1/certificaterequests/{id}/resubmission"
---

# set ngts cert-requests resubmission
