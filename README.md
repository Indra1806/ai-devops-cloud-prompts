# AI DevOps & Cloud Prompts

[![CI/CD](https://github.com/Indra1806/ai-devops-cloud-prompts/actions/workflows/ci.yml/badge.svg)](https://github.com/Indra1806/ai-devops-cloud-prompts/actions)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Prompts](https://img.shields.io/badge/Prompts-150%2B-brightgreen)](.)

A production-grade library of AI prompts for DevOps, Cloud Engineering, FinOps, SRE, and Platform Engineering. Each prompt is versioned, documented, tested, and tagged by difficulty, provider, and use case.

## Overview

- **150+ prompts** across AWS, Azure, GCP, and Oracle Cloud
- **Organized by domain**: Kubernetes, CI/CD, Observability, Security, FinOps, SRE, Migration, Automation
- **Structured format** with YAML metadata, variable schemas, and expected outputs
- **Validated & tested** via CI/CD pipeline with JSON Schema validation
- **Governance model** with maturity labels (draft, reviewed, production)
- **Best practices** documentation for prompt tuning and LLM adaptation

## Quick Start

### Using a Prompt

1. Browse prompts by category: `prompts/providers/aws/`, `prompts/k8s/`, etc.
2. Each prompt is a `.md` file with YAML front matter:
   ```yaml
   ---
   title: "Design a VPC with Private Subnets"
   id: aws-vpc-private-001
   intent: "Generate Terraform module for secure VPC architecture"
   difficulty: intermediate
   provider: aws
   tags: [terraform, networking, security]
   variables:
     vpc_cidr: { type: "string", example: "10.0.0.0/16" }
   expected_output_schema: { ... }
   ---
   ```
3. Copy the prompt, fill in variables, and send to your LLM.

### Adding a Prompt

1. Create a new `.md` file in the appropriate `prompts/` folder.
2. Use the canonical template: `prompts/templates/prompt_template.md`
3. Validate metadata with: `tools/test_harness/runner.py --validate <file>`
4. Submit a PR and wait for two approvals before merging to production.

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

### Running Tests

```bash
cd tools/test_harness
python runner.py --harness sample
```

This validates 10 sample prompts against expected output schemas.

## Prompt Structure

Each prompt includes:
- **Metadata**: title, id, intent, difficulty, provider, tags
- **Variables**: typed placeholders (string, number, array, object)
- **Instructions**: system and user prompts with explicit output format
- **Schema**: JSON Schema for validating LLM response
- **Example**: sample input and output
- **Rationale**: when to use and common pitfalls

## Repository Layout

```
ai-devops-cloud-prompts/
├── README.md                           # This file
├── CONTRIBUTING.md                     # Style guide & governance
├── docs/
│   ├── prompt_engineering.md           # LLM tuning, temperature, tokens
│   ├── usage.md                        # How to run tests & add prompts
│   └── style_guide.md                  # Voice, tone, formatting
├── prompts/
│   ├── general/                        # Onboarding, runbooks
│   ├── providers/
│   │   ├── aws/                        # 15-25 AWS prompts
│   │   ├── azure/                      # 15-25 Azure prompts
│   │   ├── gcp/                        # 15-25 GCP prompts
│   │   └── oracle/                     # 15-25 Oracle prompts
│   ├── k8s/                            # 20 Kubernetes prompts
│   ├── ci-cd/                          # 20 CI/CD prompts
│   ├── observability/                  # 15 Observability prompts
│   ├── security/                       # 15 Security prompts
│   ├── finops/                         # 15 FinOps prompts
│   ├── sre/                            # 10 SRE/runbook prompts
│   ├── automation/                     # 10 Automation prompts
│   ├── migration/                      # 10 Migration prompts
│   └── templates/                      # Canonical prompt template
├── examples/
│   ├── seed_prompts.md                 # 20 fully-fleshed examples
│   └── expected_outputs/               # Sample LLM responses
├── tools/
│   └── test_harness/
│       ├── runner.py                   # Validates prompts
│       └── requirements.txt            # Dependencies
└── .github/
    └── workflows/
        └── ci.yml                      # Lint, test, catalog build
```

## Categories & Examples

### Cloud Providers
- **AWS** (20 prompts): VPC design, IAM policies, RDS patterns, S3 lifecycle, cost estimation, Terraform modules
- **Azure** (20 prompts): Virtual networks, managed identities, App Service, AKS, Bicep templates, cost optimization
- **GCP** (20 prompts): VPC peering, IAM bindings, Pub/Sub, GKE, Terraform modules, billing insights
- **Oracle** (15 prompts): OCI compartments, VCN design, OKE, budget alerts, Terraform modules

### Cross-Cutting
- **Kubernetes** (20): Pod manifests, Helm charts, security policies, scaling strategies, troubleshooting
- **CI/CD** (20): GitHub Actions, GitLab CI, Jenkins, canary deployments, rollback strategies
- **Observability** (15): Prometheus rules, Grafana dashboards, tracing setup, SLO definition
- **Security** (15): Threat models, secret scanning, network policies, hardening checklist
- **FinOps** (15): Cost reports, rightsizing, RI/SA analysis, tagging standards
- **SRE** (10): SLO/SLI design, incident runbooks, postmortem templates
- **Automation** (10): Infrastructure code, script generation, safe change patterns
- **Migration** (10): Rehost strategies, data migration, DNS cutover, rollback plans

## Maturity Levels

All prompts are labeled with maturity:
- **Draft**: Experimental, untested in production
- **Reviewed**: Peer-reviewed, validated with sample outputs
- **Production**: Battle-tested, two approvals required

## Contributing

Contributions are welcome! Please:
1. Fork and create a feature branch
2. Follow the prompt template and style guide (see [CONTRIBUTING.md](CONTRIBUTING.md))
3. Add metadata, examples, and rationale
4. Run `tools/test_harness/runner.py --validate <file>` locally
5. Submit a PR with a clear description

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## Governance

- **Prompt Review**: Two approvals required for production prompts
- **Testing**: All prompts validated against JSON Schema
- **Versioning**: Semantic versioning (major.minor.patch) for breaking changes
- **Deprecation**: Old prompts marked with `deprecated: true` and moved to `legacy/`

## Documentation

- [Prompt Engineering Guide](docs/prompt_engineering.md): LLM tuning, temperature, system messages, safety
- [Usage Guide](docs/usage.md): Running tests, adding prompts, local setup
- [Style Guide](docs/style_guide.md): Voice, tone, formatting conventions

## CI/CD

Every PR runs:
1. **Lint**: YAML front matter, Markdown formatting, no secrets
2. **Test**: JSON Schema validation on sample prompts
3. **Catalog**: Generates static HTML catalog of all prompts

See [.github/workflows/ci.yml](.github/workflows/ci.yml) for details.

## Roadmap

- [ ] Add 50+ more prompts (Q2 2024)
- [ ] Support for Claude API structured outputs
- [ ] Interactive prompt builder web UI
- [ ] Telemetry for prompt performance tracking
- [ ] Provider workshops & video tutorials

## License

Licensed under Apache License 2.0. See [LICENSE](LICENSE) for terms.

## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). We foster an inclusive, respectful community.

## Questions?

- File an issue: [New Prompt Issue Template](.github/ISSUE_TEMPLATE/new_prompt.md)
- See [Discussions](../../discussions) for community Q&A
- Check [docs/](docs/) for detailed guides

---

**Last Updated**: 2024-01-15 | **Prompts**: 150+ | **Providers**: 4 | **Maturity**: Production
