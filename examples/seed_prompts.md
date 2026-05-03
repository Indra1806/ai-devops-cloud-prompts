# Seed Prompts – 20 High‑Value Examples

Each example includes full YAML front matter and the prompt body. Variables are clearly marked with `{{...}}`.

---

## 1. AWS – Secure VPC Design

```yaml
title: "Design a secure multi‑tier VPC with public and private subnets"
id: aws-vpc-multi-tier
intent: "Generate a Terraform configuration for a secure AWS VPC."
difficulty: intermediate
provider: aws
variables:
  - name: vpc_cidr
    type: string
    description: "CIDR block for the VPC"
    example: "10.0.0.0/16"
  - name: public_subnet_cidrs
    type: list
    description: "List of CIDR blocks for public subnets"
    example: ["10.0.1.0/24", "10.0.2.0/24"]
  - name: private_subnet_cidrs
    type: list
    description: "List of CIDR blocks for private subnets"
    example: ["10.0.10.0/24", "10.0.11.0/24"]
  - name: region
    type: string
    description: "AWS region"
    example: "us-east-1"
expected_output_schema:
  type: object
  properties:
    vpc_id:
      type: string
    public_subnet_ids:
      type: array
      items:
        type: string
    private_subnet_ids:
      type: array
      items:
        type: string
    nat_gateway_id:
      type: string
  required: ["vpc_id", "public_subnet_ids", "private_subnet_ids"]
sample_input:
  vpc_cidr: "10.0.0.0/16"
  public_subnet_cidrs: ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnet_cidrs: ["10.0.10.0/24", "10.0.11.0/24"]
  region: "us-east-1"
sample_output:
  vpc_id: "vpc-0abcd1234"
  public_subnet_ids: ["subnet-1111", "subnet-2222"]
  private_subnet_ids: ["subnet-3333", "subnet-4444"]
  nat_gateway_id: "nat-0abcd"
```

**Prompt**

```
[System]
You are a Terraform expert. Generate production‑ready HCL code that creates a VPC with the given CIDR, public and private subnets, an Internet Gateway, a NAT Gateway in the first public subnet, and route tables. Return only valid Terraform configuration inside a code block, preceded by a JSON object describing resource IDs as per the schema.

[User]
Create a VPC in {{region}} with CIDR {{vpc_cidr}}. Public subnets: {{public_subnet_cidrs}}. Private subnets: {{private_subnet_cidrs}}.

[Output]
First output a JSON object with keys: vpc_id, public_subnet_ids, private_subnet_ids, nat_gateway_id (use placeholder IDs like "vpc-0abcd1234"). Then write the Terraform code.
```

## 2. AWS – IAM Least‑Privilege for S3

```yaml
title: "Create least‑privilege IAM policy for an S3 bucket"
id: aws-iam-least-privilege-s3
intent: "Generate a secure IAM policy document that grants only required S3 actions."
difficulty: intermediate
provider: aws
variables:
  - name: bucket_name
    type: string
    description: "S3 bucket name"
    example: "my-app-data"
  - name: actions
    type: list
    description: "Allowed S3 actions"
    example: ["s3:GetObject", "s3:PutObject"]
  - name: effect
    type: string
    description: "Allow or Deny"
    example: "Allow"
expected_output_schema:
  type: object
  properties:
    policy_name:
      type: string
    policy_json:
      type: object
      properties:
        Version:
          type: string
        Statement:
          type: array
  required: ["policy_name", "policy_json"]
sample_output:
  policy_name: "s3-least-privilege-my-app-data"
  policy_json:
    Version: "2012-10-17"
    Statement:
      - Effect: "Allow"
        Action: ["s3:GetObject", "s3:PutObject"]
        Resource: "arn:aws:s3:::my-app-data/*"
```

**Prompt**
```
[System]
You are an AWS IAM security specialist. Construct an IAM policy in JSON that follows the principle of least privilege, granting only the specified actions on the given S3 bucket.

[User]
Bucket name: {{bucket_name}}. Allowed actions: {{actions}}. Effect: {{effect}}.

[Output]
Return a JSON object with policy_name (a sensible name) and policy_json (the full IAM policy document). Do not include explanations.
```

## 3. AWS – Cost Estimate for EC2 + RDS

