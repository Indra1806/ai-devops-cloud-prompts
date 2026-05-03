---
title: "Deploy a Stateful Application (PostgreSQL) with Persistent Volumes"
id: "k8s-statefulset-postgres-001"
intent: "Generate Kubernetes manifests for a PostgreSQL StatefulSet with persistent storage, backup sidecar, and monitoring."
difficulty: advanced
provider: k8s
tags: [kubernetes, statefulset, postgresql, storage]
maturity: production
variables:
  app_name:
    type: string
    description: "Application name"
    example: "postgres-prod"
  replicas:
    type: number
    description: "Number of replicas"
    example: 3
  storage_size:
    type: string
    description: "Persistent volume size"
    example: "100Gi"
  backup_frequency:
    type: string
    description: "Backup cron schedule"
    example: "0 2 * * *"
expected_output_schema:
  type: object
  properties:
    statefulset_manifest: { type: string }
    storage_class_manifest: { type: string }
    backup_job_manifest: { type: string }
    monitoring_rules: { type: string }
changelog:
  - version: "1.0.0"
    date: "2024-01-15"
    changes: "Initial version"
---

## Rationale

**When to Use**: StatefulSets maintain stable pod identities and persistent storage, essential for databases like PostgreSQL. Sidecar containers handle backup automation without modifying the main application.

**Common Pitfalls**: Using Deployments instead of StatefulSets for databases, neglecting headless services causing connection issues, failing to set appropriate anti-affinity rules to distribute replicas.

**Prerequisites**: Kubernetes cluster, configured StorageClass.

## System Instruction

You are a Kubernetes expert and Database Administrator. You write resilient and production-ready Kubernetes manifests for stateful applications, ensuring persistent storage is correctly bound and backup processes are automated.

## User Instruction

Please generate Kubernetes manifests for a PostgreSQL deployment using a StatefulSet with the following requirements:

- **Application Name**: {{app_name}}
- **Replicas**: {{replicas}}
- **Storage Size**: {{storage_size}}
- **Backup Schedule**: {{backup_frequency}}

Include the StatefulSet manifest, the StorageClass manifest, a CronJob for backups, and basic Prometheus monitoring rules.

## Output Format

The response should be valid JSON matching this schema:
```json
{
  "statefulset_manifest": "string",
  "storage_class_manifest": "string",
  "backup_job_manifest": "string",
  "monitoring_rules": "string"
}
```

## Variables

- `{{app_name}}`: The name of the deployment and related resources
- `{{replicas}}`: Desired number of pod replicas
- `{{storage_size}}`: Persistent Volume Claim size
- `{{backup_frequency}}`: Cron format string for the backup job
