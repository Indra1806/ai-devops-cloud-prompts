---
title: "Harden AWS Security Groups with Principle of Least Privilege"
id: "security-aws-sg-hardening-001"
intent: "Generate Terraform code to audit and harden security groups, removing overly permissive rules and enforcing encryption."
difficulty: intermediate
provider: aws
tags: [terraform, security, compliance, least-privilege]
maturity: production
variables:
  vpc_id:
    type: string
    description: "VPC ID to audit"
    example: "vpc-12345678"
  allowed_ssh_cidrs:
    type: array
    description: "CIDR blocks allowed for SSH"
    example: ["10.0.0.0/8", "203.0.113.0/24"]
  remove_world_access:
    type: boolean
    description: "Remove 0.0.0.0/0 rules (except HTTP/HTTPS)"
    example: true
expected_output_schema:
  type: object
  properties:
    audit_report: { type: string }
    terraform_remediation: { type: string }
    risk_summary: { type: string }
changelog:
  - version: "1.0.0"
    date: "2024-01-15"
    changes: "Initial version"
---

## Rationale

**When to Use**: Enforcing the principle of least privilege in Security Groups mitigates lateral movement during a breach. This prompt helps transition from permissive default groups to strict, audited ingress/egress boundaries.

**Common Pitfalls**: Removing `0.0.0.0/0` outbound traffic blindly and breaking application dependencies, forgetting to allow communication between intra-VPC components.

**Prerequisites**: AWS Account, VPC provisioned, Terraform.

## System Instruction

You are an expert AWS Cloud Security Architect. You audit existing cloud infrastructure and generate secure Terraform code that strictly enforces least privilege networking, avoiding overly permissive security groups.

## User Instruction

I need to harden the security groups for an existing AWS environment. Based on the following parameters:

- **VPC ID**: {{vpc_id}}
- **Allowed SSH CIDRs**: {{allowed_ssh_cidrs}}
- **Remove World Access**: {{remove_world_access}}

Please provide an audit report template, the Terraform remediation code to lock down the security groups, and a risk summary explaining the changes.

## Output Format

The response should be valid JSON matching this schema:
```json
{
  "audit_report": "string",
  "terraform_remediation": "string",
  "risk_summary": "string"
}
```

## Variables

- `{{vpc_id}}`: Target Virtual Private Cloud identifier
- `{{allowed_ssh_cidrs}}`: List of trusted IP ranges for port 22
- `{{remove_world_access}}`: Boolean flag to strip all 0.0.0.0/0 rules excluding web traffic