```yaml
title: "Estimate monthly cost for EC2 and RDS deployment"
id: aws-cost-estimate-ec2-rds
intent: "Compute a rough AWS monthly cost estimate."
difficulty: beginner
provider: aws
tags: ["finops", "cost"]
variables:
  - name: instance_type
    type: string
    example: "t3.medium"
  - name: instance_count
    type: number
    example: 2
  - name: rds_instance_class
    type: string
    example: "db.t3.small"
  - name: storage_gb
    type: number
    example: 100
expected_output_schema:
  type: object
  properties:
    total_monthly_usd:
      type: number
    breakdown:
      type: object
      properties:
        ec2:
          type: number
        rds:
          type: number
  required: ["total_monthly_usd", "breakdown"]
sample_output:
  total_monthly_usd: 85.40
  breakdown:
    ec2: 48.00
    rds: 37.40
```

**Prompt**
```
[System]
Act as a FinOps analyst. Provide a rough monthly cost estimate in USD using on‑demand pricing for the specified resources. Use us‑east‑1 prices. Ignore data transfer.

[User]
EC2: {{instance_count}} × {{instance_type}}. RDS: {{rds_instance_class}} with {{storage_gb}} GB storage.

[Output]
JSON with total_monthly_usd and breakdown (ec2, rds).
```

## 4. AWS – Terraform Module Scaffold for S3 Website

```yaml
title: "Scaffold a Terraform module for static website hosting with S3 and CloudFront"
id: aws-tf-module-s3-website
intent: "Generate a reusable Terraform module skeleton."
difficulty: advanced
provider: aws
tags: ["terraform", "module"]
variables:
  - name: bucket_name
    type: string
    example: "www.example.com"
  - name: domain_name
    type: string
    example: "example.com"
expected_output_schema:
  type: object
  properties:
    module_name:
      type: string
    required_providers:
      type: array
    files:
      type: object
      description: "Map of filename to HCL content"
  required: ["module_name", "files"]
sample_output:
  module_name: "s3-static-website"
  required_providers:
    - aws
  files:
    main.tf: "resource \"aws_s3_bucket\"..."
    variables.tf: "variable \"bucket_name\"..."
    outputs.tf: "output \"website_endpoint\"..."
```

**Prompt**
```
[System]
You are a Terraform module author. Produce a scaffold for a module that creates an S3 bucket configured for static website hosting, with a CloudFront distribution in front. Return a JSON object with module_name, required_providers, and a files map containing main.tf, variables.tf, outputs.tf with placeholders.

[User]
Bucket name: {{bucket_name}}, Domain: {{domain_name}}.

[Output]
JSON as described. HCL code must be syntactically valid.
```

## 5. Azure – VNet with Subnets and NSGs

```yaml
title: "Design an Azure VNet with subnets, NSGs, and route tables"
id: azure-vnet-nsg
intent: "Generate a Bicep template for a secure Azure network."
difficulty: intermediate
provider: azure
variables:
  - name: vnet_address_space
    type: string
    example: "10.1.0.0/16"
  - name: subnets
    type: list
    description: "List of subnet names and prefixes"
    example: [{"name": "web", "prefix": "10.1.1.0/24"}, {"name": "db", "prefix": "10.1.2.0/24"}]
expected_output_schema:
  type: object
  properties:
    vnet_id:
      type: string
    subnet_ids:
      type: object
    nsg_ids:
      type: object
  required: ["vnet_id", "subnet_ids"]
sample_output:
  vnet_id: "/subscriptions/.../virtualNetworks/myVnet"
  subnet_ids:
    web: "/subscriptions/.../subnets/web"
    db: "/subscriptions/.../subnets/db"
  nsg_ids:
    web: "/subscriptions/.../networkSecurityGroups/web-nsg"
```

**Prompt**
```
[System]
You are an Azure network engineer. Write a Bicep file that creates a VNet, subnets, network security groups with default deny rules, and a route table. Return first a JSON summary of resource IDs (using placeholders), then the Bicep code.

[User]
Address space: {{vnet_address_space}}. Subnets: {{subnets}}.

[Output]
JSON summary then Bicep.
```

## 6. Azure – RBAC Least‑Privilege Role Assignment

