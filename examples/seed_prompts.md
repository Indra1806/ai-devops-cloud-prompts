# Seed Prompts – 30 High‑Value Examples

Each example includes YAML front matter, prompt body, and validation instructions.

---

## 1. AWS – Secure Multi‑Tier VPC (Terraform)

```yaml
---
title: "Design a secure multi‑tier VPC with public and private subnets"
id: aws-vpc-multi-tier
intent: "Generate Terraform configuration for a secure AWS VPC."
difficulty: intermediate
provider: aws
tags: [networking, terraform]
variables:
  vpc_cidr:
    type: string
    example: "10.0.0.0/16"
  public_subnet_cidrs:
    type: list
    example: ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnet_cidrs:
    type: list
    example: ["10.0.10.0/24", "10.0.11.0/24"]
  region:
    type: string
    example: "us-east-1"
expected_output_schema:
  type: object
  properties:
    vpc_id: {type: string}
    public_subnet_ids: {type: array, items: {type: string}}
    private_subnet_ids: {type: array, items: {type: string}}
  required: [vpc_id, public_subnet_ids, private_subnet_ids]
sample_input:
  vpc_cidr: "10.0.0.0/16"
  public_subnet_cidrs: ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnet_cidrs: ["10.0.10.0/24", "10.0.11.0/24"]
  region: "us-east-1"
sample_output:
  vpc_id: vpc-0abcd1234
  public_subnet_ids: [subnet-1111, subnet-2222]
  private_subnet_ids: [subnet-3333, subnet-4444]
rationale: "Use for greenfield VPC designs. Pitfall: forgetting NAT Gateway for private subnets."
---
```

**Prompt**

```
[System]
You are a Terraform expert. Generate production‑ready HCL code that creates a VPC with the given CIDR, public and private subnets, Internet Gateway, NAT Gateway, and route tables. Return first a JSON object describing the resource IDs, then the Terraform code.

[User]
Create a VPC in {{region}} with CIDR {{vpc_cidr}}. Public subnets: {{public_subnet_cidrs}}. Private subnets: {{private_subnet_cidrs}}.

[Output]
First output the JSON object, then the Terraform code in a code block.
```

---

## 2. AWS – IAM Least‑Privilege for S3

```yaml
---
title: "Generate least‑privilege IAM policy for an S3 bucket"
id: aws-iam-least-privilege-s3
intent: "Create a secure IAM policy that grants minimal required permissions."
difficulty: intermediate
provider: aws
tags: [iam, security]
variables:
  bucket_name:
    type: string
    example: my-app-data
  actions:
    type: list
    example: [s3:GetObject, s3:PutObject]
expected_output_schema:
  type: object
  properties:
    policy_name: {type: string}
    policy_json: {type: object}
  required: [policy_name, policy_json]
sample_input:
  bucket_name: my-app-data
  actions: [s3:GetObject, s3:PutObject]
sample_output:
  policy_name: s3-least-privilege-my-app-data
  policy_json:
    Version: "2012-10-17"
    Statement:
      - Effect: Allow
        Action: [s3:GetObject, s3:PutObject]
        Resource: arn:aws:s3:::my-app-data/*
rationale: "Review actions carefully; granting s3:ListBucket may expose object keys."
---
```

**Prompt**

```
[System]
You are an AWS IAM specialist. Craft a policy document (JSON) that grants only the specified S3 actions on the bucket.

[User]
Bucket name: {{bucket_name}}. Allowed actions: {{actions}}.

[Output]
Return a JSON object with policy_name and policy_json. Use the principle of least privilege.
```

---

## 3. AWS – Cost Estimate for EC2 + RDS

```yaml
---
title: "Estimate monthly cost for EC2 and RDS deployment"
id: aws-cost-estimate-ec2-rds
intent: "Compute a rough AWS monthly cost estimate."
difficulty: beginner
provider: aws
tags: [finops, cost]
variables:
  instance_type:
    type: string
    example: t3.medium
  instance_count:
    type: number
    example: 2
  rds_instance_class:
    type: string
    example: db.t3.small
  storage_gb:
    type: number
    example: 100
expected_output_schema:
  type: object
  properties:
    total_monthly_usd: {type: number}
    breakdown:
      type: object
      properties:
        ec2: {type: number}
        rds: {type: number}
  required: [total_monthly_usd, breakdown]
sample_input:
  instance_type: t3.medium
  instance_count: 2
  rds_instance_class: db.t3.small
  storage_gb: 100
sample_output:
  total_monthly_usd: 85.40
  breakdown:
    ec2: 48.00
    rds: 37.40
rationale: "Ignores data transfer. Use for quick budgeting; actual prices may vary."
---
```

**Prompt**

```
[System]
Act as a FinOps analyst. Provide on‑demand monthly cost in USD (us‑east‑1).

[User]
EC2: {{instance_count}} × {{instance_type}}. RDS: {{rds_instance_class}} with {{storage_gb}} GB storage.

[Output]
JSON with total_monthly_usd and breakdown.
```

---

## 4. AWS – Terraform Module for S3 Website

```yaml
---
title: "Scaffold a Terraform module for static website hosting with S3 and CloudFront"
id: aws-tf-module-s3-website
intent: "Generate a reusable Terraform module skeleton."
difficulty: advanced
provider: aws
tags: [terraform, module]
variables:
  bucket_name:
    type: string
    example: www.example.com
  domain_name:
    type: string
    example: example.com
expected_output_schema:
  type: object
  properties:
    module_name: {type: string}
    files:
      type: object
      description: "Map of filename to HCL content"
  required: [module_name, files]
sample_input:
  bucket_name: www.example.com
  domain_name: example.com
sample_output:
  module_name: s3-static-website
  files:
    main.tf: "resource \"aws_s3_bucket\" \"site\" {...}"
    variables.tf: "variable \"bucket_name\" {...}"
    outputs.tf: "output \"website_endpoint\" {...}"
rationale: "Provides a quick start for static website modules. Pitfall: forgetting to enable versioning or logging."
---
```

