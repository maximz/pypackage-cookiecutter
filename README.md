# Python package template (Cookiecutter)

This template for Python packages gives you:

* TODO

## Usage

To run this cookiecutter template:

```bash
pip install cookiecutter
cookiecutter gh:maximz/pypackage-cookiecutter
```

Navigate to the destination and initialize the repo:

```bash
cd generated-projected # swap in the right path

pip install -e .
pre-commit install
make lint
make test

git init
git add .
git commit -m "Initial commit"
gh repo create "projectname" --private --source=. --remote=origin # swap in projectname
git push -u origin master

git checkout -b develop
git push origin develop
```

Follow instructions in the generated repo for development setup.

Other setup:

- Github main settings: Always suggest updating pull request branches; Allow auto-merge; Automatically delete head branches; Limit how many branches and tags can be updated in a single push (1).
    - Deselect: Allow squash merging; allow rebase merging.
- Add Github branch protection rules for `master` and `develop`: require PR before merging; require status checks to pass before merging (add "tests" check); requires branches to be up to date before merging (master only); allow force push (develop only).
- Add Github tag protection rule: `v*`
- Enable Dependabot security updates
- Create a dev and a prod Netlify site. The dev one should be in a sandboxed dev account because its token will be available to Dependabot-triggered PRs.
    - Create each with https://app.netlify.com/drop: manual deploy the landing page demo
    - Or if created by linking to a Git repo, turn off automatic builds in Netlify settings.
    - Configure DNS for the prod site. CNAME TODO, then Netlify settings -> Add custom domain.
- Add Github Actions secrets:
    - `NETLIFY_DEV_AUTH_TOKEN` (Netlify user settings for sandbox account --> personal access tokens)
    - `DEV_NETLIFY_SITE_ID` (API ID from Netlify sandbox site settings)
- Dependabot secrets: add only `NETLIFY_DEV_AUTH_TOKEN` and `DEV_NETLIFY_SITE_ID`. Dependabot can't read the main repo secrets.
- Create Github environment called "production" that only can be used by `master` branch. Add secrets:
    - Set `PYPI_API_TOKEN` to an all-access user token for first push to PyPI. Once the project is live, generate a project-specific token, switch to it, and rotate the user token.
    - `NETLIFY_PROD_AUTH_TOKEN` (Netlify user settings for prod account --> personal access tokens)
    - `PROD_NETLIFY_SITE_ID` (API ID from Netlify prod site settings)

Creating Netlify sites through CLI:

```bash
# https://cli.netlify.com/getting-started
npm install netlify-cli -g
netlify login # or `netlify switch` to switch accounts

# https://cli.netlify.com/commands/sites#sitescreate
mkdir blank
cd blank

netlify sites:create --disable-linking --debug
# then click enter twice

# or look up account slug in Team Settings and specify a name:
netlify sites:create --disable-linking --debug --account-slug "maximz" --name "projectname"
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
