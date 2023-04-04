# {{cookiecutter.friendly_name}}

[![](https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.package_name }})
[![CI](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repo_name}}/actions/workflows/ci.yaml/badge.svg?branch=master)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repo_name}}/actions/workflows/ci.yaml)
[![](https://img.shields.io/badge/docs-here-blue.svg)]({{ cookiecutter.docs_url }})
[![](https://img.shields.io/github/stars/{{cookiecutter.github_username}}/{{ cookiecutter.github_repo_name }}?style=social)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repo_name}})

## TODOs: Configuring this template

Create a Netlify site for your repository, then turn off automatic builds in Netlify settings.

Add these CI secrets: `PYPI_API_TOKEN`, `NETLIFY_AUTH_TOKEN` (Netlify user settings - personal access tokens), `DEV_NETLIFY_SITE_ID`, `PROD_NETLIFY_SITE_ID` (API ID from Netlify site settings)

Set up Codecov at TODO

## Overview

## Installation

```bash
pip install {{ cookiecutter.package_name }}
```

## Usage

## Development

Submit PRs against `develop` branch, then make a release pull request to `master`.

```bash
# Optional: set up a pyenv virtualenv
pyenv virtualenv 3.9 {{ cookiecutter.package_name }}-3.9
echo "{{ cookiecutter.package_name }}-3.9" > .python-version
pyenv version

# Install requirements
pip install --upgrade pip wheel
pip install -r requirements_dev.txt

# Install local package
pip install -e .

# Install pre-commit
pre-commit install

# Run tests
make test

# Run lint
make lint

# bump version before submitting a PR against master (all master commits are deployed)
bump2version patch # possible: major / minor / patch

# also ensure CHANGELOG.md updated
```
