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

[System]
You are an AWS IAM specialist. Craft a policy document (JSON) that grants only the specified S3 actions on the bucket.

[User]
Bucket name: {{bucket_name}}. Allowed actions: {{actions}}.

[Output]
Return a JSON object with policy_name and policy_json. Use the principle of least privilege.
