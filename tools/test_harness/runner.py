#!/usr/bin/env python3
"""
Lightweight test harness for AI DevOps Cloud Prompts.
Parses YAML front matter, injects sample_input, calls a mock LLM,
and validates output against expected_output_schema.
"""

import argparse
import json
import sys
import os
from pathlib import Path

import yaml
from jsonschema import validate, ValidationError, SchemaError


def parse_front_matter(text):
    """Extract YAML front matter and body from Markdown text."""
    if not text.startswith('---'):
        return None, ''
    parts = text.split('---', 2)
    if len(parts) < 3:
        return None, ''
    fm = yaml.safe_load(parts[1])
    body = parts[2]
    return fm, body


def substitute_placeholders(template, variables):
    """Replace {{var}} with string representation of value."""
    result = template
    for k, v in variables.items():
        result = result.replace(f'{{{{{k}}}}}', str(v))
    return result


def mock_llm(prompt_text, expected_output):
    """
    Stub LLM that simply returns the expected_output.
    In a real scenario, this would call an actual model.
    """
    # Simulate some delay for realism (comment out if not wanted)
    return expected_output


def check_secrets(text):
    """Basic secret patterns; fails if found."""
    import re
    patterns = [
        r'AKIA[0-9A-Z]{16}',
        r'AIza[0-9A-Za-z\-_]{35}',
        r'password\s*=\s*[^\s]+',
        r'secret\s*=\s*[^\s]+',
    ]
    for pat in patterns:
        if re.search(pat, text):
            return False, f'Pattern detected: {pat}'
    return True, ''


def validate_prompt_file(filepath):
    """Run validation on a single prompt file. Returns (pass, message)."""
    try:
        content = Path(filepath).read_text(encoding='utf-8')
    except Exception as e:
        return False, f'Cannot read file: {e}'

    secret_ok, secret_msg = check_secrets(content)
    if not secret_ok:
        return False, f'SECURITY: {secret_msg}'

    fm, body = parse_front_matter(content)
    if fm is None:
        return False, 'No valid YAML front matter'

    required_keys = ['id', 'expected_output_schema', 'sample_input', 'sample_output']
    missing = [k for k in required_keys if k not in fm]
    if missing:
        return False, f'Missing front matter keys: {missing}'

    # Build the prompt with substitutions
    prompt = substitute_placeholders(body, fm['sample_input'])

    # Call mock LLM (returns sample_output)
    llm_output = mock_llm(prompt, fm['sample_output'])

    # Validate against schema
    schema = fm['expected_output_schema']
    try:
        validate(instance=llm_output, schema=schema)
        return True, 'PASS'
    except ValidationError as e:
        return False, f'Schema validation failed: {e.message}'
    except SchemaError as e:
        return False, f'Invalid JSON Schema: {e.message}'


def main():
    parser = argparse.ArgumentParser(description='Validate prompt files.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--prompt', help='Single prompt file to validate')
    group.add_argument('--dir', help='Directory of prompt files to validate (recursive)')
    args = parser.parse_args()

    if args.prompt:
        ok, msg = validate_prompt_file(args.prompt)
        print(f'{args.prompt}: {msg}')
        sys.exit(0 if ok else 1)
    elif args.dir:
        root = Path(args.dir)
        md_files = list(root.rglob('*.md'))
        if not md_files:
            print('No Markdown files found.')
            sys.exit(1)
        failed = []
        for f in sorted(md_files):
            ok, msg = validate_prompt_file(f)
            status = 'PASS' if ok else 'FAIL'
            print(f'{f}: {status} - {msg}')
            if not ok:
                failed.append(f)
        if failed:
            print(f'\n{len(failed)} file(s) failed.')
            sys.exit(1)
        else:
            print('\nAll prompts passed.')
            sys.exit(0)


if __name__ == '__main__':
    main()