**Prompt**

```
[System]
Produce a Terraform module scaffold with main.tf, variables.tf, outputs.tf. Include S3 bucket for static hosting, CloudFront distribution, and OAI.

[User]
Bucket: {{bucket_name}}, Domain: {{domain_name}}.

[Output]
JSON with module_name and files map.
```

---

## 5. AWS – CloudFormation Autoscaling Group with ALB

```yaml
---
title: "Create a CloudFormation template for an autoscaling group behind an ALB"
id: aws-cfn-asg-alb
intent: "Generate a complete CloudFormation YAML template."
difficulty: advanced
provider: aws
tags: [cloudformation, autoscaling]
variables:
  instance_type:
    type: string
    example: t3.micro
  min_size:
    type: number
    example: 2
  max_size:
    type: number
    example: 4
expected_output_schema:
  type: object
  properties:
    template_yaml: {type: string}
    key_resources: {type: array, items: {type: string}}
  required: [template_yaml, key_resources]
sample_input:
  instance_type: t3.micro
  min_size: 2
  max_size: 4
sample_output:
  template_yaml: "AWSTemplateFormatVersion: '2010-09-09'\nResources: ..."
  key_resources: [LaunchTemplate, AutoScalingGroup, ALB, TargetGroup]
rationale: "Use for scalable web apps. Ensure health checks are correctly configured."
---
```

**Prompt**

```
[System]
Write a CloudFormation template that creates a launch template, autoscaling group, Application Load Balancer, and target group.

[User]
Instance type: {{instance_type}}, min size {{min_size}}, max size {{max_size}}.

[Output]
JSON with template_yaml and key_resources list.
```

---

## 6. Azure – VNet with Subnets and NSGs (Bicep)

```yaml
---
title: "Design an Azure VNet with subnets, NSGs, and route tables"
id: azure-vnet-nsg
intent: "Generate a Bicep template for a secure Azure network."
difficulty: intermediate
provider: azure
tags: [networking, bicep]
variables:
  vnet_address_space:
    type: string
    example: "10.1.0.0/16"
  subnets:
    type: list
    example: [{"name": "web", "prefix": "10.1.1.0/24"}, {"name": "db", "prefix": "10.1.2.0/24"}]
expected_output_schema:
  type: object
  properties:
    bicep_code: {type: string}
    resource_ids:
      type: object
      properties:
        vnet_id: {type: string}
        subnet_ids: {type: object}
  required: [bicep_code, resource_ids]
sample_input:
  vnet_address_space: "10.1.0.0/16"
  subnets:
    - {name: web, prefix: "10.1.1.0/24"}
    - {name: db, prefix: "10.1.2.0/24"}
sample_output:
  bicep_code: "resource vnet 'Microsoft.Network/virtualNetworks@2021-02-01' = { ... }"
  resource_ids:
    vnet_id: "[resourceId('Microsoft.Network/virtualNetworks', 'myVnet')]"
    subnet_ids:
      web: "[resourceId('Microsoft.Network/virtualNetworks/subnets', 'myVnet', 'web')]"
      db: "[resourceId('Microsoft.Network/virtualNetworks/subnets', 'myVnet', 'db')]"
rationale: "Covers default NSG rules. Common pitfall: missing route to 0.0.0.0/0 for internet access."
---
```

**Prompt**

```
[System]
Write a Bicep file that deploys a VNet, subnets, NSGs with default deny rules, and a route table.

[User]
Address space: {{vnet_address_space}}, subnets: {{subnets}}.

[Output]
JSON with bicep_code and resource_ids.
```

---

## 7. Azure – RBAC Least‑Privilege Role Assignment

```yaml
---
title: "Assign least‑privilege Azure RBAC role for a storage account"
id: azure-rbac-storage
intent: "Generate Azure CLI command for limited access."
difficulty: beginner
provider: azure
tags: [iam, security]
variables:
  storage_account_name:
    type: string
    example: mystorageacct
  principal_id:
    type: string
    example: "12345678-1234-1234-1234-123456789012"
  resource_group:
    type: string
    example: myResourceGroup
expected_output_schema:
  type: object
  properties:
    role_name: {type: string}
    cli_command: {type: string}
  required: [role_name, cli_command]
sample_input:
  storage_account_name: mystorageacct
  principal_id: "12345678-1234-1234-1234-123456789012"
  resource_group: myResourceGroup
sample_output:
  role_name: "Storage Blob Data Reader"
  cli_command: "az role assignment create --assignee 12345678-1234-1234-1234-123456789012 --role 'Storage Blob Data Reader' --scope /subscriptions/.../resourceGroups/myResourceGroup/providers/Microsoft.Storage/storageAccounts/mystorageacct"
rationale: "Use built-in roles where possible. Don't grant Contributor unless necessary."
---
```

**Prompt**

```
[System]
Suggest the most restrictive role for reading blobs and produce the exact `az` command.

[User]
Storage account: {{storage_account_name}}, principal: {{principal_id}}, resource group: {{resource_group}}.

[Output]
JSON with role_name and cli_command.
```

---

## 8. Azure – AKS Cluster Cost Estimate

