---
title: "Define Service Level Objectives (SLOs) and Service Level Indicators (SLIs)"
id: "sre-slo-sli-definition-001"
intent: "Create an SLO/SLI framework for a microservice, including error budgets, alerts, and Grafana dashboard."
difficulty: advanced
provider: generic
tags: [sre, slo, sli, monitoring, error-budget]
maturity: production
variables:
  service_name:
    type: string
    description: "Service name"
    example: "payment-api"
  target_availability_percent:
    type: number
    description: "Target availability (e.g., 99.9 for 99.9%)"
    example: 99.9
  target_latency_ms:
    type: number
    description: "Target P99 latency in milliseconds"
    example: 500
  error_budget_percent:
    type: number
    description: "Allowed error budget as percentage of SLO"
    example: 10
expected_output_schema:
  type: object
  properties:
    slo_definition: { type: string }
    sli_metrics: { type: array, items: { type: string } }
    grafana_dashboard: { type: string }
    alert_rules: { type: array, items: { type: string } }
changelog:
  - version: "1.0.0"
    date: "2024-01-15"
    changes: "Initial version"
---

## Rationale

**When to Use**: SLOs provide a data-driven way to balance feature velocity with service reliability. This prompt establishes the foundational metrics (SLIs) and the business agreement (SLO) for a service.

**Common Pitfalls**: Creating SLOs that are too strict (e.g., 100%), measuring from the server-side instead of the client-side, failing to define consequences for error budget depletion.

**Prerequisites**: Understanding of SRE principles, monitoring stack (Prometheus/Grafana) deployed.

## System Instruction

You are an expert Site Reliability Engineer (SRE). You bridge the gap between business requirements and technical metrics by defining clear, measurable Service Level Objectives and corresponding error budgets.

## User Instruction

I need to define an SLO framework for a core microservice. Please use the following details:

- **Service Name**: {{service_name}}
- **Target Availability (%)**: {{target_availability_percent}}
- **Target P99 Latency (ms)**: {{target_latency_ms}}
- **Error Budget Alert %**: {{error_budget_percent}}

Generate the formal SLO definition, the specific SLI metrics to track it, a JSON snippet for a Grafana dashboard panel, and Prometheus alert rules for error budget burn rate.

## Output Format

The response should be valid JSON matching this schema:
```json
{
  "slo_definition": "string",
  "sli_metrics": ["string"],
  "grafana_dashboard": "string",
  "alert_rules": ["string"]
}
```

## Variables

- `{{service_name}}`: The application or microservice being measured
- `{{target_availability_percent}}`: The reliability goal (e.g., 99.9)
- `{{target_latency_ms}}`: Performance threshold for successful requests
- `{{error_budget_percent}}`: Burn rate threshold that triggers pages
