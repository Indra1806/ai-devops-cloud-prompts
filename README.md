# AI DevOps Cloud Prompts

![License](https://img.shields.io/badge/license-Apache%202.0-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen)

A **canonical, versioned library** of high‑quality AI prompts for **DevOps, Cloud (AWS, Azure, GCP, Oracle Cloud), FinOps, SRE, Security, and Platform Engineering**. Designed to help engineers and prompt builders accelerate infrastructure automation, troubleshooting, cost optimisation, and secure operations using large language models.

## Why this repository?

- **Battle‑tested prompts** – ready to copy into your LLM chat or integration.
- **Metadata‑rich** – every prompt includes variables, difficulty, tags, provider, sample I/O, and a JSON Schema for output validation.
- **Provider‑agnostic with cloud‑specific variants** – covers AWS, Azure, GCP, and Oracle Cloud.
- **Maturity labels** – draft → reviewed → production, governed by a review process.
- **Tooling included** – test harness validates output shape, CI lints front matter and builds a static catalog.

## Quickstart

```bash
git clone https://github.com/Indra1806/ai-devops-cloud-prompts.git
cd ai-devops-cloud-prompts

# Validate a single prompt
python tools/test_harness/runner.py --prompt prompts/k8s/pod_disruption_budget.md

# Run the full test suite
python tools/test_harness/runner.py --dir prompts/
```

Browse prompts by category:
- `prompts/providers/aws/`
- `prompts/k8s/`
- `prompts/finops/`
- ...

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
│   └── templates/         # Prompt template & metadata schema
├── examples/
│   └── seed_prompts.md    # 20 fully‑fleshed sample prompts
├── tools/
│   └── test_harness/runner.py
├── docs/
│   ├── prompt_engineering.md
│   ├── usage.md
│   └── style_guide.md
├── .github/
│   ├── workflows/ci.yml
│   ├── ISSUE_TEMPLATE/
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
title: "Generate least-privilege IAM policy for an S3 bucket"
id: aws-iam-least-privilege-s3
intent: "Create a secure IAM policy that grants minimal required permissions."
difficulty: intermediate
provider: aws
variables:
  - name: bucket_name
    type: string
    description: "Name of the S3 bucket"
    example: "my-app-data"
  - name: actions
    type: list
    description: "Allowed S3 actions (e.g. GetObject, PutObject)"
    example: ["s3:GetObject", "s3:PutObject"]
expected_output_schema:
  type: object
  properties:
    policy_name:
      type: string
    policy_json:
      type: object
  required: ["policy_name", "policy_json"]
---
```

The prompt body gives the LLM clear instructions to produce valid JSON matching the schema.

## Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for the prompt style guide, review checklist, and maturity model.

## License

Apache 2.0 – see [LICENSE](LICENSE).
