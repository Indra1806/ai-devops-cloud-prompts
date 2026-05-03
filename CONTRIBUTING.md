# Contributing to AI DevOps Cloud Prompts

Thank you for helping build a high‑quality prompt library! This document outlines the workflow, style guide, and review process.

## Prompt Style Guide

- Every prompt lives in a **single Markdown file** with YAML front matter.
- The front matter must include all required fields (see template below).
- Prompt body should contain:
  1. **System instruction** (optional but recommended).
  2. **User instruction** with placeholders `{{variable_name}}`.
  3. **Output format constraints** (JSON, YAML, code block).
  4. **Validation hints** – what the LLM must check.

### Required front matter fields

| Field | Type | Description |
|-------|------|-------------|
| `title` | string | Short, action‑oriented title |
| `id` | string | Unique slug (e.g. `aws-iam-least-privilege-s3`) |
| `intent` | string | One‑line description of the prompt’s purpose |
| `difficulty` | enum | `beginner`, `intermediate`, `advanced`, `professional`, `optimalistic`, `cost-efficient` |
| `tags` | list of strings | Keywords helping search (max 6) |
| `provider` | string | `aws`, `azure`, `gcp`, `oracle`, or `agnostic` |
| `variables` | list of objects | Each with `name`, `type`, `description`, `example` |
| `expected_output_schema` | object | A valid JSON Schema describing the expected LLM output |
| `sample_input` | object | Key‑value pairs filled with example variable values |
| `sample_output` | object | An example output that conforms to the schema |

## Review Checklist

Before submitting a pull request:

- [ ] Prompt follows the template from `prompts/templates/prompt_template.md`.
- [ ] YAML front matter is valid and all required fields present.
- [ ] Variables are used in the prompt body with `{{name}}` placeholders.
- [ ] `expected_output_schema` is a valid JSON Schema (validate with `jsonschema`).
- [ ] `sample_output` validates against the schema.
- [ ] No secrets, credentials, or proprietary information.
- [ ] Difficulty and tags are appropriate.
- [ ] Prompt has been tested with at least one LLM (note the model in a comment).

## Maturity Labels

Every prompt carries a maturity label in a comment at the bottom of the front matter:

```yaml
# maturity: draft | reviewed | production
```

- **draft** – Work in progress, not yet reviewed.
- **reviewed** – Peer‑reviewed by at least one other contributor.
- **production** – Approved by two maintainers, ready for broad use.

Upgrading from `reviewed` to `production` requires **two approvals** and passing the automated schema validation.

## Adding a New Prompt

1. Create a new `.md` file in the appropriate category folder.
2. Copy the canonical template from `prompts/templates/prompt_template.md`.
3. Fill in front matter and prompt body.
4. Run the test harness locally:
   ```bash
   python tools/test_harness/runner.py --prompt your-file.md
   ```
5. Submit a pull request. The CI will lint and validate automatically.

## Pull Request Process

- Branch from `main` with a descriptive name.
- Add a changelog entry in `CHANGELOG.md`.
- Ensure all checks pass (GitHub Actions).
- Request review from a maintainer.

## Code of Conduct

This project adheres to the [Contributor Covenant](CODE_OF_CONDUCT.md).
