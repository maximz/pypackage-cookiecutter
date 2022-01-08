# Data Science Starter Template (Cookiecutter)

This template for data science projects gives you:

* A directory for Python scripts, for refactoring logic out of your Jupyter notebooks. These are bundled together in a `pip install`-able package that you can import in your notebooks.
* A directory for Jupyter notebooks, with automatic mirroring/sync to Python scripts, so you can easily edit and diff your notebooks.
* Linting for your Python scripts and Jupyter notebooks.
* Automated tests and Github Actions CI.
* Helper scripts to run notebooks en-masse in a pipeline.

## Usage

To run this cookiecutter template:

```bash
pip install cookiecutter
cookiecutter gh:maximz/datascience-cookiecutter-starter
```

## Development of the cookiecutter project

```bash
pre-commit install
make lint
```

For long blocks with templated braces that shouldn't involve Cookiecutter -- e.g. the inner CI yaml -- wrap with `{% raw -%}` and `{%- endraw %}`.

## Thanks

With inspiration from https://github.com/audreyfeldroy/cookiecutter-pypackage and https://github.com/cjolowicz/cookiecutter-hypermodern-python
