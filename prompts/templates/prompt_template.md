---
title: "[EXAMPLE] Design a Multi-AZ RDS Instance with Automated Backups"
id: "aws-rds-multiaz-001"
intent: "Generate a Terraform module and configuration for a production-ready RDS instance with multi-AZ failover, automated backups, and encryption."
difficulty: intermediate
provider: aws
tags:
  - terraform
  - rds
  - high-availability
  - disaster-recovery
maturity: production
variables:
  database_name:
    type: string
    description: "Name of the database to create"
    example: "production_db"
  db_instance_class:
    type: string
    description: "RDS instance type (e.g., db.t3.large, db.r5.xlarge)"
    example: "db.t3.large"
  allocated_storage_gb:
    type: number
    description: "Initial allocated storage in GB"
    example: 100
  backup_retention_days:
    type: number
    description: "Number of days to retain automated backups"
    example: 30
  maintenance_window:
    type: string
    description: "Preferred maintenance window (UTC, format: ddd:hh24:mi-ddd:hh24:mi)"
    example: "sun:03:00-sun:04:00"
  enable_encryption:
    type: boolean
    description: "Enable RDS encryption at rest"
    example: true
expected_output_schema:
  type: object
  properties:
    terraform_module:
      type: object
      properties:
        variables_tf:
          type: string
          description: "Terraform variables file content"
        main_tf:
          type: string
          description: "Terraform main configuration"
        outputs_tf:
          type: string
          description: "Terraform outputs"
      required: [variables_tf, main_tf, outputs_tf]
    deployment_steps:
      type: array
      items:
        type: object
        properties:
          step_number: { type: number }
          action: { type: string }
          command: { type: string }
          expected_output: { type: string }
      minItems: 3
    monitoring_checklist:
      type: array
      items: { type: string }
      minItems: 5
  required: [terraform_module, deployment_steps, monitoring_checklist]
sample_input:
  database_name: "analytics_db"
  db_instance_class: "db.t3.large"
  allocated_storage_gb: 100
  backup_retention_days: 30
  maintenance_window: "sun:03:00-sun:04:00"
  enable_encryption: true
sample_output:
  terraform_module:
    variables_tf: |
      variable "database_name" {
        type = string
      }
      variable "db_instance_class" {
        type = string
      }
    main_tf: |
      resource "aws_db_instance" "main" {
        identifier           = var.database_name
        instance_class       = var.db_instance_class
        multi_az             = true
        storage_encrypted    = true
      }
    outputs_tf: |
      output "db_endpoint" {
        value = aws_db_instance.main.endpoint
      }
  deployment_steps:
    - step_number: 1
      action: "Initialize Terraform"
      command: "terraform init"
      expected_output: "Terraform initialized in current directory"
    - step_number: 2
      action: "Plan infrastructure"
      command: "terraform plan -out=tfplan"
      expected_output: "Plan to create X resources"
    - step_number: 3
      action: "Apply configuration"
      command: "terraform apply tfplan"
      expected_output: "aws_db_instance.main created"
  monitoring_checklist:
    - "Enable Enhanced Monitoring"
    - "Configure CloudWatch alarms for CPU, connection count"
    - "Enable Performance Insights"
    - "Test automated backups with restore"
    - "Document failover runbook"
changelog:
  - version: "1.0.0"
    date: "2024-01-15"
    changes: "Initial production version with multi-AZ and encryption support"
---

## Rationale

### When to Use

Use this prompt when you need to:
- Design a production RDS deployment with high availability
- Ensure automatic failover across availability zones
- Enable encryption and automated backups
- Generate Terraform code for infrastructure as code
- Establish monitoring and alerting patterns

### Common Pitfalls

1. **Missing Multi-AZ**: Forgetting to enable multi-AZ failover for production workloads
2. **Insufficient Backup Windows**: Choosing a window that conflicts with peak usage hours
3. **Encryption Overhead**: Not accounting for ~5% performance impact of encryption
4. **Unencrypted Backups**: Enabling encryption on instance but not snapshots
5. **Under-provisioned Storage**: Not considering growth; RDS scaling requires downtime
6. **Missing Monitoring**: Not setting up CloudWatch alarms for connection count, CPU, storage

### Prerequisites

- AWS account with appropriate IAM permissions (ec2, rds, kms, logs)
- Terraform >= 1.0
- Understanding of database parameters for your workload (MySQL, PostgreSQL, etc.)
- VPC and security group already provisioned

---

## System Instruction

