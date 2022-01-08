# {{cookiecutter.friendly_name}}

## Project overview

## Installation

```bash
# Install requirements
pip install --upgrade pip wheel
pip install -r requirements.txt --src ../

# Install local package
pip install -e .

# Install pre-commit
pre-commit install

# Run tests
make test

# Run lint
make lint
```

Review `config.py` configuration. Create directories with: `python -c "from {{ cookiecutter.package_name }} import config; config.make_dirs();"`
## Runbook

```bash
# reset outputs
rm -r out
mkdir out

# run notebooks
./run_notebooks.sh \
    notebooks/analysis.ipynb \
    notebooks/summary.ipynb;
```

## Development

### Jupytext mirroring

Using jupytext, every `.ipynb` notebook in `notebooks/` has a paired `.py` script in `notebooks_src/`. This makes diffs much cleaner (nbdiff/nbdime is too slow and finnicky to be practical) and allows for bulk refactoring.

When you edit and save the `.ipynb` notebook in Jupyter Lab, Jupytext updates the `.py` paired script automatically. And when you edit the `.py` script in a text editor, reloading the paired `.ipynb` notebook in Jupyter Lab will sync the updates to the notebook.

Sometimes we fall back to the command line to sync these notebook/script pairs: after editing either element of the pair, you can `git add` it to the git staging area and then `make lint-staged` to run jupytext-sync (and other pre-commit hooks) on all staged files. We tend to do this after bulk refactors of `.py` scripts (`make lint-staged` will update the paired notebooks without having to open each one in Jupyter Lab) or after auto-generating notebooks from other template notebooks with `run_notebook_to_new_file.sh` (`make lint-staged` will then generate or update the paired script.)

### Common commands

```bash
# lint all files
make lint
# or lint staged files only - most frequently used
make lint-staged
# or lint files that have changed since upstream only
make lint-diff

# run all tests
make test

# recreate all jupytext generated scripts
make regen-jupytext
```
