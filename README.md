# AI DevOps Cloud Prompts

A **canonical, versioned library** of high‑quality AI prompts for DevOps, Cloud (AWS, Azure, GCP, Oracle Cloud), FinOps, SRE, Security, and Platform Engineering.

Designed to accelerate infrastructure automation, troubleshooting, cost optimisation, and secure operations using large language models. Each prompt includes metadata, variables, sample I/O, and a JSON Schema so you can validate LLM outputs automatically.

## Quickstart

```bash
git clone https://github.com/your-org/ai-devops-cloud-prompts.git
cd ai-devops-cloud-prompts

# Install test harness dependencies
pip install -r tools/test_harness/requirements.txt

# Validate a single prompt
python tools/test_harness/runner.py --prompt prompts/k8s/pod_disruption_budget.md

# Validate all prompts
python tools/test_harness/runner.py --dir prompts/
```

## Repository structure

```
.
├── prompts/
│   ├── general/
│   ├── providers/{aws,azure,gcp,oracle}/
│   ├── finops/
│   ├── k8s/
│   ├── ci-cd/
│   ├── observability/
│   ├── security/
│   ├── sre/
│   ├── migration/
│   ├── automation/
│   └── templates/         # Canonical prompt template & metadata schema
├── examples/
│   └── seed_prompts.md    # 30 fully‑fleshed prompt examples
├── tools/
│   └── test_harness/runner.py
├── docs/
│   ├── prompt_engineering.md
│   └── usage.md
├── .github/
│   ├── workflows/ci.yml
│   ├── ISSUE_TEMPLATE.md
│   └── PULL_REQUEST_TEMPLATE.md
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── CODE_OF_CONDUCT.md
└── CHANGELOG.md
```

## Example prompt (AWS least‑privilege IAM policy)

```yaml
---
title: "Generate least‑privilege IAM policy for an S3 bucket"
id: aws-iam-least-privilege-s3
intent: "Create a secure IAM policy that grants minimal required permissions."
difficulty: intermediate
provider: aws
variables:
  bucket_name:
    type: string
    example: my-app-data
  actions:
    type: list
    example: ["s3:GetObject", "s3:PutObject"]
expected_output_schema:
  type: object
  properties:
    policy_name:
      type: string
    policy_json:
      type: object
  required: ["policy_name", "policy_json"]
sample_input:
  bucket_name: my-app-data
  actions: ["s3:GetObject", "s3:PutObject"]
sample_output:
  policy_name: s3-least-privilege-my-app-data
  policy_json:
    Version: "2012-10-17"
    Statement:
      - Effect: "Allow"
        Action: ["s3:GetObject", "s3:PutObject"]
        Resource: "arn:aws:s3:::my-app-data/*"
rationale: "Use when granting access to S3 objects. Prefer least‑privilege to avoid data leaks."
---
```

The prompt body tells the LLM to produce valid JSON matching the schema.

## Adding your own prompts

1. Copy `templates/prompt_template.md` to the appropriate category folder.
2. Fill in the YAML front matter and prompt body with `{{variable}}` placeholders.
3. Run the test harness to validate.
4. Open a pull request following `CONTRIBUTING.md`.

## License

Apache 2.0 – see `LICENSE`.