```yaml
---
title: "Estimate monthly cost of an AKS cluster with node pools"
id: azure-aks-cost
intent: "Provide a rough cost estimate for Azure Kubernetes Service."
difficulty: beginner
provider: azure
tags: [finops, kubernetes]
variables:
  node_count:
    type: number
    example: 3
  vm_size:
    type: string
    example: Standard_D2s_v3
  region:
    type: string
    example: eastus
expected_output_schema:
  type: object
  properties:
    estimated_monthly_usd: {type: number}
    breakdown:
      type: object
      properties:
        compute: {type: number}
        management: {type: number}
  required: [estimated_monthly_usd, breakdown]
sample_input:
  node_count: 3
  vm_size: Standard_D2s_v3
  region: eastus
sample_output:
  estimated_monthly_usd: 240.00
  breakdown:
    compute: 210.00
    management: 30.00
rationale: "Assumes pay-as-you-go and 730 hours. Management cost is flat."
---
```

**Prompt**

```
[System]
Use Azure retail prices for {{region}}. Ignore data transfer and load balancer.

[User]
AKS with {{node_count}} nodes of size {{vm_size}}.

[Output]
JSON with estimated_monthly_usd and breakdown.
```

---

## 9. Azure – ARM Template for Cosmos DB with Backup

```yaml
---
title: "ARM template for Cosmos DB with continuous backup"
id: azure-arm-cosmosdb
intent: "Generate an ARM template for a production Cosmos DB account."
difficulty: advanced
provider: azure
tags: [database, arm]
variables:
  account_name:
    type: string
    example: mycosmosdb
  database_name:
    type: string
    example: ToDoList
  throughput:
    type: number
    example: 400
expected_output_schema:
  type: object
  properties:
    arm_template_json: {type: object}
    backup_policy: {type: object}
  required: [arm_template_json, backup_policy]
sample_input:
  account_name: mycosmosdb
  database_name: ToDoList
  throughput: 400
sample_output:
  arm_template_json:
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#"
    resources: [...]
  backup_policy:
    type: Continuous
rationale: "Ensure backup type is Continuous for point-in-time restore. Pitfall: forgetting to set default consistency level."
---
```

**Prompt**

```
[System]
Write an ARM template for a Cosmos DB SQL API account with continuous backup and a database with {{throughput}} RU/s.

[User]
Account: {{account_name}}, database: {{database_name}}, throughput: {{throughput}}.

[Output]
JSON with arm_template_json and backup_policy.
```

---

## 10. GCP – Secure VPC with Cloud NAT

```yaml
---
title: "Create a GCP VPC with subnet, Cloud NAT, and firewall rules"
id: gcp-vpc-nat
intent: "Generate Deployment Manager configuration for a private GCP network."
difficulty: intermediate
provider: gcp
tags: [networking, deployment-manager]
variables:
  region:
    type: string
    example: us-central1
  subnet_cidr:
    type: string
    example: "10.0.0.0/24"
expected_output_schema:
  type: object
  properties:
    config_yaml: {type: string}
    resources:
      type: array
      items: {type: string}
  required: [config_yaml, resources]
sample_input:
  region: us-central1
  subnet_cidr: "10.0.0.0/24"
sample_output:
  config_yaml: "resources:\n- name: my-vpc\n  type: compute.v1.network..."
  resources: [my-vpc, my-subnet, my-nat, my-firewall]
rationale: "Use for private clusters. Ensure Cloud NAT is regional."
---
```

**Prompt**

```
[System]
Generate a GCP Deployment Manager YAML template with a VPC network, subnet, Cloud Router, Cloud NAT, and a firewall rule allowing SSH only from IAP ranges.

[User]
Region: {{region}}, subnet CIDR: {{subnet_cidr}}.

[Output]
JSON with config_yaml and list of resource names.
```

---

## 11. GCP – IAM Least‑Privilege for GCS Bucket

```yaml
---
title: "Assign least‑privilege IAM role on a GCS bucket"
id: gcp-iam-gcs
intent: "Produce gsutil command to grant object viewer role."
difficulty: beginner
provider: gcp
tags: [iam, security]
variables:
  bucket_name:
    type: string
    example: my-bucket
  member:
    type: string
    example: user:alice@example.com
expected_output_schema:
  type: object
  properties:
    command: {type: string}
    role: {type: string}
  required: [command, role]
sample_input:
  bucket_name: my-bucket
  member: user:alice@example.com
sample_output:
  command: "gsutil iam ch user:alice@example.com:roles/storage.objectViewer gs://my-bucket"
  role: roles/storage.objectViewer
rationale: "Object Viewer allows listing objects; only use if needed."
---
```

**Prompt**

```
[System]
Generate the exact gsutil command to grant read-only access to a GCS bucket.

[User]
Bucket: {{bucket_name}}, member: {{member}}.

[Output]
JSON with command and role.
```

---

## 12. GCP – Compute Engine Instance Template with Startup Script

```yaml
---
title: "Create a GCE instance template with startup script"
id: gcp-gce-instance-template
intent: "Generate a gcloud command to create an instance template."
difficulty: intermediate
provider: gcp
tags: [compute, automation]
variables:
  template_name:
    type: string
    example: my-template
  machine_type:
    type: string
    example: n1-standard-2
  startup_script_url:
    type: string
    example: gs://my-bucket/startup.sh
expected_output_schema:
  type: object
  properties:
    gcloud_command: {type: string}
    template_self_link_format: {type: string}
  required: [gcloud_command]
sample_input:
  template_name: my-template
  machine_type: n1-standard-2
  startup_script_url: gs://my-bucket/startup.sh
sample_output:
  gcloud_command: "gcloud compute instance-templates create my-template --machine-type=n1-standard-2 --metadata-from-file startup-script=startup.sh"
  template_self_link_format: "https://www.googleapis.com/compute/v1/projects/PROJECT/global/instanceTemplates/my-template"
rationale: "Use when scaling managed instance groups. Pitfall: ensure the script is accessible."
---
```

