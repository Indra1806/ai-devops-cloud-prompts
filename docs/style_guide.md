# Prompt Style Guide

This guide ensures consistent, high-quality prompt writing across the library. All contributors should follow these conventions.

## Voice & Tone

### Professional but Approachable

- Assume the reader is a skilled engineer but may be new to the specific domain
- Use clear, direct language; avoid unnecessary jargon
- Be encouraging without being patronizing
- Strike a balance between formality (suitable for enterprise) and friendliness

**Good**: "Create an RDS instance with multi-AZ failover to ensure high availability."
**Bad**: "We should probably think about maybe making the database more available somehow."

### Action-Oriented

- Use imperative verbs: Generate, Design, Optimize, Automate, Migrate, Secure
- Avoid passive voice: "The VPC should be created" → "Create the VPC"
- Lead with the outcome: "Reduce cloud costs by 30%" not "Cost optimization techniques"

**Good**: "Generate a Terraform module for VPC provisioning."
**Bad**: "Discuss how one might approach VPC provisioning."

### Specific Examples

- Always provide concrete values, not generic placeholders
- Reference real AWS services, not "cloud provider X"
- Use realistic numbers: "100 GB", "90 days", "$1,200/month"

**Good**: "Transition objects to Glacier after 90 days to save ~$0.004 per GB per month."
**Bad**: "Archive old data to cheaper storage."

## Language

### Person

- Use **second person** ("you") when addressing the user
- Use **first person plural** ("we") when describing the project or community
- Avoid "one" ("One might consider") in favor of "you"

### Mood

- Use **imperative mood** for instructions: "Provide...", "Include...", "Output..."
- Use **conditional mood** sparingly for requirements: "if you need X, do Y"

### Tense

- Use **present tense**: "This variable holds...", "The schema validates..."
- Use **future tense** only for consequences: "Enabling this will reduce costs."

### Avoid

- **Hedging**: "might", "could", "possibly", "arguably"
- **Absolutes**: "always", "never" (use "typically", "generally" instead)
- **Marketing language**: "revolutionary", "amazing", "cutting-edge"
- **Contractions** in formal sections (but acceptable in examples)
- **Acronyms without definition** (first use: define in full, then use acronym)

## Formatting

### Titles

- **Action-oriented**: Use gerunds or noun phrases starting with action verbs
- **Specific**: Include provider or key tech: "AWS", "Kubernetes", "Terraform"
- **Concise**: Keep to 60 characters where possible

**Good titles**:
- "Design a Secure VPC with Private Subnets"
- "Migrate On-Premises Database to AWS RDS"
- "Deploy a Stateful Application to Kubernetes"

**Bad titles**:
- "VPC"
- "Database"
- "How to Use AWS"

### Headers

- Use **H2** (`##`) for major sections
- Use **H3** (`###`) for subsections
- Use **H4** (`####`) for minor details
- Avoid nesting more than 3 levels

**Structure**:
```markdown
## Rationale
### When to Use
### Common Pitfalls
### Prerequisites

## System Instruction

## User Instruction

## Output Format

## Variables

## Examples
### Example Input
### Example Output
```

### Lists

- Use **unordered lists** for alternatives, examples, or non-sequential items
- Use **ordered lists** only for steps or sequential instructions
- Keep list items parallel in structure
- Limit to 5-7 items per list (break into sub-lists if needed)

**Good**:
```markdown
You'll need:
- AWS account with EC2 permissions
- Terraform >= 1.0
- Familiarity with VPC concepts
```

**Bad**:
```markdown
You'll need AWS account, which should have EC2 permissions, and also Terraform and maybe VPC knowledge.
```

### Code Blocks

- Use **fenced code blocks** with language identifier
- Indent nested blocks by 2 spaces
- Include syntax highlighting for readability

```markdown
\`\`\`python
def validate(schema):
    return True
\`\`\`

\`\`\`yaml
variables:
  name: value
\`\`\`
```

### Variables & Placeholders

- Wrap placeholders in **`{{double_braces}}`** (not `{{single}}`, not `${bash}`)
- Define every variable in the Variables section
- Use descriptive names: `{{vpc_cidr}}`, not `{{var1}}`

**Good**: `aws_s3_bucket_{{bucket_name}}`
**Bad**: `aws_s3_bucket_${name}` or `aws_s3_bucket_[YOUR_BUCKET_NAME]`

### Links

- Use **relative paths** for internal resources: `[Contributing](CONTRIBUTING.md)`
- Use **full URLs** for external resources: `[AWS Docs](https://docs.aws.amazon.com)`
- Use **descriptive link text**, not "click here"

**Good**: `See [VPC documentation](https://docs.aws.amazon.com/vpc/) for details.`
**Bad**: `[Click here](https://docs.aws.amazon.com/vpc/) for more info.`

## Prompt Content

### System Instruction

- **Length**: 50-150 words
- **Purpose**: Define the AI's role, constraints, and output style
- **Include**: Expertise area, output format, safety guardrails

