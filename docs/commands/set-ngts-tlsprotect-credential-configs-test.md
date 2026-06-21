---
command: "set ngts tlsprotect credential-configs test"
description: "Test the connection to an external"
usage: "set ngts tlsprotect credential-configs test id <value> json|file <payload-or-path>"
feature_flag: create_ngts_credential_configs_test
category: ngts
scope: global
api: "POST https://api.strata.paloaltonetworks.com/v1/credentialmanagerconfigurations/{id}/test"
---

# set ngts tlsprotect credential-configs test