**Prompt**

```
[System]
Generate a gcloud compute instance-templates create command that includes the startup script from the URL.

[User]
Template name: {{template_name}}, machine type: {{machine_type}}, startup script URL: {{startup_script_url}}.

[Output]
JSON with gcloud_command and template_self_link_format.
```

---

## 13. Oracle OCI – VCN with Security List (Terraform)

```yaml
---
title: "Define an OCI VCN with public subnet and security list"
id: oci-vcn-security
intent: "Create Terraform code for a basic Oracle Cloud Infrastructure network."
difficulty: intermediate
provider: oracle
tags: [networking, terraform]
variables:
  compartment_id:
    type: string
    example: ocid1.compartment.oc1..example
  vcn_cidr:
    type: string
    example: "10.0.0.0/16"
  public_subnet_cidr:
    type: string
    example: "10.0.1.0/24"
expected_output_schema:
  type: object
  properties:
    terraform_code: {type: string}
    resource_ids:
      type: object
      properties:
        vcn_id: {type: string}
        subnet_id: {type: string}
  required: [terraform_code, resource_ids]
sample_input:
  compartment_id: ocid1.compartment.oc1..example
  vcn_cidr: "10.0.0.0/16"
  public_subnet_cidr: "10.0.1.0/24"
sample_output:
  terraform_code: "resource \"oci_core_vcn\" \"my_vcn\" { ... }"
  resource_ids:
    vcn_id: ocid1.vcn.oc1..example
    subnet_id: ocid1.subnet.oc1..example
rationale: "Always restrict security list ingress to minimal IPs. Avoid 0.0.0.0/0 for sensitive ports."
---
```

**Prompt**

```
[System]
Write Terraform resources for an OCI VCN and public subnet with an HTTPS ingress rule.

[User]
Compartment: {{compartment_id}}, VCN CIDR: {{vcn_cidr}}, public subnet: {{public_subnet_cidr}}.

[Output]
JSON with terraform_code and resource_ids.
```

---

## 14. Oracle OCI – IAM Policy for Object Storage

```yaml
---
title: "OCI IAM policy for read‑only access to Object Storage buckets"
id: oci-iam-object-storage
intent: "Generate an OCI IAM policy statement."
difficulty: beginner
provider: oracle
tags: [iam, security]
variables:
  group_name:
    type: string
    example: BucketReaders
  compartment_name:
    type: string
    example: MyCompartment
expected_output_schema:
  type: object
  properties:
    policy_statement: {type: string}
  required: [policy_statement]
sample_input:
  group_name: BucketReaders
  compartment_name: MyCompartment
sample_output:
  policy_statement: "Allow group BucketReaders to read buckets in compartment MyCompartment"
rationale: "OCI IAM uses verbs like 'read', 'inspect'. Avoid granting 'manage' unnecessarily."
---
```

**Prompt**

```
[System]
Write an OCI IAM policy that allows the group to read all buckets in the compartment.

[User]
Group: {{group_name}}, compartment: {{compartment_name}}.

[Output]
JSON with policy_statement.
```

---

## 15. Oracle OCI – Autonomous Database Provisioning with Backup

```yaml
---
title: "Provision an Autonomous Database with automatic backup"
id: oci-adb-backup
intent: "Generate Terraform configuration for OCI Autonomous Database."
difficulty: advanced
provider: oracle
tags: [database, terraform]
variables:
  db_name:
    type: string
    example: myadb
  cpu_count:
    type: number
    example: 1
  storage_tb:
    type: number
    example: 1
expected_output_schema:
  type: object
  properties:
    terraform_resource: {type: string}
    backup_config:
      type: object
      properties:
        auto_backup_enabled: {type: boolean}
        retention_days: {type: number}
  required: [terraform_resource, backup_config]
sample_input:
  db_name: myadb
  cpu_count: 1
  storage_tb: 1
sample_output:
  terraform_resource: "resource \"oci_database_autonomous_database\" \"myadb\" { ... }"
  backup_config:
    auto_backup_enabled: true
    retention_days: 30
rationale: "Ensure backup is enabled; pitfall: not enabling auto scaling can lead to outages."
---
```

**Prompt**

```
[System]
Generate an OCI Terraform resource for an Autonomous Database with automatic backup enabled, 30‑day retention.

[User]
DB name: {{db_name}}, CPUs: {{cpu_count}}, storage: {{storage_tb}} TB.

[Output]
JSON with terraform_resource and backup_config.
```

---

## 16. Kubernetes – PodDisruptionBudget for Critical Deployment

```yaml
---
title: "Create a PodDisruptionBudget for a critical deployment"
id: k8s-pdb-critical
intent: "Generate a PDB manifest ensuring high availability during voluntary disruptions."
difficulty: intermediate
provider: general
tags: [k8s, availability]
variables:
  app_name:
    type: string
    example: payment-service
  min_available:
    type: number
    example: 2
expected_output_schema:
  type: object
  properties:
    apiVersion: {type: string}
    kind: {type: string}
    metadata: {type: object}
    spec: {type: object}
  required: [apiVersion, kind, metadata, spec]
sample_input:
  app_name: payment-service
  min_available: 2
sample_output:
  apiVersion: policy/v1
  kind: PodDisruptionBudget
  metadata:
    name: payment-service-pdb
  spec:
    minAvailable: 2
    selector:
      matchLabels:
        app: payment-service
rationale: "Use with clusters that undergo node upgrades. Pitfall: setting minAvailable too high can block node drains."
---
```