You are an expert AWS infrastructure architect specializing in production-grade RDS deployments. You provide Terraform code following AWS best practices for high availability, security, and observability. All code should be:
- Idempotent and declarative
- Well-commented
- Using variable input validation
- Including monitoring and logging
- Suitable for version control and CI/CD integration

You understand trade-offs between cost and reliability, and highlight them in your response.

---

## User Instruction

I need to design a production-ready RDS instance with the following requirements:

- **Database**: {{database_name}}
- **Instance Type**: {{db_instance_class}} (ensure this supports multi-AZ)
- **Storage**: {{allocated_storage_gb}} GB initial, auto-scaling enabled
- **Backup Retention**: {{backup_retention_days}} days
- **Maintenance Window**: {{maintenance_window}} (UTC)
- **Encryption**: {{enable_encryption}} (at rest and in transit)

Please generate:

1. **Terraform Module**: Complete `variables.tf`, `main.tf`, and `outputs.tf` files
   - Include multi-AZ failover configuration
   - Enable encryption with AWS KMS
   - Configure automated backups with specified retention
   - Include parameter group for performance tuning
   - Add security group rules for application access

2. **Deployment Steps**: Sequential commands to safely deploy
   - Include terraform init, plan, and apply
   - Recommendations for backup testing
   - Rollback procedures if needed

3. **Monitoring Checklist**: Post-deployment verification steps
   - CloudWatch metrics and alarms
   - Performance Insights configuration
   - Backup verification
   - Failover testing approach

---

## Output Format

Respond with a JSON object matching this structure:

```json
{
  "terraform_module": {
    "variables_tf": "<complete variables.tf content>",
    "main_tf": "<complete main.tf content>",
    "outputs_tf": "<complete outputs.tf content>"
  },
  "deployment_steps": [
    {
      "step_number": 1,
      "action": "<Description of action>",
      "command": "<Terraform or AWS CLI command>",
      "expected_output": "<What you should see if successful>"
    }
  ],
  "monitoring_checklist": [
    "<Item 1>",
    "<Item 2>"
  ]
}
```

---

## Variables

- `{{database_name}}`: The logical name for your database (e.g., `analytics_db`). This appears in AWS console and RDS endpoint.
- `{{db_instance_class}}`: AWS instance family (e.g., `db.t3.large` for burstable, `db.r5.xlarge` for memory-optimized). Check [RDS instance types](https://aws.amazon.com/rds/instance-types/) for details.
- `{{allocated_storage_gb}}`: Initial EBS volume size. **Note**: Cannot decrease without replacement; plan for growth or use auto-scaling.
- `{{backup_retention_days}}`: Retention period for automated snapshots. Longer retention increases storage cost (~$0.023/GB/month).
- `{{maintenance_window}}`: Time for AWS to apply patches. Choose off-peak hours; multi-AZ failover minimizes downtime.
- `{{enable_encryption}}`: Enable AWS KMS encryption for data at rest and RDS encryption for in-transit. Adds ~5% latency overhead but essential for compliance (HIPAA, PCI-DSS).

---

## Examples

### Example Input

```yaml
database_name: "analytics_db"
db_instance_class: "db.t3.large"
allocated_storage_gb: 100
backup_retention_days: 30
maintenance_window: "sun:03:00-sun:04:00"
enable_encryption: true
```

### Example Output

```json
{
  "terraform_module": {
    "variables_tf": "variable \"database_name\" {\n  type = string\n}\n\nvariable \"db_instance_class\" {\n  type = string\n}",
    "main_tf": "resource \"aws_db_instance\" \"main\" {\n  identifier = var.database_name\n  instance_class = var.db_instance_class\n  multi_az = true\n  storage_encrypted = true\n}",
    "outputs_tf": "output \"db_endpoint\" {\n  value = aws_db_instance.main.endpoint\n}"
  },
  "deployment_steps": [
    {
      "step_number": 1,
      "action": "Initialize Terraform",
      "command": "terraform init",
      "expected_output": "Terraform initialized successfully"
    }
  ],
  "monitoring_checklist": [
    "Enable Enhanced Monitoring in RDS console",
    "Configure CloudWatch alarms for CPU and connection count"
  ]
}
```

---

## Validation

**Required JSON Schema Validation**:
- All terraform files must be syntactically valid Terraform >= 1.0
- All deployment commands must be real `terraform` or `aws` CLI commands
- All monitoring items must be actionable (not aspirational)

**Safety Checks**:
- Do not output AWS access keys, secret keys, or credentials
- Do not output database master passwords
- Do not recommend overly permissive security group rules (e.g., CIDR 0.0.0.0/0)

