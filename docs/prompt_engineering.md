# Prompt Engineering Guide

## Adapting Prompts for Different LLMs

- **System messages**: Some providers (OpenAI, Anthropic) support a system message. Place the system instruction at the top of the prompt or use the API’s system role.
- **Temperature**: For deterministic outputs (e.g., JSON schema), set temperature to 0. For creative tasks, use 0.3‑0.7.
- **Max tokens**: Estimate output size based on expected schema; set max_tokens slightly higher.

## Prompt Tuning

- Iterate on the output format constraints until the LLM consistently returns valid JSON.
- Use few‑shot examples if needed (add one or two correct outputs in the prompt).
- Chain prompts for complex tasks: break into smaller, validated steps.

## Safety Checks

- Always validate LLM output against the JSON Schema before using it in automation.
- Scan output for injection patterns before executing generated code.
- Use the test harness as a gate in CI.

## Crafting Output Constraints

- Be explicit: “Return a single JSON object with exactly the following keys.”
- Avoid natural language descriptions if the schema can be expressed in JSON.
- Use `additionalProperties: false` to prevent hallucinations.