**Prompt**

```
[System]
Generate a Kubernetes PDB manifest (policy/v1) for the deployment labeled app={{app_name}}. Set minAvailable to {{min_available}}.

[Output]
JSON that represents a valid Kubernetes manifest.
```

---

## 17. Kubernetes – Network Policy Isolating Namespace

```yaml
---
title: "Default deny‑all network policy with specific allow rules"
id: k8s-netpol-deny-all
intent: "Create a secure baseline NetworkPolicy that denies all traffic and then permits required flows."
difficulty: advanced
provider: general
tags: [k8s, security]
variables:
  namespace:
    type: string
    example: production
  allowed_apps:
    type: list
    example: [frontend, backend]
expected_output_schema:
  type: object
  properties:
    policies:
      type: array
      items: {type: object}
  required: [policies]
sample_input:
  namespace: production
  allowed_apps: [frontend, backend]
sample_output:
  policies:
    - kind: NetworkPolicy
      metadata: {name: deny-all, namespace: production}
      spec: {podSelector: {}, policyTypes: [Ingress, Egress]}
    - kind: NetworkPolicy
      metadata: {name: allow-frontend-to-backend, namespace: production}
      spec:
        podSelector: {matchLabels: {app: backend}}
        ingress:
          - from:
              - podSelector: {matchLabels: {app: frontend}}
rationale: "Start with deny-all, then open only necessary paths. Avoid over‑permissive rules."
---
```

**Prompt**

```
[System]
Design NetworkPolicies for namespace {{namespace}}. First create a deny‑all policy, then allow traffic between apps in {{allowed_apps}}.

[Output]
JSON object with a "policies" array containing both manifests.
```

---

## 18. Kubernetes – HPA manifest for CPU and Memory

```yaml
---
title: "Horizontal Pod Autoscaler for CPU and memory utilization"
id: k8s-hpa-cpu-memory
intent: "Generate an HPA manifest targeting a deployment."
difficulty: intermediate
provider: general
tags: [k8s, scaling]
variables:
  deployment_name:
    type: string
    example: api-gateway
  min_replicas:
    type: number
    example: 2
  max_replicas:
    type: number
    example: 10
  cpu_target_percent:
    type: number
    example: 70
  memory_target_percent:
    type: number
    example: 80
expected_output_schema:
  type: object
  properties:
    apiVersion: {type: string}
    kind: {type: string}
    metadata: {type: object}
    spec: {type: object}
  required: [apiVersion, kind, metadata, spec]
sample_input:
  deployment_name: api-gateway
  min_replicas: 2
  max_replicas: 10
  cpu_target_percent: 70
  memory_target_percent: 80
sample_output:
  apiVersion: autoscaling/v2
  kind: HorizontalPodAutoscaler
  metadata: {name: api-gateway-hpa}
  spec:
    scaleTargetRef: {apiVersion: apps/v1, kind: Deployment, name: api-gateway}
    minReplicas: 2
    maxReplicas: 10
    metrics:
      - type: Resource
        resource: {name: cpu, target: {type: Utilization, averageUtilization: 70}}
      - type: Resource
        resource: {name: memory, target: {type: Utilization, averageUtilization: 80}}
rationale: "Always set both CPU and memory to avoid thrashing. Ensure resource requests are defined."
---
```

**Prompt**

```
[System]
Generate an HPA (autoscaling/v2) for deployment {{deployment_name}}.

[User]
Min replicas: {{min_replicas}}, max: {{max_replicas}}, CPU target: {{cpu_target_percent}}%, memory target: {{memory_target_percent}}%.

[Output]
Valid Kubernetes HPA manifest as JSON.
```

---

## 19. Kubernetes – RBAC for CI/CD Service Account

```yaml
---
title: "RBAC roles for a CI/CD service account in a namespace"
id: k8s-rbac-cicd
intent: "Create a Role and RoleBinding for a CI/CD pipeline."
difficulty: intermediate
provider: general
tags: [k8s, security]
variables:
  namespace:
    type: string
    example: cicd
  service_account:
    type: string
    example: jenkins-sa
  allowed_verbs:
    type: list
    example: [get, list, create, update, patch, delete]
  resources:
    type: list
    example: [deployments, services, configmaps]
expected_output_schema:
  type: object
  properties:
    role:
      type: object
    role_binding:
      type: object
  required: [role, role_binding]
sample_input:
  namespace: cicd
  service_account: jenkins-sa
  allowed_verbs: [get, list, create, update, patch, delete]
  resources: [deployments, services, configmaps]
sample_output:
  role:
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata: {name: cicd-role, namespace: cicd}
    rules:
      - apiGroups: [apps, ""]
        resources: [deployments, services, configmaps]
        verbs: [get, list, create, update, patch, delete]
  role_binding:
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata: {name: cicd-binding, namespace: cicd}
    subjects:
      - kind: ServiceAccount
        name: jenkins-sa
        namespace: cicd
    roleRef: {kind: Role, name: cicd-role, apiGroup: rbac.authorization.k8s.io}
rationale: "Never use cluster-admin; scope permissions to one namespace. Missing apiGroups can cause silent failures."
---
```

**Prompt**

```
[System]
Create a Role and RoleBinding for service account {{service_account}} in namespace {{namespace}}. Allow verbs {{allowed_verbs}} on resources {{resources}}.

[Output]
JSON with `role` and `role_binding` objects.
```

