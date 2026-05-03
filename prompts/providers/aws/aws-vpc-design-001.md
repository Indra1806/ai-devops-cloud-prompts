---
title: "Design a Secure VPC with Private and Public Subnets"
id: "aws-vpc-design-001"
intent: "Generate Terraform code for a multi-tier VPC architecture with public and private subnets, NAT gateways, and route tables."
difficulty: intermediate
provider: aws
tags: [terraform, networking, security, vpc]
maturity: production
variables:
  vpc_cidr:
    type: string
    description: "CIDR block for the VPC"
    example: "10.0.0.0/16"
  region:
    type: string
    description: "AWS region for deployment"
    example: "us-east-1"
  public_subnets:
    type: array
    description: "List of public subnet CIDR blocks"
    example: ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets:
    type: array
    description: "List of private subnet CIDR blocks"
    example: ["10.0.10.0/24", "10.0.11.0/24"]
  enable_nat:
    type: boolean
    description: "Enable NAT gateways for private subnet internet access"
    example: true
expected_output_schema:
  type: object
  properties:
    terraform_code:
      type: string
      description: "Complete Terraform configuration"
    architecture_diagram:
      type: string
      description: "ASCII art diagram of the VPC structure"
    deployment_checklist:
      type: array
      items: { type: string }
  required: [terraform_code, architecture_diagram, deployment_checklist]
sample_input:
  vpc_cidr: "10.0.0.0/16"
  region: "us-east-1"
  public_subnets: ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets: ["10.0.10.0/24", "10.0.11.0/24"]
  enable_nat: true
sample_output:
  terraform_code: "resource \"aws_vpc\" \"main\" {\n  cidr_block = \"10.0.0.0/16\"\n  enable_dns_hostnames = true\n}"
  architecture_diagram: "┌─────────────────────────┐\n│ VPC (10.0.0.0/16)       │\n│ ┌───────────┐ ┌───────┐ │\n│ │ Public    │ │ NAT   │ │\n│ │ Subnet    │ │ GW    │ │\n│ └───────────┘ └───────┘ │\n│ ┌───────────────────────┐│\n│ │ Private Subnet        ││\n│ └───────────────────────┘│\n└─────────────────────────┘"
  deployment_checklist: ["Create VPC", "Create subnets", "Create route tables", "Create NAT gateway"]
changelog:
  - version: "1.0.0"
    date: "2024-01-15"
    changes: "Initial production release"
---

## Rationale

**When to Use**: Multi-tier VPC design is foundational for AWS workloads. Public subnets host load balancers and NAT gateways; private subnets isolate applications and databases. NAT gateways provide secure internet access for private resources.

**Common Pitfalls**: Over-provisioning NAT gateways (each costs ~$32/month), using overly large CIDR blocks without planning for growth, not setting up VPC Flow Logs for troubleshooting.

**Prerequisites**: AWS account, understanding of CIDR blocks, Terraform installed.

## System Instruction

You are an expert AWS infrastructure architect specializing in secure network design. You provide Terraform code following AWS best practices for high availability, security, and networking. All code should be idempotent, well-commented, and include appropriate tags.

## User Instruction

I need to design a secure multi-tier VPC architecture using Terraform. Please implement the following specifications:

- **CIDR Block**: {{vpc_cidr}}
- **Region**: {{region}}
- **Public Subnets**: {{public_subnets}}
- **Private Subnets**: {{private_subnets}}
- **NAT Gateways**: {{enable_nat}}

Ensure you generate the Terraform code, an ASCII architecture diagram, and a step-by-step deployment checklist.

## Output Format

The response should be valid JSON matching this schema:
```json
{
  "terraform_code": "string",
  "architecture_diagram": "string",
  "deployment_checklist": ["string"]
}
```

## Variables

- `{{vpc_cidr}}`: The IPv4 CIDR block for the entire VPC (e.g., 10.0.0.0/16)
- `{{region}}`: Target AWS region
- `{{public_subnets}}`: List of CIDR blocks for public subnets
- `{{private_subnets}}`: List of CIDR blocks for private subnets
- `{{enable_nat}}`: Boolean to indicate whether to provision NAT gateways

## Examples

### Example Input

```yaml
vpc_cidr: "10.0.0.0/16"
region: "us-east-1"
public_subnets: ["10.0.1.0/24", "10.0.2.0/24"]
private_subnets: ["10.0.10.0/24", "10.0.11.0/24"]
enable_nat: true
```

### Example Output

```json
{
  "terraform_code": "resource \"aws_vpc\" \"main\" {\n  cidr_block = \"10.0.0.0/16\"\n  enable_dns_hostnames = true\n}",
  "architecture_diagram": "┌─────────────────────────┐\n│ VPC (10.0.0.0/16)       │\n│ ┌───────────┐ ┌───────┐ │\n│ │ Public    │ │ NAT   │ │\n│ │ Subnet    │ │ GW    │ │\n│ └───────────┘ └───────┘ │\n│ ┌───────────────────────┐│\n│ │ Private Subnet        ││\n│ └───────────────────────┘│\n└─────────────────────────┘",
  "deployment_checklist": [
    "Create VPC",
    "Create subnets",
    "Create route tables",
    "Create NAT gateway"
  ]
}
```
