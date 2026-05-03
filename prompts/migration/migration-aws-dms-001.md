---
title: "Plan and Execute On-Premises Database Migration to AWS RDS"
id: "migration-aws-dms-001"
intent: "Generate a migration plan including DMS tasks, minimal downtime cutover strategy, and rollback procedures."
difficulty: professional
provider: aws
tags: [dms, migration, database, terraform, high-availability]
maturity: production
variables:
  source_db_type:
    type: string
    description: "Source database type (oracle, mysql, postgresql)"
    example: "oracle"
  target_db_type:
    type: string
    description: "Target RDS database type"
    example: "postgresql"
  estimated_data_size_gb:
    type: number
    description: "Approximate database size"
    example: 500
  downtime_tolerance_minutes:
    type: number
    description: "Maximum acceptable downtime"
    example: 30
expected_output_schema:
  type: object
  properties:
    dms_configuration: { type: string }
    cutover_runbook: { type: string }
    rollback_plan: { type: string }
    validation_queries: { type: array, items: { type: string } }
changelog:
  - version: "1.0.0"
    date: "2024-01-15"
    changes: "Initial version"
---

## Rationale

**When to Use**: Migrating core databases carries massive risk. Using AWS Database Migration Service (DMS) enables continuous replication. This prompt ensures the migration is planned carefully with a focus on cutover and rollback safety.

**Common Pitfalls**: Ignoring schema conversion complexities (SCT), under-sizing the replication instance, not accounting for sequence synchronization after cutover.

**Prerequisites**: Source database accessible via network, AWS SCT (if heterogeneous).

## System Instruction

You are an expert Cloud Database Migration Specialist. You design zero-downtime or minimal-downtime migration architectures using AWS DMS, emphasizing data integrity validation and bulletproof rollback strategies.

## User Instruction

Generate a comprehensive database migration plan from on-premises to AWS RDS using the following parameters:

- **Source Database**: {{source_db_type}}
- **Target Database**: {{target_db_type}}
- **Data Size (GB)**: {{estimated_data_size_gb}}
- **Max Downtime (mins)**: {{downtime_tolerance_minutes}}

Provide the required AWS DMS task configuration logic, a step-by-step cutover runbook, a rollback plan in case of failure, and SQL queries to validate data integrity post-migration.

## Output Format

The response should be valid JSON matching this schema:
```json
{
  "dms_configuration": "string",
  "cutover_runbook": "string",
  "rollback_plan": "string",
  "validation_queries": ["string"]
}
```

## Variables

- `{{source_db_type}}`: The originating database engine
- `{{target_db_type}}`: The destination AWS RDS engine
- `{{estimated_data_size_gb}}`: Total size of data to migrate
- `{{downtime_tolerance_minutes}}`: Hard limit for read/write unavailability during cutover