---

## 20. CI/CD – GitHub Actions Workflow for Terraform Plan/Apply with Approval

```yaml
---
title: "GitHub Actions pipeline for Terraform with manual approval"
id: cicd-gha-terraform
intent: "Generate a complete workflow YAML for Terraform validate, plan, and apply."
difficulty: intermediate
provider: multi
tags: [terraform, github-actions]
variables:
  working_directory:
    type: string
    example: terraform/
  environment_name:
    type: string
    example: staging
expected_output_schema:
  type: object
  properties:
    workflow_yaml: {type: string}
    required_secrets: {type: array, items: {type: string}}
  required: [workflow_yaml, required_secrets]
sample_input:
  working_directory: terraform/
  environment_name: staging
sample_output:
  workflow_yaml: |
    name: "Terraform"
    on:
      push:
        branches: [main]
    jobs:
      terraform:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v3
          - uses: hashicorp/setup-terraform@v2
          - run: terraform init
          - run: terraform validate
          - run: terraform plan -out=tfplan
          - uses: trstringer/manual-approval@v1
            with:
              secret: ${{ github.TOKEN }}
              approvers: user1
          - run: terraform apply tfplan
  required_secrets: [AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY]
rationale: "Manual approval step prevents accidental applies. Ensure the approver is defined."
---
```

**Prompt**

```
[System]
Produce a GitHub Actions workflow that runs Terraform init, validate, plan, waits for manual approval, then applies in environment {{environment_name}}. Working directory: {{working_directory}}.

[Output]
JSON with workflow_yaml and required_secrets list.
```

---

## 21. CI/CD – GitLab CI Pipeline for Docker Build and ECR Push

```yaml
---
title: "GitLab CI pipeline to build and push Docker image to Amazon ECR"
id: cicd-gitlab-ecr
intent: "Generate a .gitlab-ci.yml that builds a Docker image and pushes to ECR."
difficulty: intermediate
provider: aws
tags: [docker, gitlab-ci]
variables:
  ecr_repository:
    type: string
    example: "123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app"
  aws_region:
    type: string
    example: us-east-1
expected_output_schema:
  type: object
  properties:
    gitlab_ci_yaml: {type: string}
    required_variables: {type: array}
  required: [gitlab_ci_yaml, required_variables]
sample_input:
  ecr_repository: "123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app"
  aws_region: us-east-1
sample_output:
  gitlab_ci_yaml: "stages:\n  - build\n  - push\nbuild:\n  stage: build\n  script:\n    - docker build -t $ECR_REPO:$CI_COMMIT_SHA .\npush:\n  stage: push\n  script:\n    - aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_REPO\n    - docker push $ECR_REPO:$CI_COMMIT_SHA"
  required_variables: [AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, ECR_REPO]
rationale: "Use CI variables for credentials, never hardcode. Pitfall: missing Docker in Docker service."
---
```

**Prompt**

```
[System]
Write a GitLab CI pipeline with stages build and push. Use AWS CLI to authenticate and push to {{ecr_repository}}.

[User]
ECR repo: {{ecr_repository}}, region: {{aws_region}}.

[Output]
JSON with gitlab_ci_yaml and required_variables.
```

---

## 22. CI/CD – Canary Deployment Strategy with Argo Rollouts

```yaml
---
title: "Describe a canary deployment strategy using Argo Rollouts for Kubernetes"
id: cicd-canary-argo
intent: "Generate a step‑by‑step canary release configuration."
difficulty: advanced
provider: general
tags: [k8s, argo-rollouts]
variables:
  app_name:
    type: string
    example: my-app
  canary_steps:
    type: number
    example: 3
  weight_increment:
    type: number
    example: 30
expected_output_schema:
  type: object
  properties:
    rollout_manifest:
      type: object
    analysis_template:
      type: object
  required: [rollout_manifest]
sample_input:
  app_name: my-app
  canary_steps: 3
  weight_increment: 30
sample_output:
  rollout_manifest:
    apiVersion: argoproj.io/v1alpha1
    kind: Rollout
    metadata: {name: my-app}
    spec:
      replicas: 5
      strategy:
        canary:
          steps:
            - setWeight: 30
            - pause: {duration: 5m}
            - setWeight: 60
            - pause: {duration: 5m}
      selector:
        matchLabels: {app: my-app}
      template:
        metadata:
          labels: {app: my-app}
        spec:
          containers:
            - name: my-app
              image: my-app:latest
rationale: "Use with metrics‑based analysis to automate promotion. Pitfall: insufficient pause duration may miss issues."
---
```

**Prompt**

```
[System]
Create an Argo Rollout manifest for {{app_name}} with a canary strategy. Use {{canary_steps}} steps, each increasing traffic by {{weight_increment}}%, with a 5‑minute pause.

[Output]
JSON with rollout_manifest.
```

---

## 23. Observability – Prometheus Alert for High 5xx Error Rate

```yaml
---
title: "Prometheus alert rule for HTTP 5xx error rate"
id: observability-prom-5xx-alert
intent: "Generate a PrometheusRule manifest that fires when error rate exceeds threshold."
difficulty: intermediate
provider: general
tags: [prometheus, alerting]
variables:
  service_label:
    type: string
    example: api-gateway
  threshold_percent:
    type: number
    example: 5
expected_output_schema:
  type: object
  properties:
    alert_name: {type: string}
    expr: {type: string}
    severity: {type: string}
  required: [alert_name, expr, severity]
sample_input:
  service_label: api-gateway
  threshold_percent: 5
sample_output:
  alert_name: High5xxRate
  expr: "sum(rate(http_requests_total{service='api-gateway',status=~'5..'}[5m])) / sum(rate(http_requests_total{service='api-gateway'}[5m])) > 0.05"
  severity: critical
rationale: "Place in the same namespace as the service. Test that label selectors match."
---
```

