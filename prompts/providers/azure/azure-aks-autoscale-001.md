---
title: "Deploy an AKS Cluster with Auto-Scaling and Network Policy"
id: "azure-aks-autoscale-001"
intent: "Generate Bicep template for production AKS cluster with VMSS autoscaling, managed identity, and network policies."
difficulty: advanced
provider: azure
tags: [bicep, aks, kubernetes, auto-scaling]
maturity: production
variables:
  cluster_name:
    type: string
    description: "AKS cluster name"
    example: "prod-aks-cluster"
  node_count:
    type: number
    description: "Initial number of nodes"
    example: 3
  max_nodes:
    type: number
    description: "Maximum nodes for autoscaling"
    example: 10
  vm_size:
    type: string
    description: "Azure VM size (e.g., Standard_D4s_v3)"
    example: "Standard_D4s_v3"
  k8s_version:
    type: string
    description: "Kubernetes version"
    example: "1.27.0"
expected_output_schema:
  type: object
  properties:
    bicep_template: { type: string }
    deployment_command: { type: string }
    post_deploy_steps: { type: array, items: { type: string } }
changelog:
  - version: "1.0.0"
    date: "2024-01-15"
    changes: "Initial version"
---

## Rationale

**When to Use**: AKS auto-scaling ensures applications handle traffic spikes while minimizing costs during low usage. Network policies enforce zero-trust networking within the cluster.

**Common Pitfalls**: Not configuring pod disruption budgets before autoscaling, insufficient resource requests/limits causing CrashLoopBackOff during scale-down, not integrating with Azure Monitor for autoscaling metrics.

**Prerequisites**: Azure Subscription, Azure CLI, basic understanding of Bicep and Kubernetes.

## System Instruction

You are an expert Azure Cloud Architect specializing in AKS deployments. You provide production-ready Bicep templates that enforce security through managed identities and network policies, while configuring cluster auto-scaling properly.

## User Instruction

Please generate a Bicep template for a production AKS cluster with the following specifications:

- **Cluster Name**: {{cluster_name}}
- **Initial Node Count**: {{node_count}}
- **Max Nodes for Auto-scaling**: {{max_nodes}}
- **VM Size**: {{vm_size}}
- **Kubernetes Version**: {{k8s_version}}

Ensure you include the deployment command required to apply this template via the Azure CLI, along with post-deployment verification steps.

## Output Format

The response should be valid JSON matching this schema:
```json
{
  "bicep_template": "string",
  "deployment_command": "string",
  "post_deploy_steps": ["string"]
}
```

## Variables

- `{{cluster_name}}`: The name of the AKS cluster
- `{{node_count}}`: Default number of nodes
- `{{max_nodes}}`: Auto-scaling upper bound
- `{{vm_size}}`: Azure VM series type
- `{{k8s_version}}`: Target K8s version
