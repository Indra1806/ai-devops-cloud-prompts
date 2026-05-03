---
title: "Create S3 Bucket with Lifecycle Policies and Encryption"
id: "aws-s3-lifecycle-001"
intent: "Generate Terraform code for an S3 bucket with encryption, versioning, lifecycle rules to transition to Glacier, and audit logging."
difficulty: intermediate
provider: aws
tags: [terraform, s3, storage, cost-optimization]
maturity: production
variables:
  bucket_name:
    type: string
    description: "Globally unique S3 bucket name"
    example: "my-app-data-2024"
  transition_to_glacier_days:
    type: number
    description: "Days before transitioning objects to Glacier"
    example: 90
  delete_old_versions_days:
    type: number
    description: "Days before deleting old object versions"
    example: 365
  enable_versioning:
    type: boolean
    description: "Enable object versioning"
    example: true
expected_output_schema:
  type: object
  properties:
    terraform_main:
      type: string
    bucket_policy:
      type: string
    lifecycle_rules:
      type: array
      items:
        type: object
        properties:
          rule_name: { type: string }
          transition_days: { type: number }
          storage_class: { type: string }
    cost_analysis:
      type: object
      properties:
        estimated_monthly_cost: { type: number }
        savings_vs_no_transition: { type: number }
sample_input:
  bucket_name: "analytics-data-2024"
  transition_to_glacier_days: 90
  delete_old_versions_days: 365
  enable_versioning: true
sample_output:
  terraform_main: "resource \"aws_s3_bucket\" \"data\" {\n  bucket = \"analytics-data-2024\"\n}"
  bucket_policy: "{\n\t\"Version\": \"2012-10-17\",\n\t\"Statement\": [{\n\t\t\"Effect\": \"Deny\",\n\t\t\"Principal\": \"*\",\n\t\t\"Action\": \"s3:*\",\n\t\t\"Resource\": \"arn:aws:s3:::analytics-data-2024/*\",\n\t\t\"Condition\": { \"Bool\": { \"aws:SecureTransport\": \"false\" } }\n\t}]\n}"
  lifecycle_rules:
    - rule_name: "Transition to Glacier"
      transition_days: 90
      storage_class: "GLACIER"
    - rule_name: "Delete old versions"
      transition_days: 365
      storage_class: "DELETED"
  cost_analysis:
    estimated_monthly_cost: 45.50
    savings_vs_no_transition: 120.75
changelog:
  - version: "1.0.0"
    date: "2024-01-15"
    changes: "Initial version"
---

## Rationale

**When to Use**: S3 lifecycle policies reduce storage costs by 60-80% by automatically transitioning old data to cheaper storage classes. Encryption and versioning ensure compliance and protect against accidental deletion.

**Common Pitfalls**: Forgetting to enable MFA delete for critical buckets, not considering retrieval costs when transitioning to Glacier, not implementing bucket policies to enforce encryption.

**Prerequisites**: AWS account, Terraform installed.

## System Instruction

You are an expert AWS infrastructure architect. You provide secure and cost-optimized Terraform code for AWS S3. All buckets must be encrypted by default and configured with appropriate lifecycle rules based on user inputs.

## User Instruction

Please generate Terraform code for a secure, cost-optimized S3 bucket. Include the following configuration:

- **Bucket Name**: {{bucket_name}}
- **Transition to Glacier**: After {{transition_to_glacier_days}} days
- **Delete old versions**: After {{delete_old_versions_days}} days
- **Versioning**: {{enable_versioning}}

Also provide the bucket policy to enforce TLS and an estimated cost analysis for this configuration.

## Output Format

The response should be valid JSON matching this schema:
```json
{
  "terraform_main": "string",
  "bucket_policy": "string",
  "lifecycle_rules": [
    {
      "rule_name": "string",
      "transition_days": 0,
      "storage_class": "string"
    }
  ],
  "cost_analysis": {
    "estimated_monthly_cost": 0.0,
    "savings_vs_no_transition": 0.0
  }
}
```

## Variables

- `{{bucket_name}}`: Globally unique name for the S3 bucket.
- `{{transition_to_glacier_days}}`: Number of days to wait before archiving data to Glacier.
- `{{delete_old_versions_days}}`: Number of days to retain old object versions.
- `{{enable_versioning}}`: Set to true to enable versioning.