**Prompt**

```
[System]
Write a PromQL alert rule that triggers when the 5xx error rate for service {{service_label}} exceeds {{threshold_percent}}% over the last 5 minutes.

[Output]
JSON with alert_name, expr, severity.
```

---

## 24. Observability – Grafana Dashboard Panel for p99 Latency

```yaml
---
title: "Grafana dashboard panel for p99 latency of a microservice"
id: observability-grafana-latency
intent: "Produce a Grafana panel JSON snippet."
difficulty: intermediate
provider: general
tags: [grafana, monitoring]
variables:
  datasource:
    type: string
    example: Prometheus
  job_name:
    type: string
    example: payment-service
expected_output_schema:
  type: object
  properties:
    panel_title: {type: string}
    targets: {type: array}
    panel_type: {type: string}
  required: [panel_title, targets, panel_type]
sample_input:
  datasource: Prometheus
  job_name: payment-service
sample_output:
  panel_title: "p99 Latency"
  panel_type: graph
  targets:
    - expr: "histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket{job='payment-service'}[5m])) by (le))"
rationale: "Adjust the quantile as needed. Ensure the job label matches your scrape config."
---
```

**Prompt**

```
[System]
Design a Grafana panel that shows p99 latency over time for {{job_name}}, using {{datasource}}.

[Output]
JSON with panel_title, panel_type, targets.
```

---

## 25. Observability – OpenTelemetry Collector Config for Tracing

```yaml
---
title: "OpenTelemetry Collector configuration for exporting traces to Jaeger"
id: observability-otel-collector
intent: "Generate a YAML config for the OTel Collector with OTLP receiver and Jaeger exporter."
difficulty: intermediate
provider: general
tags: [opentelemetry, tracing]
variables:
  jaeger_endpoint:
    type: string
    example: "http://jaeger-collector:14268/api/traces"
  service_name:
    type: string
    example: my-service
expected_output_schema:
  type: object
  properties:
    config_yaml: {type: string}
  required: [config_yaml]
sample_input:
  jaeger_endpoint: "http://jaeger-collector:14268/api/traces"
  service_name: my-service
sample_output:
  config_yaml: |
    receivers:
      otlp:
        protocols:
          grpc:
          http:
    exporters:
      jaeger:
        endpoint: "http://jaeger-collector:14268/api/traces"
    service:
      pipelines:
        traces:
          receivers: [otlp]
          exporters: [jaeger]
rationale: "Add batch processor for production. Pitfall: misconfigured endpoints lead to trace loss."
---
```

**Prompt**

```
[System]
Generate an OpenTelemetry Collector configuration that receives OTLP traces and exports to Jaeger at {{jaeger_endpoint}}.

[Output]
JSON with config_yaml.
```

---

## 26. Security – Lightweight Threat Model using STRIDE

```yaml
---
title: "Quick threat model for a cloud‑hosted web application"
id: security-threat-model-webapp
intent: "Identify potential threats using STRIDE methodology."
difficulty: advanced
provider: general
tags: [threat-modeling, security]
variables:
  components:
    type: list
    example: ["S3 static site", "API Gateway", "Lambda", "DynamoDB"]
  trust_boundaries:
    type: list
    example: ["Internet → CloudFront", "CloudFront → S3", "API Gateway → Lambda"]
expected_output_schema:
  type: object
  properties:
    threats:
      type: array
      items:
        type: object
        properties:
          component: {type: string}
          stride_category: {type: string}
          description: {type: string}
  required: [threats]
sample_input:
  components: ["S3 static site", "API Gateway", "Lambda", "DynamoDB"]
  trust_boundaries: ["Internet → CloudFront", "CloudFront → S3", "API Gateway → Lambda"]
sample_output:
  threats:
    - component: "S3 bucket"
      stride_category: "Information Disclosure"
      description: "Public read access due to misconfigured bucket policy"
    - component: "API Gateway"
      stride_category: "Denial of Service"
      description: "No rate limiting, allowing resource exhaustion"
    - component: "Lambda"
      stride_category: "Elevation of Privilege"
      description: "Over‑permissive execution role"
rationale: "Use early in design phase. Update as architecture evolves."
---
```

**Prompt**

```
[System]
Conduct a lightweight threat model using STRIDE. Focus on: {{components}} and trust boundaries: {{trust_boundaries}}.

[Output]
JSON with a threats array.
```

---

## 27. Security – OPA/Rego Policy to Deny Public S3 Buckets

```yaml
---
title: "Rego policy to deny public S3 buckets in Terraform"
id: security-opa-deny-public-s3
intent: "Write an OPA policy that prevents S3 buckets with public ACLs."
difficulty: intermediate
provider: aws
tags: [opa, policy-as-code]
variables:
  bucket_resource_type:
    type: string
    example: "aws_s3_bucket"
  acl_field:
    type: string
    example: "acl"
expected_output_schema:
  type: object
  properties:
    rego_policy: {type: string}
  required: [rego_policy]
sample_input:
  bucket_resource_type: aws_s3_bucket
  acl_field: acl
sample_output:
  rego_policy: |
    package terraform.analysis
    import input as tfplan
    deny[msg] {
      r := tfplan.resource_changes[_]
      r.type == "aws_s3_bucket"
      r.change.after.acl == "public-read"
      msg = sprintf("Bucket %v has public-read ACL", [r.address])
    }
rationale: "Extend to check block public access settings. Always run in CI pipelines."
---
```

