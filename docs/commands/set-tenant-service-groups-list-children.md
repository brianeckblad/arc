---
command: "set tenant-service-groups list-children"
description: "List tenant service group children"
usage: "set tenant-service-groups list-children tsg_id <value> json|file <payload-or-path>"
feature_flag: create_tenant_service_groups_list_children
category: tenancy
scope: global
api: "POST https://api.sase.paloaltonetworks.com/tenancy/v1/tenant_service_groups/{tsg_id}/operations/list_children"
---

# set tenant-service-groups list-children
