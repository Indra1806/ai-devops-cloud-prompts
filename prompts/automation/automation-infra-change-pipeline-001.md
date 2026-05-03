---
title: "Design Automated Infrastructure Change Pipeline with Review and Approval"
id: "automation-infra-change-pipeline-001"
intent: "Create a safe infrastructure change process using GitOps, Terraform plans, policy as code (OPA), and automated approvals."
difficulty: advanced
provider: generic
tags: [terraform, gitops, policy-as-code, automation]
maturity: production
variables:
  vcs_platform:
    type: string
    description: "Version control platform (github, gitlab, bitbucket)"
    example: "github"
  approval_requirement:
    type: string
    description: "Approval requirement (single, dual)"
    example: "dual"
  max_resource_deletion:
    type: string
    description: "Maximum resources allowed to delete per change"
    example: "5"
expected_output_schema:
  type: object
  properties:
    pipeline_architecture: { type: string }
    terraform_ci_config: { type: string }
    opa_policies: { type: array, items: { type: string } }
    approval_workflow: { type: string }
changelog:
  - version: "1.0.0"
    date: "2024-01-15"
    changes: "Initial version"
---

## Rationale

**When to Use**: Scaling infrastructure-as-code requires strict guardrails. This pipeline enforces Open Policy Agent (OPA) checks and limits blast radius (e.g., preventing massive accidental deletions) via automated GitOps.

**Common Pitfalls**: Bypassing branch protections in emergencies, failing to securely store Terraform state credentials, not archiving plan files between CI and CD stages.

**Prerequisites**: Terraform backend configured, OPA/Conftest installed.

## System Instruction

You are a DevSecOps Architect. You design automated, secure, and compliant GitOps pipelines for infrastructure as code, leveraging Policy as Code to prevent destructive or non-compliant changes.

## User Instruction

Design an automated Infrastructure as Code CI/CD pipeline with the following parameters:

- **VCS Platform**: {{vcs_platform}}
- **Required Approvals**: {{approval_requirement}}
- **Max Deletions Allowed**: {{max_resource_deletion}}

Generate the architecture overview, the CI configuration file (for Terraform plan and OPA evaluation), OPA policy snippets enforcing the deletion limits, and the step-by-step approval workflow.

## Output Format

The response should be valid JSON matching this schema:
```json
{
  "pipeline_architecture": "string",
  "terraform_ci_config": "string",
  "opa_policies": ["string"],
  "approval_workflow": "string"
}
```

## Variables

- `{{vcs_platform}}`: Source control and CI engine (e.g., GitHub, GitLab)
- `{{approval_requirement}}`: Number of mandatory human reviewers
- `{{max_resource_deletion}}`: Hard threshold for resources destroyed in a single apply