```yaml
title: "Assign least‑privilege Azure RBAC role for a storage account"
id: azure-rbac-storage
intent: "Generate Azure CLI command and role definition for limited access."
difficulty: beginner
provider: azure
variables:
  - name: storage_account_name
    type: string
    example: "mystorageacct"
  - name: principal_id
    type: string
    example: "user-object-id"
  - name: scope
    type: string
    example: "/subscriptions/.../resourceGroups/rg/providers/Microsoft.Storage/storageAccounts/mystorageacct"
expected_output_schema:
  type: object
  properties:
    role_definition_name:
      type: string
    cli_command:
      type: string
  required: ["role_definition_name", "cli_command"]
sample_output:
  role_definition_name: "Storage Blob Data Reader"
  cli_command: "az role assignment create --assignee ... --role 'Storage Blob Data Reader' --scope ..."
```

**Prompt**
```
[System]
You assist with Azure IAM. Suggest the most restrictive built‑in role that allows read access to blob data, and produce the exact az CLI command.

[User]
Storage account: {{storage_account_name}}, principal: {{principal_id}}, scope: {{scope}}.

[Output]
JSON with role_definition_name and cli_command.
```

## 7. Azure – Cost Estimate for AKS Cluster

```yaml
title: "Estimate monthly cost of an AKS cluster with node pools"
id: azure-aks-cost
intent: "Provide a rough cost estimate for Azure Kubernetes Service."
difficulty: beginner
provider: azure
variables:
  - name: node_count
    type: number
    example: 3
  - name: vm_size
    type: string
    example: "Standard_D2s_v3"
  - name: region
    type: string
    example: "eastus"
expected_output_schema:
  type: object
  properties:
    estimated_monthly_usd:
      type: number
    breakdown:
      type: object
      properties:
        compute:
          type: number
        management:
          type: number
  required: ["estimated_monthly_usd", "breakdown"]
sample_output:
  estimated_monthly_usd: 240.00
  breakdown:
    compute: 210.00
    management: 30.00
```

**Prompt**
```
[System]
Use public Azure pricing (pay‑as‑you‑go, {{region}}) to estimate monthly cost for an AKS cluster with {{node_count}} worker nodes of size {{vm_size}}. Assume standard load balancer and 730 hours.

[Output]
JSON with estimated_monthly_usd and breakdown.
```

## 8. GCP – Secure VPC with Cloud NAT

```yaml
title: "Create a GCP VPC with subnet, Cloud NAT, and firewall rules"
id: gcp-vpc-nat
intent: "Generate a Deployment Manager configuration for a private GCP network."
difficulty: intermediate
provider: gcp
variables:
  - name: region
    type: string
    example: "us-central1"
  - name: subnet_cidr
    type: string
    example: "10.0.0.0/24"
expected_output_schema:
  type: object
  properties:
    network_name:
      type: string
    subnet_name:
      type: string
    cloud_nat_name:
      type: string
  required: ["network_name", "subnet_name", "cloud_nat_name"]
sample_output:
  network_name: "my-private-vpc"
  subnet_name: "my-subnet"
  cloud_nat_name: "my-nat"
```

**Prompt**
```
[System]
Write a GCP Deployment Manager YAML template that creates a VPC network, a subnet, a Cloud Router, and a Cloud NAT gateway. Use {{region}} and CIDR {{subnet_cidr}}. Then output a JSON with the resource names.

[User]
Region: {{region}}, subnet CIDR: {{subnet_cidr}}.

[Output]
JSON summary then the template.
```

## 9. GCP – IAM Least‑Privilege for Cloud Storage Bucket

```yaml
title: "Assign least‑privilege IAM role on a GCS bucket"
id: gcp-iam-gcs
intent: "Produce gcloud command to grant object viewer role on a bucket."
difficulty: beginner
provider: gcp
variables:
  - name: bucket_name
    type: string
    example: "my-bucket"
  - name: member
    type: string
    example: "user:alice@example.com"
expected_output_schema:
  type: object
  properties:
    gcloud_command:
      type: string
    role:
      type: string
  required: ["gcloud_command", "role"]
sample_output:
  gcloud_command: "gsutil iam ch user:alice@example.com:roles/storage.objectViewer gs://my-bucket"
  role: "roles/storage.objectViewer"
```

**Prompt**
```
[System]
Generate the exact gcloud/gsutil command to grant read‑only access to a GCS bucket.

[User]
Bucket: {{bucket_name}}, member: {{member}}.

[Output]
JSON with gcloud_command and role.
```

