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
export GITHUB_USER="maximz" # swap in username
export GITHUB_REPO="projectname" # swap in projectname

# Optional: set up a pyenv virtualenv
pyenv virtualenv 3.9 "$GITHUB_REPO-3.9"
echo "$GITHUB_REPO-3.9" > .python-version
pyenv version

# Install requirements
pip install --upgrade pip wheel
pip install -r requirements_dev.txt

pip install -e .
git init
pre-commit install
make lint
make test

git add .
git commit -m "Initial commit"
gh repo create "$GITHUB_REPO" --private --source=. --remote=origin # swap in projectname
git push -u origin master
git checkout -b develop
git push origin develop
gh repo view --web
```

Follow instructions in the generated repo for development setup.

Manual setup:

- Github main settings: Always suggest updating pull request branches; Allow auto-merge; Automatically delete head branches; Limit how many branches and tags can be updated in a single push (1).
    - Deselect: Allow squash merging; allow rebase merging.
- Enable Dependabot security updates

Next, if publishing docs (i.e. if docs CI job is enabled), create Netlify sites through CLI. Run this twice to create both a dev and a prod Netlify site. The dev one should be in a sandboxed dev account because its token will be available to Dependabot-triggered PRs. (The manual alternative: Create each with <https://app.netlify.com/drop>: manual deploy the landing page demo. Or if created by linking to a Git repo, turn off automatic builds in Netlify settings.)

```bash
# https://cli.netlify.com/getting-started
npm install netlify-cli -g

# https://cli.netlify.com/commands/sites#sitescreate
tmpdir=$(mktemp -d)
pushd $tmpdir
# mkdir blank
# cd blank

# These are account slugs from Team Settings:
netlify login # or `netlify switch` to switch accounts, `netlify status` to check authentication

# Dev account: maxim-sandboxdev
netlify switch
netlify status
netlify sites:create --disable-linking --debug --account-slug "maxim-sandboxdev" --name "$GITHUB_REPO-dev"

# Prod account: maximz
netlify switch
netlify status
netlify sites:create --disable-linking --debug --account-slug "maximz" --name "$GITHUB_REPO"

# Write down the site IDs

popd
rm -r "$tmpdir"
```

Manual step: Configure DNS for the prod site at Cloudflare. Point the CNAME to `echo "$GITHUB_REPO.netlify.app"`

Then add the custom domain in Netlify settings:

```bash
chrome "https://app.netlify.com/sites/$GITHUB_REPO/domain-management"
```

Automated Github setup:

```bash
# indented by one space to not save the secrets in shell history
 export DEV_NETLIFY_SITE_ID="TODO" # from above
 export PROD_NETLIFY_SITE_ID="TODO" # from above
 export NETLIFY_DEV_AUTH_TOKEN="TODO" # from password manager
 export NETLIFY_PROD_AUTH_TOKEN="TODO"  # from password manager
 export PYPI_API_TOKEN="TODO" # start with global account token, then rotate to project-specific token
# TODO: Replace pypi tokens with https://til.simonwillison.net/pypi/pypi-releases-from-github

# create "production" environment
# https://github.com/cli/cli/issues/5149#issuecomment-1523463635
# https://docs.github.com/en/rest/deployments/environments
echo '{"deployment_branch_policy": {"protected_branches":false,"custom_branch_policies":true}}' | gh api --method PUT -H "Accept: application/vnd.github+json" "repos/$GITHUB_USER/$GITHUB_REPO/environments/production" --input -


# https://docs.github.com/en/rest/deployments/branch-policies?apiVersion=2022-11-28
gh api --method POST -H "Accept: application/vnd.github+json" "repos/$GITHUB_USER/$GITHUB_REPO/environments/production/deployment-branch-policies" -f 'name=master'

gh secret set DEV_NETLIFY_SITE_ID --app actions --body "$DEV_NETLIFY_SITE_ID"
gh secret set NETLIFY_DEV_AUTH_TOKEN --app actions --body "$NETLIFY_DEV_AUTH_TOKEN"

gh secret set PYPI_API_TOKEN --app actions --body "$PYPI_API_TOKEN" --env production
gh secret set PROD_NETLIFY_SITE_ID --app actions --body "$PROD_NETLIFY_SITE_ID" --env production
gh secret set NETLIFY_PROD_AUTH_TOKEN --app actions --body "$NETLIFY_PROD_AUTH_TOKEN" --env production

gh secret set DEV_NETLIFY_SITE_ID --app dependabot --body "$DEV_NETLIFY_SITE_ID"
gh secret set NETLIFY_DEV_AUTH_TOKEN --app dependabot --body "$NETLIFY_DEV_AUTH_TOKEN"

jq -n '{"name": "tag delete protections", "target": "tag", "enforcement": "active", "conditions": {"ref_name": {"exclude": [], "include": ["refs/tags/v*"]}}, "rules": [{"type": "update"},{"type": "deletion"}], "bypass_actors": [{"actor_id": 5,"actor_type": "RepositoryRole","bypass_mode": "always"},{"actor_id": 1,"actor_type": "OrganizationAdmin","bypass_mode": "always"}]}' | gh api --method POST -H "Accept: application/vnd.github+json" "repos/$GITHUB_USER/$GITHUB_REPO/rulesets" --input -;

