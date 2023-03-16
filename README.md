# Python package template (Cookiecutter)

This template for Python packages gives you:

* TODO

## Usage

To run this cookiecutter template:

```bash
pip install cookiecutter
cookiecutter gh:maximz/pypackage-cookiecutter
```

## Development of the cookiecutter project

```bash
pre-commit install
make lint
```

Note that symlinks in the generated project's `docs/` folder are created by a post-generate hook in `hooks/`.

For long blocks with templated braces that shouldn't involve Cookiecutter -- e.g. the inner CI yaml -- wrap with `{% raw -%}` and `{%- endraw %}`.

## Thanks

With inspiration from https://github.com/audreyfeldroy/cookiecutter-pypackage and https://github.com/cjolowicz/cookiecutter-hypermodern-python
