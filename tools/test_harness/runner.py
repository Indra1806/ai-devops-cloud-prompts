#!/usr/bin/env python3
"""
Lightweight test harness for AI DevOps Cloud Prompts.

Parses YAML front matter from prompt Markdown files,
validates expected_output_schema and sample_output using jsonschema.
"""

import argparse
import json
import sys
import os
import glob

import yaml  # PyYAML
from jsonschema import validate, ValidationError, SchemaError


def extract_front_matter(filepath: str):
    """Extract YAML front matter from a Markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if not content.startswith('---'):
        return None
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None
    yaml_text = parts[1]
    return yaml.safe_load(yaml_text)


def validate_prompt(filepath: str):
    """Validate a single prompt file. Returns (pass, message)."""
    meta = extract_front_matter(filepath)
    if not meta:
        return False, "No valid YAML front matter found."
    required_keys = ['id', 'expected_output_schema', 'sample_output']
    for key in required_keys:
        if key not in meta:
            return False, f"Missing required front matter key: {key}"
    schema = meta['expected_output_schema']
    sample_output = meta['sample_output']

    # Validate the JSON Schema itself
    try:
        from jsonschema import Draft7Validator
        Draft7Validator.check_schema(schema)
    except SchemaError as e:
        return False, f"Invalid JSON Schema: {e.message}"

    # Validate sample_output against the schema
    try:
        validate(instance=sample_output, schema=schema)
        return True, "PASS"
    except ValidationError as e:
        return False, f"Output validation failed: {e.message}"


def main():
    parser = argparse.ArgumentParser(description='Validate prompt files.')
    parser.add_argument('--prompt', help='Single prompt file to validate')
    parser.add_argument('--dir', help='Directory of prompt files to validate (recursive)')
    args = parser.parse_args()

    if args.prompt:
        success, msg = validate_prompt(args.prompt)
        print(f"{args.prompt}: {msg}")
        sys.exit(0 if success else 1)
    elif args.dir:
        md_files = glob.glob(os.path.join(args.dir, '**/*.md'), recursive=True)
        if not md_files:
            print("No Markdown files found.")
            sys.exit(1)
        failed = []
        for f in sorted(md_files):
            success, msg = validate_prompt(f)
            status = "PASS" if success else "FAIL"
            print(f"{f}: {status} - {msg}")
            if not success:
                failed.append(f)
        if failed:
            print(f"\n{len(failed)} file(s) failed validation.")
            sys.exit(1)
        else:
            print("\nAll prompt files passed validation.")
            sys.exit(0)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
