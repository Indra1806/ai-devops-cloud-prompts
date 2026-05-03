---
title: "GitHub Actions Workflow for Multi-Environment Deployment (Dev/Staging/Prod)"
id: "cicd-github-actions-multi-env-001"
intent: "Generate a GitHub Actions workflow that validates, builds, and deploys to multiple environments with approval gates."
difficulty: advanced
provider: github-actions
tags: [github-actions, ci-cd, deployment, approval-gates]
maturity: production
variables:
  repo_name:
    type: string
    description: "Repository name"
    example: "my-app"
  environments:
    type: array
    description: "Deployment environments"
    example: ["dev", "staging", "prod"]
  docker_registry:
    type: string
    description: "Docker registry (e.g., ECR, Docker Hub)"
    example: "123456789.dkr.ecr.us-east-1.amazonaws.com"
expected_output_schema:
  type: object
  properties:
    workflow_yaml: { type: string }
    secrets_setup: { type: array, items: { type: string } }
    approval_guide: { type: string }
changelog:
  - version: "1.0.0"
    date: "2024-01-15"
    changes: "Initial version"
---

## Rationale

**When to Use**: Standardizing deployments across multiple environments ensures consistency and safety. Using GitHub Actions environment protection rules provides native approval gates before production rollouts.

**Common Pitfalls**: Hardcoding environment variables in the workflow instead of using GitHub Environments, passing secrets incorrectly between jobs, not using artifact caching.

**Prerequisites**: GitHub repository, configured Docker registry.

## System Instruction

You are an expert CI/CD engineer specializing in GitHub Actions. You design secure, efficient, and reusable workflows that follow best practices, including proper dependency caching and manual approval gates for production deployments.

## User Instruction

Generate a complete GitHub Actions workflow for a multi-environment CI/CD pipeline with the following parameters:

- **Repository**: {{repo_name}}
- **Environments**: {{environments}}
- **Docker Registry**: {{docker_registry}}

The workflow should build and push a Docker image, then deploy sequentially to each environment. Include a guide on how to set up the necessary repository secrets and approval gates.

## Output Format

The response should be valid JSON matching this schema:
```json
{
  "workflow_yaml": "string",
  "secrets_setup": ["string"],
  "approval_guide": "string"
}
```

## Variables

- `{{repo_name}}`: Name of the application repository
- `{{environments}}`: The ordered list of deployment targets
- `{{docker_registry}}`: Target container registry URL
