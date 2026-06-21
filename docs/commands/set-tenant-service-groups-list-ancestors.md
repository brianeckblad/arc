---
command: "set tenant-service-groups list-ancestors"
description: "List tenant service group ancestors"
usage: "set tenant-service-groups list-ancestors tsg_id <value> json|file <payload-or-path>"
feature_flag: create_tenant_service_groups_list_ancestors
category: tenancy
scope: global
api: "POST https://api.sase.paloaltonetworks.com/tenancy/v1/tenant_service_groups/{tsg_id}/operations/list_ancestors"
---

# set tenant-service-groups list-ancestors
