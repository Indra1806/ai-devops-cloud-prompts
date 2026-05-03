---
title: "Define Prometheus Alert Rules for Kubernetes Cluster Health"
id: "observability-prometheus-alerts-001"
intent: "Generate Prometheus alert rules for common Kubernetes issues: node pressure, pod failures, high latency, resource exhaustion."
difficulty: intermediate
provider: k8s
tags: [prometheus, alerting, observability, sre]
maturity: production
variables:
  alert_namespace:
    type: string
    description: "Kubernetes namespace for Prometheus"
    example: "monitoring"
  slack_webhook:
    type: string
    description: "Slack webhook URL for notifications"
    example: "https://hooks.slack.com/services/..."
  cpu_threshold_percent:
    type: number
    description: "CPU threshold for alerting"
    example: 80
expected_output_schema:
  type: object
  properties:
    alert_rules: { type: string }
    alertmanager_config: { type: string }
    runbook_links: { type: array, items: { type: string } }
changelog:
  - version: "1.0.0"
    date: "2024-01-15"
    changes: "Initial version"
---

## Rationale

**When to Use**: Prometheus alerting is crucial for proactive incident management in Kubernetes clusters. This defines standard alerts for memory/CPU pressure, CrashLoopBackOffs, and node health.

**Common Pitfalls**: Alert fatigue from thresholds being set too low, missing "for" duration causing flapping alerts, poorly formatted Alertmanager routes.

**Prerequisites**: Kubernetes cluster, Prometheus Operator installed.

## System Instruction

You are an expert Site Reliability Engineer specializing in Kubernetes Observability. You design robust Prometheus alert rules that are actionable, appropriately severity-labeled, and avoid alert fatigue.

## User Instruction

Please generate a set of Prometheus alert rules and an Alertmanager configuration based on the following:

- **Namespace**: {{alert_namespace}}
- **Slack Webhook URL**: {{slack_webhook}}
- **CPU Threshold (%)**: {{cpu_threshold_percent}}

Ensure you include rules for high CPU, memory exhaustion, pod restart loops, and node unreachability. Provide the `alert_rules` block, `alertmanager_config`, and placeholder `runbook_links` for incident response.

## Output Format

The response should be valid JSON matching this schema:
```json
{
  "alert_rules": "string",
  "alertmanager_config": "string",
  "runbook_links": ["string"]
}
```

## Variables

- `{{alert_namespace}}`: K8s namespace where Prometheus runs
- `{{slack_webhook}}`: Alertmanager Slack receiver endpoint
- `{{cpu_threshold_percent}}`: Sustained CPU utilization before alerting
