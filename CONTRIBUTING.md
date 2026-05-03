# Contributing to AI DevOps Cloud Prompts

Thanks for helping build a high‑quality prompt library!

## Prompt Style Guide

- Every prompt is a **single Markdown file** with YAML front matter.
- Front matter must include all required fields described in `templates/prompt_template.md`.
- Prompt body should contain:
  1. **System instruction** (optional but recommended).
  2. **User instruction** with `{{variable}}` placeholders.
  3. **Output format constraints** (JSON, YAML, or code block).
  4. **Validation hints** – what the LLM must check.

## Required Front Matter Fields

| Field | Type | Description |
|-------|------|-------------|
| `title` | string | Short, action‑oriented title |
| `id` | string | Unique slug (e.g., `aws-iam-least-privilege-s3`) |
| `intent` | string | One‑line description of the prompt’s purpose |
| `difficulty` | enum | `beginner`, `intermediate`, `advanced`, `professional`, `optimalistic`, `cost-efficient` |
| `tags` | array of strings | Keywords (max 6) |
| `provider` | string | `aws`, `azure`, `gcp`, `oracle`, `multi`, `general` |
| `variables` | map | Variable name → `{type, example}` |
| `expected_output_schema` | object | Valid JSON Schema for output |
| `sample_input` | object | Example values for variables |
| `sample_output` | object | Example output matching schema |
| `rationale` | string | When to use the prompt and common pitfalls |

## Review Checklist

- [ ] Prompt follows the template and style guide.
- [ ] YAML front matter is valid and all required fields present.
- [ ] `{{variable}}` placeholders match the `variables` map.
- [ ] `expected_output_schema` is a valid JSON Schema (check with `jsonschema`).
- [ ] `sample_output` passes validation against the schema.
- [ ] No secrets or credentials appear (CI will scan).
- [ ] Difficulty and tags are appropriate.
- [ ] Prompt has been tested with at least one LLM (note model in a comment).

## Maturity Labels

Add a comment in the front matter:

```yaml
# maturity: draft | reviewed | production
```

- **draft** – Work in progress, not yet reviewed.
- **reviewed** – Peer‑reviewed by at least one other contributor.
- **production** – Approved by two maintainers, ready for broad use.

Upgrading from `reviewed` to `production` requires **two approvals**.

## Pull Request Process

1. Branch from `main` with a descriptive name.
2. Add or modify prompts, following the checklist.
3. Run `python tools/test_harness/runner.py --dir prompts/` locally.
4. Open a PR using the pull request template.
5. CI must pass (linting, validation, secrets check).
6. Obtain approvals as per maturity rules.
