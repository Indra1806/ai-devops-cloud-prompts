---
title: "Configure OCI Compartment Structure and IAM Policies"
id: "oracle-iam-compartments-001"
intent: "Generate Terraform code for a hierarchical OCI compartment structure with role-based access control (RBAC)."
difficulty: intermediate
provider: oracle
tags: [terraform, iam, compartments, governance]
maturity: production
variables:
  tenancy_name:
    type: string
    description: "OCI tenancy name"
    example: "my-org-tenancy"
  environments:
    type: array
    description: "List of environments (dev, staging, prod)"
    example: ["dev", "staging", "prod"]
  teams:
    type: array
    description: "Team names requiring separate access"
    example: ["platform", "analytics", "security"]
expected_output_schema:
  type: object
  properties:
    compartment_structure: { type: string }
    iam_policies: { type: array, items: { type: string } }
    access_control_matrix: { type: string }
changelog:
  - version: "1.0.0"
    date: "2024-01-15"
    changes: "Initial version"
---

## Rationale

**When to Use**: Correct compartment structure in Oracle Cloud Infrastructure (OCI) is essential for security boundaries, cost tracking, and governance. Setting this up as Code ensures parity across environments.

**Common Pitfalls**: Flat compartment structures, attaching policies to users instead of groups, and creating circular policy dependencies.

**Prerequisites**: OCI account with tenancy administrator privileges, Terraform installed.

## System Instruction

You are an expert Oracle Cloud Infrastructure architect. You generate structured and secure compartment configurations and corresponding IAM policies that map to organizational teams and environments using Terraform.

## User Instruction

I need to configure my OCI compartment hierarchy and IAM policies using Terraform. Please generate the code based on the following:

- **Tenancy**: {{tenancy_name}}
- **Environments**: {{environments}}
- **Teams**: {{teams}}

Output the Terraform structure, an array of generated IAM policies in OCI syntax, and an access control matrix explaining who has access to what.

## Output Format

The response should be valid JSON matching this schema:
```json
{
  "compartment_structure": "string",
  "iam_policies": ["string"],
  "access_control_matrix": "string"
}
```

## Variables

- `{{tenancy_name}}`: The root tenancy name
- `{{environments}}`: The logical environment boundaries
- `{{teams}}`: The operational groups requiring access
