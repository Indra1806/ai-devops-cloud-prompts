---
title: "Design a secure multi‑tier VPC with public and private subnets"
id: aws-vpc-multi-tier
intent: "Generate Terraform configuration for a secure AWS VPC."
difficulty: intermediate
provider: aws
tags: [networking, terraform]
variables:
  vpc_cidr:
    type: string
    example: "10.0.0.0/16"
  public_subnet_cidrs:
    type: list
    example: ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnet_cidrs:
    type: list
    example: ["10.0.10.0/24", "10.0.11.0/24"]
  region:
    type: string
    example: "us-east-1"
expected_output_schema:
  type: object
  properties:
    vpc_id: {type: string}
    public_subnet_ids: {type: array, items: {type: string}}
    private_subnet_ids: {type: array, items: {type: string}}
  required: [vpc_id, public_subnet_ids, private_subnet_ids]
sample_input:
  vpc_cidr: "10.0.0.0/16"
  public_subnet_cidrs: ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnet_cidrs: ["10.0.10.0/24", "10.0.11.0/24"]
  region: "us-east-1"
sample_output:
  vpc_id: vpc-0abcd1234
  public_subnet_ids: [subnet-1111, subnet-2222]
  private_subnet_ids: [subnet-3333, subnet-4444]
rationale: "Use for greenfield VPC designs. Pitfall: forgetting NAT Gateway for private subnets."
---

[System]
You are a Terraform expert. Generate production‑ready HCL code that creates a VPC with the given CIDR, public and private subnets, Internet Gateway, NAT Gateway, and route tables. Return first a JSON object describing the resource IDs, then the Terraform code.

[User]
Create a VPC in {{region}} with CIDR {{vpc_cidr}}. Public subnets: {{public_subnet_cidrs}}. Private subnets: {{private_subnet_cidrs}}.

[Output]
First output the JSON object, then the Terraform code in a code block.
