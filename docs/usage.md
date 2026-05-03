# Usage Guide

## Running the Test Harness

```bash
pip install -r tools/test_harness/requirements.txt

# Validate all prompts
python tools/test_harness/runner.py --dir prompts/

# Validate a single prompt
python tools/test_harness/runner.py --prompt prompts/aws/s3_least_privilege.md
```

The harness extracts YAML front matter, injects `sample_input` into the prompt, calls a mock LLM that returns `sample_output`, and validates it against `expected_output_schema`.

## Adding New Prompts

1. Copy `templates/prompt_template.md` to the appropriate category folder.
2. Fill in front matter and prompt body using `{{variable}}` syntax.
3. Ensure `sample_output` is valid against your schema.
4. Run the test harness locally.
5. Open a pull request.

## Running CI Locally

You can simulate the CI workflow:

```bash
# Lint front matter
python -c "
import glob, yaml, sys
for f in glob.glob('prompts/**/*.md', recursive=True):
    with open(f) as fh:
        fm = yaml.safe_load(fh.read().split('---')[1])
    for k in ['id','title','intent']:
        assert k in fm, f'{f}: missing {k}'
print('Lint OK')
"

# Check secrets
grep -rE 'AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z\-_]{35}|password=|secret=' prompts/

# Build static catalog
python -m markdown -f catalog.html prompts/
```

## Generating the Static Catalog

```bash
python -c "
import markdown, glob, os
for md_file in glob.glob('prompts/**/*.md', recursive=True):
    html = markdown.markdown(open(md_file).read())
    out_path = 'catalog/' + md_file.replace('prompts/', '').replace('.md', '.html')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    open(out_path, 'w').write('<html><body>' + html + '</body></html>')
"
```
