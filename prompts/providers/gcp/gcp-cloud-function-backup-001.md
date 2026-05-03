---
title: "Create a Scheduled Cloud Function for Automated GCS Backups"
id: "gcp-cloud-function-backup-001"
intent: "Generate Terraform and Python code for a Cloud Function that backs up BigQuery datasets to Cloud Storage on a schedule."
difficulty: intermediate
provider: gcp
tags: [terraform, cloud-function, python, backup, gcs]
maturity: production
variables:
  project_id:
    type: string
    description: "GCP project ID"
    example: "my-analytics-project"
  dataset_name:
    type: string
    description: "BigQuery dataset to backup"
    example: "prod_analytics"
  backup_schedule:
    type: string
    description: "Cloud Scheduler cron expression (UTC)"
    example: "0 2 * * *"
  backup_bucket:
    type: string
    description: "GCS bucket for backup storage"
    example: "bq-backups-prod"
expected_output_schema:
  type: object
  properties:
    terraform_code: { type: string }
    python_function: { type: string }
    scheduler_setup: { type: string }
changelog:
  - version: "1.0.0"
    date: "2024-01-15"
    changes: "Initial version"
---

## Rationale

**When to Use**: Automated backups prevent data loss from accidental deletion or corruption. Scheduled Cloud Functions are cost-effective for time-based tasks like exporting BigQuery datasets to GCS on a nightly basis.

**Common Pitfalls**: Missing IAM permissions for the Cloud Function service account, incorrect cron syntax for the scheduler, failing to account for BigQuery export limits.

**Prerequisites**: GCP Project, Terraform installed.

## System Instruction

You are an expert Google Cloud Data Engineer and DevOps architect. You create reliable, automated serverless workflows using Cloud Functions and Terraform, ensuring IAM permissions follow the principle of least privilege.

## User Instruction

I need to automate BigQuery backups to Google Cloud Storage. Please generate the Terraform configuration and the Python Cloud Function code to execute this:

- **Project ID**: {{project_id}}
- **Dataset to Backup**: {{dataset_name}}
- **Backup Schedule**: {{backup_schedule}}
- **Target Bucket**: {{backup_bucket}}

Include the Terraform code, the Python script for the Cloud Function, and any necessary scheduler configuration.

## Output Format

The response should be valid JSON matching this schema:
```json
{
  "terraform_code": "string",
  "python_function": "string",
  "scheduler_setup": "string"
}
```

## Variables

- `{{project_id}}`: GCP Project Identifier
- `{{dataset_name}}`: BigQuery Dataset to back up
- `{{backup_schedule}}`: Cron expression for the Cloud Scheduler job
- `{{backup_bucket}}`: Destination Cloud Storage bucket
