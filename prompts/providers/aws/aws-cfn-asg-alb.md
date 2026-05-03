---
title: "Create a CloudFormation template for an autoscaling group behind an ALB"
id: aws-cfn-asg-alb
intent: "Generate a complete CloudFormation YAML template."
difficulty: advanced
provider: aws
tags: [cloudformation, autoscaling]
variables:
  instance_type:
    type: string
    example: t3.micro
  min_size:
    type: number
    example: 2
  max_size:
    type: number
    example: 4
expected_output_schema:
  type: object
  properties:
    template_yaml: {type: string}
    key_resources: {type: array, items: {type: string}}
  required: [template_yaml, key_resources]
sample_input:
  instance_type: t3.micro
  min_size: 2
  max_size: 4
sample_output:
  template_yaml: "AWSTemplateFormatVersion: '2010-09-09'\nResources: ..."
  key_resources: [LaunchTemplate, AutoScalingGroup, ALB, TargetGroup]
rationale: "Use for scalable web apps. Ensure health checks are correctly configured."
---

[System]
Write a CloudFormation template that creates a launch template, autoscaling group, Application Load Balancer, and target group.

[User]
Instance type: {{instance_type}}, min size {{min_size}}, max size {{max_size}}.

[Output]
JSON with template_yaml and key_resources list.
