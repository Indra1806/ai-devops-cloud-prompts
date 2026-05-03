---
title: "Generate AWS Cost Optimization Report with Rightsizing and RI/Savings Plan Recommendations"
id: "finops-aws-cost-optimization-001"
intent: "Analyze AWS spending patterns and recommend cost-saving measures: RI purchases, Savings Plans, instance downsizing, reserved capacity."
difficulty: advanced
provider: aws
tags: [finops, cost-optimization, rightsizing, reserved-instances]
maturity: production
variables:
  account_id:
    type: string
    description: "AWS account ID"
    example: "123456789012"
  analysis_period_months:
    type: number
    description: "Number of months to analyze"
    example: 12
  target_savings_percent:
    type: number
    description: "Target cost reduction percentage"
    example: 25
expected_output_schema:
  type: object
  properties:
    current_monthly_cost: { type: number }
    recommendations:
      type: array
      items:
        type: object
        properties:
          recommendation: { type: string }
          monthly_savings: { type: number }
          implementation_effort: { type: string }
    implementation_roadmap: { type: array, items: { type: string } }
changelog:
  - version: "1.0.0"
    date: "2024-01-15"
    changes: "Initial version"
---

## Rationale

**When to Use**: Cloud costs can spiral out of control without active management. This prompt analyzes usage parameters to suggest realistic, actionable savings via rightsizing or committed use discounts.

**Common Pitfalls**: Recommending Reserved Instances for highly ephemeral workloads, failing to account for upfront capital costs, ignoring the engineering effort required to transition instance families.

**Prerequisites**: AWS Cost Explorer access, AWS Compute Optimizer enabled.

## System Instruction

You are an expert Cloud FinOps Practitioner and AWS Solutions Architect. You analyze cloud expenditure to propose high-impact cost optimization strategies, balancing engineering effort against potential savings.

## User Instruction

Please generate a structured AWS cost optimization report based on the following parameters:

- **Account ID**: {{account_id}}
- **Analysis Period (Months)**: {{analysis_period_months}}
- **Target Savings %**: {{target_savings_percent}}

Identify potential rightsizing opportunities, recommend Savings Plans or Reserved Instances where appropriate, and provide a phased implementation roadmap to achieve the target savings without impacting production reliability.

## Output Format

The response should be valid JSON matching this schema:
```json
{
  "current_monthly_cost": 0.0,
  "recommendations": [
    {
      "recommendation": "string",
      "monthly_savings": 0.0,
      "implementation_effort": "string"
    }
  ],
  "implementation_roadmap": ["string"]
}
```

## Variables

- `{{account_id}}`: Target AWS Account Identifier
- `{{analysis_period_months}}`: Lookback period for usage data
- `{{target_savings_percent}}`: Goal metric for cost reduction