## 10. Oracle – VCN with Security List

```yaml
title: "Define an OCI VCN with public subnet and security list"
id: oci-vcn-security
intent: "Create Terraform code for a basic Oracle Cloud Infrastructure network."
difficulty: intermediate
provider: oracle
variables:
  - name: compartment_id
    type: string
    example: "ocid1.compartment.oc1..example"
  - name: vcn_cidr
    type: string
    example: "10.0.0.0/16"
  - name: public_subnet_cidr
    type: string
    example: "10.0.1.0/24"
expected_output_schema:
  type: object
  properties:
    vcn_id:
      type: string
    subnet_id:
      type: string
  required: ["vcn_id", "subnet_id"]
sample_output:
  vcn_id: "ocid1.vcn.oc1..example"
  subnet_id: "ocid1.subnet.oc1..example"
```

**Prompt**
```
[System]
Provide OCI Terraform resources for a VCN and a public subnet with an ingress rule for HTTPS. Use compartment {{compartment_id}}.

[User]
VCN CIDR: {{vcn_cidr}}, public subnet: {{public_subnet_cidr}}.

[Output]
JSON summary of IDs, then Terraform code.
```

## 11. Oracle – IAM Policy for Object Storage

```yaml
title: "OCI IAM policy for read‑only access to Object Storage buckets"
id: oci-iam-object-storage
intent: "Generate an OCI IAM policy statement."
difficulty: beginner
provider: oracle
variables:
  - name: group_name
    type: string
    example: "BucketReaders"
  - name: compartment_name
    type: string
    example: "MyCompartment"
expected_output_schema:
  type: object
  properties:
    policy_statement:
      type: string
  required: ["policy_statement"]
sample_output:
  policy_statement: "Allow group BucketReaders to read buckets in compartment MyCompartment"
```

**Prompt**
```
[System]
Write an OCI IAM policy that allows the group {{group_name}} to read all buckets in compartment {{compartment_name}}.

[Output]
JSON with policy_statement.
```

## 12. Kubernetes – Pod Disruption Budget for Critical App

```yaml
title: "Create a PodDisruptionBudget for a critical deployment"
id: k8s-pdb-critical
intent: "Generate a PDB manifest ensuring high availability during voluntary disruptions."
difficulty: intermediate
provider: agnostic
tags: ["k8s", "availability"]
variables:
  - name: app_name
    type: string
    example: "payment-service"
  - name: min_available
    type: number
    example: 2
expected_output_schema:
  type: object
  properties:
    apiVersion:
      type: string
    kind:
      type: string
    metadata:
      type: object
    spec:
      type: object
  required: ["apiVersion", "kind", "metadata", "spec"]
sample_output:
  apiVersion: "policy/v1"
  kind: "PodDisruptionBudget"
  metadata:
    name: "payment-service-pdb"
  spec:
    minAvailable: 2
    selector:
      matchLabels:
        app: "payment-service"
```

**Prompt**
```
[System]
Generate a Kubernetes PodDisruptionBudget manifest. Use apps/v1 for the deployment selector.

[User]
Application: {{app_name}}, minAvailable: {{min_available}}.

[Output]
JSON that represents a valid Kubernetes manifest.
```

## 13. Kubernetes – Network Policy to Isolate Namespace

```yaml
title: "Default deny‑all network policy with specific allow rules"
id: k8s-netpol-deny-all
intent: "Create a secure baseline NetworkPolicy that denies all ingress/egress and then permits required flows."
difficulty: advanced
provider: agnostic
variables:
  - name: namespace
    type: string
    example: "production"
  - name: allowed_apps
    type: list
    example: ["frontend", "backend"]
expected_output_schema:
  type: object
  properties:
    policies:
      type: array
      items:
        type: object
  required: ["policies"]
sample_output:
  policies:
    - kind: NetworkPolicy
      metadata:
        name: deny-all
      spec:
        podSelector: {}
        policyTypes: ["Ingress", "Egress"]
    - kind: NetworkPolicy
      metadata:
        name: allow-frontend-to-backend
      spec:
        podSelector:
          matchLabels:
            app: backend
        ingress:
          - from:
              - podSelector:
                  matchLabels:
                    app: frontend
```