# Don't add this prevent-tag-creation rule unless we find a way to allow bypass for Github Actions
# jq -n '{"name": "tag create protections", "target": "tag", "enforcement": "active", "conditions": {"ref_name": {"exclude": [], "include": ["refs/tags/v*"]}}, "rules": [{"type": "creation"},{"type": "update"}], "bypass_actors": [{"actor_id": 5,"actor_type": "RepositoryRole","bypass_mode": "always"},{"actor_id": 1,"actor_type": "OrganizationAdmin","bypass_mode": "always"}]}' | gh api --method POST -H "Accept: application/vnd.github+json" "repos/$GITHUB_USER/$GITHUB_REPO/rulesets" --input -;

##

{
jq . <<HERE
{
  "name": "develop branch rule",
  "target": "branch",
  "enforcement": "active",
  "conditions": {
    "ref_name": {
      "exclude": [],
      "include": [
        "refs/heads/develop"
      ]
    }
  },
  "rules": [
    {
      "type": "deletion"
    },
    {
      "type": "pull_request",
      "parameters": {
        "required_approving_review_count": 0,
        "dismiss_stale_reviews_on_push": false,
        "require_code_owner_review": false,
        "require_last_push_approval": false,
        "required_review_thread_resolution": false
      }
    },
    {
      "type": "required_status_checks",
      "parameters": {
        "strict_required_status_checks_policy": false,
        "required_status_checks": [
          {
            "context": "tests (3.9)",
            "integration_id": 15368
          }
        ]
      }
    }
  ],
  "bypass_actors": [
    {
      "actor_id": 2,
      "actor_type": "RepositoryRole",
      "bypass_mode": "always"
    },
    {
      "actor_id": 5,
      "actor_type": "RepositoryRole",
      "bypass_mode": "always"
    }
  ]
}
HERE
} | gh api --method POST -H "Accept: application/vnd.github+json" "repos/$GITHUB_USER/$GITHUB_REPO/rulesets" --input -;

##

{
jq . <<HERE
{
  "name": "master branch rule",
  "target": "branch",
  "enforcement": "active",
  "conditions": {
    "ref_name": {
      "exclude": [],
      "include": [
        "refs/heads/master"
      ]
    }
  },
  "rules": [
    {
      "type": "deletion"
    },
    {
      "type": "non_fast_forward"
    },
    {
      "type": "pull_request",
      "parameters": {
        "required_approving_review_count": 0,
        "dismiss_stale_reviews_on_push": false,
        "require_code_owner_review": false,
        "require_last_push_approval": false,
        "required_review_thread_resolution": false
      }
    },
    {
      "type": "required_status_checks",
      "parameters": {
        "strict_required_status_checks_policy": false,
        "required_status_checks": [
          {
            "context": "tests (3.9)",
            "integration_id": 15368
          }
        ]
      }
    }
  ],
  "bypass_actors": [
    {
      "actor_id": 2,
      "actor_type": "RepositoryRole",
      "bypass_mode": "always"
    },
    {
      "actor_id": 5,
      "actor_type": "RepositoryRole",
      "bypass_mode": "always"
    }
  ]
}
HERE
} | gh api --method POST -H "Accept: application/vnd.github+json" "repos/$GITHUB_USER/$GITHUB_REPO/rulesets" --input -;
```

What these did:

- Add Github branch protection rules for `master` and `develop`: require PR before merging; require status checks to pass before merging (add "tests" check); requires branches to be up to date before merging (master only); allow force push (develop only).
- Add Github tag protection rule: `v*`
- Add Github Actions secrets:
    - `NETLIFY_DEV_AUTH_TOKEN` (Netlify user settings for sandbox account --> personal access tokens)
    - `DEV_NETLIFY_SITE_ID` (API ID from Netlify sandbox site settings)
- Dependabot secrets: add only `NETLIFY_DEV_AUTH_TOKEN` and `DEV_NETLIFY_SITE_ID`. Dependabot can't read the main repo secrets.
- Create Github environment called "production" that only can be used by `master` branch. Add secrets:
    - Set `PYPI_API_TOKEN` to an all-access user token for first push to PyPI. Once the project is live, generate a project-specific token, switch to it, and rotate the user token.
    - `NETLIFY_PROD_AUTH_TOKEN` (Netlify user settings for prod account --> personal access tokens)
    - `PROD_NETLIFY_SITE_ID` (API ID from Netlify prod site settings)

## Development of the cookiecutter project

```bash
pre-commit install
make lint
```

Note that symlinks in the generated project's `docs/` folder are created by a post-generate hook in `hooks/`.

For long blocks with templated braces that shouldn't involve Cookiecutter -- e.g. the inner CI yaml -- wrap with `{% raw -%}` and `{%- endraw %}`.

## Thanks

With inspiration from https://github.com/audreyfeldroy/cookiecutter-pypackage and https://github.com/cjolowicz/cookiecutter-hypermodern-python
