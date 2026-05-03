# Canonical Prompt Template

Copy this file to the appropriate category folder (e.g., `prompts/k8s/`) and fill in the details.

```yaml
---
title: "Your prompt title (action-oriented)"
id: unique-slug-here
intent: "One-sentence description of what the prompt helps achieve"
difficulty: beginner  # beginner | intermediate | advanced | professional | optimalistic | cost-efficient
tags: [tag1, tag2]
provider: aws   # aws, azure, gcp, oracle, multi, general
variables:
  variable_name:
    type: string
    example: example-value
  another_var:
    type: number
    example: 42
expected_output_schema:
  type: object
  properties:
    result_key:
      type: string
  required: [result_key]
  additionalProperties: false
sample_input:
  variable_name: example-value
  another_var: 42
sample_output:
  result_key: expected value
rationale: "Use this prompt when ... Common pitfalls: ..."
# maturity: draft
---
```

## System Instruction

```
You are an expert DevOps and cloud engineer. Always return output strictly adhering to the specified JSON schema. Do not add any text outside the JSON.
```

## User Instruction

```
Given the following inputs:
- Var1: {{variable_name}}
- Var2: {{another_var}}

<Describe the exact task here>

Output format:
Return a single JSON object that matches this schema:
{
  "result_key": "<value>"
}
```

## Validation Hints

- Ensure `result_key` is ...
- Validate your output against the JSON Schema before returning.