**Prompt**

```
[System]
Create an OPA Rego policy that denies Terraform plans containing S3 buckets with public ACLs.

[User]
Resource type: {{bucket_resource_type}}, ACL field: {{acl_field}}.

[Output]
JSON with rego_policy string.
```

---

## 28. FinOps – Rightsizing Recommendations for EC2 Instances

```yaml
---
title: "Generate rightsizing recommendations based on CPU/Memory metrics"
id: finops-ec2-rightsizing
intent: "Suggest optimal instance types after analysing usage patterns."
difficulty: intermediate
provider: aws
tags: [finops, cost-optimization]
variables:
  current_instance_type:
    type: string
    example: m5.large
  avg_cpu_percent:
    type: number
    example: 15
  avg_memory_gb:
    type: number
    example: 3.2
expected_output_schema:
  type: object
  properties:
    recommended_instance_type: {type: string}
    estimated_savings_percent: {type: number}
    rationale: {type: string}
  required: [recommended_instance_type, estimated_savings_percent]
sample_input:
  current_instance_type: m5.large
  avg_cpu_percent: 15
  avg_memory_gb: 3.2
sample_output:
  recommended_instance_type: t3.medium
  estimated_savings_percent: 40
  rationale: "Current CPU utilisation 15%, memory 3.2GB – t3.medium provides 2 vCPU/4GB and burstable performance."
rationale: "Always test performance before migrating. Use AWS Compute Optimizer for data."
---
```

**Prompt**

```
[System]
Analyze the given usage metrics and recommend a more cost‑efficient EC2 instance type.

[User]
Current: {{current_instance_type}}, avg CPU: {{avg_cpu_percent}}%, avg memory: {{avg_memory_gb}} GB.

[Output]
JSON with recommended_instance_type, estimated_savings_percent, rationale.
```

---

## 29. SRE – Error Budget Policy & Burn‑Rate Alert

```yaml
---
title: "Define an error budget policy with burn‑rate alert"
id: sre-error-budget
intent: "Create an SLO and error budget rule for a service."
difficulty: advanced
provider: general
tags: [sre, slo]
variables:
  service_name:
    type: string
    example: checkout
  slo_percent:
    type: number
    example: 99.9
  lookback_minutes:
    type: number
    example: 60
expected_output_schema:
  type: object
  properties:
    error_budget_remaining_percent: {type: number}
    alert_rule_expr: {type: string}
    suggested_action: {type: string}
  required: [error_budget_remaining_percent, alert_rule_expr]
sample_input:
  service_name: checkout
  slo_percent: 99.9
  lookback_minutes: 60
sample_output:
  error_budget_remaining_percent: 98.5
  alert_rule_expr: "(1 - (sum(rate(http_requests_total{service='checkout',status!~'5..'}[60m])) / sum(rate(http_requests_total{service='checkout'}[60m])))) * 100 < 99.9"
  suggested_action: "Stop feature rollout and investigate cause of errors."
rationale: "Use multi‑window, multi‑burn‑rate alerts for better precision. Avoid noise by tuning burn rates."
---
```

**Prompt**

```
[System]
Define an error budget for {{service_name}} with SLO {{slo_percent}}% over a {{lookback_minutes}}-min window. Generate a PromQL alert that triggers when budget burn is too fast.

[Output]
JSON with error_budget_remaining_percent (assume current success matches SLO), alert_rule_expr, suggested_action.
```

---

## 30. Automation – Bash Script to Rotate IAM Access Keys

```yaml
---
title: "Bash script to rotate IAM access keys for a user"
id: automation-rotate-iam-keys
intent: "Generate a safe script that creates a new key, updates services, and deactivates the old key."
difficulty: professional
provider: aws
tags: [automation, security]
variables:
  user_name:
    type: string
    example: deploy-bot
  services_list:
    type: list
    example: ["Jenkins", "GitHub Actions"]
expected_output_schema:
  type: object
  properties:
    script: {type: string}
    safety_checks: {type: array, items: {type: string}}
  required: [script, safety_checks]
sample_input:
  user_name: deploy-bot
  services_list: ["Jenkins", "GitHub Actions"]
sample_output:
  script: |
    #!/bin/bash
    USER={{user_name}}
    NEW_KEY=$(aws iam create-access-key --user-name $USER --output json)
    AWS_ACCESS_KEY_ID=$(echo $NEW_KEY | jq -r .AccessKey.AccessKeyId)
    AWS_SECRET_ACCESS_KEY=$(echo $NEW_KEY | jq -r .AccessKey.SecretAccessKey)
    # Manual step: update Jenkins and GitHub Actions with new key
    echo "New key created. Please update the following services: {{services_list}}"
    read -p "Press enter after updating services to deactivate old key"
    OLD_KEY_ID=$(aws iam list-access-keys --user-name $USER --query 'AccessKeyMetadata[?Status==\"Active\"]|[0].AccessKeyId' --output text)
    aws iam update-access-key --access-key-id $OLD_KEY_ID --status Inactive --user-name $USER
    echo "Old key $OLD_KEY_ID deactivated."
  safety_checks:
    - "Do not delete the old key until services are verified."
    - "Store new credentials securely."
rationale: "Always validate with a dry‑run. Pitfall: forgetting to update all services leads to outages."
---
```

**Prompt**

```
[System]
Write a bash script that rotates the access key for IAM user {{user_name}}. After creating a new key, it should instruct the operator to update services [{{services_list}}] before deactivating the old key.

[Output]
JSON with script and safety_checks list.
```