**Example**:
```
You are an AWS infrastructure architect specializing in cost optimization.
Provide concrete recommendations with implementation steps.
All Terraform code should follow best practices: modular, documented, validated.
Do not recommend solutions that violate security compliance (no overly permissive IAM).
Respond in JSON format matching the schema provided.
```

### User Instruction

- **Length**: 100-300 words
- **Structure**: Problem statement, constraints, requirements, expected output
- **Include**: All context needed to answer; reference variables with `{{placeholder}}`
- **Be specific**: Avoid vague terms like "optimize"; say "reduce cost by 25%" or "improve latency to <100ms"

**Example**:
```
I need to design a production RDS instance for analytics workload:
- Database: {{database_name}}
- Instance type: {{instance_class}} (must support multi-AZ)
- Storage: {{storage_gb}} GB, auto-scaling enabled
- Backup retention: {{backup_days}} days
- Encryption: {{enable_encryption}} (at rest and in transit)

Generate:
1. Terraform module (variables.tf, main.tf, outputs.tf)
2. Deployment steps with rollback plan
3. Monitoring checklist
```

### Output Format

- **Be explicit**: Specify format (JSON, YAML, Markdown, plain text, SQL)
- **Provide schema**: Include JSON Schema or example structure
- **Specify structure**: Field names, types, nested objects, arrays
- **Explain constraints**: Max tokens, precision, required fields

**Example**:
```
Respond with a JSON object:
{
  "terraform_code": "<string: complete Terraform module>",
  "deployment_steps": [
    {
      "step_number": <int>,
      "action": "<string>",
      "command": "<string>",
      "expected_output": "<string>"
    }
  ],
  "monitoring_checklist": ["<string>", ...]
}
```

### Variables Section

- **Define all placeholders** used in the prompt
- **Include**: type, description, example value
- **Be precise**: Specify constraints (min/max, enum values, formats)
- **Provide realistic examples**: Not "NAME_HERE", use "production_db"

**Example**:
```
- `{{database_name}}`: Name of the RDS database (e.g., `analytics_db`).
  Type: string. Constraint: 1-64 alphanumeric characters and underscores.

- `{{backup_days}}`: Number of days to retain automated backups.
  Type: number. Constraint: 1-35 (AWS limit). Example: 30.
```

## Metadata

### ID Format

```
<provider>-<category>-<sequence>
```

- `<provider>`: `aws`, `azure`, `gcp`, `oracle`, `k8s`, `generic`, `multi`
- `<category>`: Domain or service (e.g., `vpc-design`, `rds-backup`, `aks-autoscale`)
- `<sequence>`: Zero-padded 3-digit number (001, 002, ...)

**Examples**:
- `aws-vpc-design-001`
- `azure-aks-security-005`
- `k8s-pod-security-policy-001`
- `finops-cost-optimization-010`

### Tags

- **Minimum 3, maximum 5**
- **Lowercase, hyphenated**: `cloud-security`, `cost-optimization`
- **Reuse standard tags** (see CONTRIBUTING.md for list)

**Good tags**: `[terraform, iam, security, least-privilege, aws]`
**Bad tags**: `[Cloud, AWS stuff, terraform3, ...]`

### Difficulty

- `beginner`: Fundamentals, single component, minimal prerequisites
- `intermediate`: Multi-component, requires some domain knowledge
- `advanced`: Complex architecture, trade-off decisions
- `professional`: Production patterns, compliance, security hardening

## Examples

### Sample Input

- Use **realistic values**, not placeholders
- Show typical use case, not edge cases
- Match variable types and formats

**Good**:
```yaml
vpc_cidr: "10.0.0.0/16"
public_subnets: ["10.0.1.0/24", "10.0.2.0/24"]
enable_nat: true
```

**Bad**:
```yaml
vpc_cidr: "YOUR_CIDR_HERE"
public_subnets: ["SUBNET1", "SUBNET2"]
```

### Sample Output

- Demonstrate **complete, valid response**
- Include **nested structures** and **arrays** if applicable
- Show **realistic output**, not truncated
- Validate against expected_output_schema

## Rationale Section

Always include these subsections:

### When to Use
- Real-world scenarios where this prompt is helpful
- Problems it solves
- Typical use cases

### Common Pitfalls
- Mistakes engineers make
- Edge cases to watch for
- Cost traps, performance gotchas, security oversights

### Prerequisites
- Required tools, permissions, knowledge
- Assumed baseline
- Setup or configuration needed

## Validation Checklist

Before submitting, ensure:

- [ ] Title is action-oriented and specific
- [ ] All variables are defined and used consistently
- [ ] Example input/output are realistic and complete
- [ ] JSON Schema is valid and matches sample output
- [ ] Rationale explains when to use and common pitfalls
- [ ] No jargon without explanation
- [ ] No credentials, passwords, or keys in examples
- [ ] No marketing language or hyperbole
- [ ] Grammar and spelling correct
- [ ] Links work and are descriptive

---

## Examples

For well-written prompts, see:
- `prompts/providers/aws/` - AWS provider prompts
- `prompts/k8s/` - Kubernetes prompts
- `examples/seed_prompts.md` - Seed prompt examples