**Prompt**
```
[System]
Design Kubernetes NetworkPolicies for namespace {{namespace}}. First create a deny‑all policy, then allow traffic between apps in {{allowed_apps}}.

[Output]
JSON object with a "policies" array containing both manifests.
```

## 14. CI/CD – GitHub Actions Workflow for Terraform Plan/Apply

```yaml
title: "GitHub Actions pipeline for Terraform with manual approval"
id: cicd-gha-terraform
intent: "Generate a complete workflow YAML for Terraform validate, plan, and apply."
difficulty: intermediate
provider: agnostic
tags: ["terraform", "github-actions"]
variables:
  - name: working_directory
    type: string
    example: "terraform/"
  - name: environment
    type: string
    example: "staging"
expected_output_schema:
  type: object
  properties:
    workflow_yaml:
      type: string
    required_secrets:
      type: array
  required: ["workflow_yaml", "required_secrets"]
sample_output:
  workflow_yaml: "name: Terraform ..."
  required_secrets: ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"]
```

**Prompt**
```
[System]
Create a GitHub Actions workflow that runs on push to main, executes terraform fmt, validate, and plan in {{working_directory}}, and waits for manual approval before apply. Use environment {{environment}}. Output the complete YAML and a list of required secrets.

[Output]
JSON with workflow_yaml and required_secrets.
```

## 15. CI/CD – Canary Deployment Strategy Description

```yaml
title: "Describe a canary deployment strategy for Kubernetes"
id: cicd-canary-strategy
intent: "Generate a step‑by‑step runbook for canary releasing."
difficulty: intermediate
provider: agnostic
tags: ["kubernetes", "deployment"]
variables:
  - name: service_name
    type: string
    example: "my-app"
  - name: canary_percentage
    type: number
    example: 10
expected_output_schema:
  type: object
  properties:
    steps:
      type: array
      items:
        type: string
    monitoring_check:
      type: string
  required: ["steps"]
sample_output:
  steps:
    - "Deploy canary version as separate Deployment"
    - "Configure Istio VirtualService to route {{ canary_percentage }}% traffic to canary"
    - "Monitor error rate and latency for 5 minutes"
    - "Gradually increase traffic if metrics healthy"
  monitoring_check: "Prometheus query: rate(http_requests_total{service='my-app-canary'}[5m])"
```

**Prompt**
```
[System]
Outline a canary deployment process for {{service_name}} with {{canary_percentage}}% initial traffic. Include monitoring checks.

[Output]
JSON with steps array and monitoring_check string.
```

## 16. Observability – Prometheus Alert for High Error Rate

```yaml
title: "Prometheus alert rule for HTTP 5xx error rate"
id: observability-prom-5xx-alert
intent: "Generate a PrometheusRule manifest that fires when error rate exceeds threshold."
difficulty: intermediate
provider: agnostic
tags: ["prometheus", "alerting"]
variables:
  - name: service_label
    type: string
    example: "api-gateway"
  - name: threshold_percent
    type: number
    example: 5
expected_output_schema:
  type: object
  properties:
    alert_name:
      type: string
    expr:
      type: string
    severity:
      type: string
  required: ["alert_name", "expr", "severity"]
sample_output:
  alert_name: "High5xxRate"
  expr: "sum(rate(http_requests_total{service='api-gateway',status=~'5..'}[5m])) / sum(rate(http_requests_total{service='api-gateway'}[5m])) > 0.05"
  severity: "critical"
```

**Prompt**
```
[System]
Write a Prometheus alert rule (in PromQL) that triggers when the 5xx error rate for service {{service_label}} exceeds {{threshold_percent}}% over the last 5 minutes.

[Output]
JSON with alert_name, expr, severity.
```

## 17. Observability – Grafana Dashboard Panel for Latency

```yaml
title: "Grafana dashboard panel for p99 latency of a microservice"
id: observability-grafana-latency
intent: "Produce a Grafana panel JSON snippet for visualizing latency percentiles."
difficulty: intermediate
provider: agnostic
variables:
  - name: datasource
    type: string
    example: "Prometheus"
  - name: job_name
    type: string
    example: "payment-service"
expected_output_schema:
  type: object
  properties:
    panel_title:
      type: string
    targets:
      type: array
    panel_type:
      type: string
  required: ["panel_title", "targets", "panel_type"]
sample_output:
  panel_title: "p99 Latency"
  panel_type: "graph"
  targets:
    - expr: "histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket{job='payment-service'}[5m])) by (le))"
```

