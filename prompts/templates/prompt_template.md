---
title: "Prompt Title (e.g., Generate least‑privilege IAM policy for S3 bucket)"
id: "unique-id-using-slug"
intent: "Brief description of what the prompt helps achieve"
difficulty: "beginner|intermediate|advanced|professional|optimalistic|cost-efficient"
tags: ["tag1", "tag2"]
provider: "aws|azure|gcp|oracle|agnostic"
variables:
  - name: "variable_name"
    type: "string|number|boolean|list|object"
    description: "What this variable represents"
    example: "example-value"
  - name: "another_var"
    type: "string"
    description: "Description of another variable"
    example: "us-east-1"
expected_output_schema:
  type: "object"
  properties:
    output_field:
      type: "string"
      description: "Explanation"
  required: ["output_field"]
sample_input:
  variable_name: "example-value"
  another_var: "us-east-1"
sample_output:
  output_field: "result"
# maturity: draft
---

[System Instruction]
You are an expert cloud engineer and prompt assistant. Always produce output that strictly adheres to the specified JSON schema. Do not include extra commentary outside the structured output.

[User Instruction]
Given the following inputs:
- Variable1: `{{variable_name}}`
- Variable2: `{{another_var}}`

Perform the task: <describe action>.

[Output Format]
Return a single JSON object that matches the schema below:
```json
{
  "output_field": "<result>"
}
```

[Validation Hints]
- Ensure that `output_field` is ...
- Validate against the defined JSON Schema.

[Common Pitfalls]
- Watch out for ...