**Prompt**
```
[System]
Design a Grafana panel that shows p99 latency over time for {{job_name}}, using {{datasource}}.

[Output]
JSON with panel_title, panel_type, and targets.
```

## 18. Security – Lightweight Threat Model for a Web Application

```yaml
title: "Quick threat model for a cloud‑hosted web application"
id: security-threat-model-webapp
intent: "Identify potential threats using STRIDE methodology."
difficulty: advanced
provider: agnostic
tags: ["threat-modeling"]
variables:
  - name: app_components
    type: list
    example: ["S3 static site", "API Gateway", "Lambda", "DynamoDB"]
  - name: trust_boundaries
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
          component:
            type: string
          stride_category:
            type: string
          description:
            type: string
  required: ["threats"]
sample_output:
  threats:
    - component: "S3 bucket"
      stride_category: "Information Disclosure"
      description: "Public read access due to misconfigured bucket policy"
    - component: "API Gateway"
      stride_category: "Denial of Service"
      description: "No rate limiting, allowing resource exhaustion"
```

**Prompt**
```
[System]
Conduct a lightweight threat model using STRIDE. Focus on components: {{app_components}} and trust boundaries: {{trust_boundaries}}.

[Output]
JSON with a threats array; each item has component, stride_category, description.
```

## 19. FinOps – Rightsizing Recommendations for EC2 Instances

```yaml
title: "Generate rightsizing recommendations based on CPU/Memory metrics"
id: finops-ec2-rightsizing
intent: "Suggest optimal instance types after analysing usage patterns."
difficulty: intermediate
provider: aws
tags: ["finops", "cost-optimization"]
variables:
  - name: current_instance_type
    type: string
    example: "m5.large"
  - name: avg_cpu_percent
    type: number
    example: 15
  - name: avg_memory_gb
    type: number
    example: 3.2
expected_output_schema:
  type: object
  properties:
    recommended_instance_type:
      type: string
    estimated_savings_percent:
      type: number
    rationale:
      type: string
  required: ["recommended_instance_type", "estimated_savings_percent"]
sample_output:
  recommended_instance_type: "t3.medium"
  estimated_savings_percent: 40
  rationale: "Current CPU utilisation 15%, memory 3.2GB – t3.medium provides 2 vCPU/4GB and burstable performance."
```

**Prompt**
```
[System]
Analyse the given usage metrics and recommend a more cost‑efficient EC2 instance type.

[User]
Current: {{current_instance_type}}, avg CPU: {{avg_cpu_percent}}%, avg memory: {{avg_memory_gb}} GB.

[Output]
JSON with recommended_instance_type, estimated_savings_percent, rationale.
```

## 20. SRE – Error Budget Policy & Alert

```yaml
title: "Define an error budget policy with burn‑rate alert"
id: sre-error-budget
intent: "Create an SLO and error budget rule for a service."
difficulty: advanced
provider: agnostic
tags: ["sre", "slo"]
variables:
  - name: service_name
    type: string
    example: "checkout"
  - name: slo_percent
    type: number
    example: 99.9
  - name: lookback_window_minutes
    type: number
    example: 60
expected_output_schema:
  type: object
  properties:
    error_budget_percent_remaining:
      type: number
    alert_rule_expr:
      type: string
    suggested_action:
      type: string
  required: ["error_budget_percent_remaining", "alert_rule_expr"]
sample_output:
  error_budget_percent_remaining: 98.5
  alert_rule_expr: "(1 - (sum(rate(http_requests_total{service='checkout',status!~'5..'}[60m])) / sum(rate(http_requests_total{service='checkout'}[60m])))) * 100 < 99.9"
  suggested_action: "Stop feature rollout and investigate cause of errors."
```

**Prompt**
```
[System]
Define an error budget for {{service_name}} with SLO {{slo_percent}}% over a {{lookback_window_minutes}}-minute window. Generate a PromQL alert that triggers when the budget burn rate is unsustainable.

[Output]
JSON with error_budget_percent_remaining (assuming current success rate matches SLO), alert_rule_expr, and suggested_action.
```
---

These 20 prompts span AWS, Azure, GCP, Oracle, Kubernetes, CI/CD, observability, security, FinOps, and SRE. They demonstrate the canonical template and can be directly used or adapted.
