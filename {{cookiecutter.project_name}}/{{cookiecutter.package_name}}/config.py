import os

# Store global configuration here.

# Struct-like simplenamespace (https://dbader.org/blog/records-structs-and-data-transfer-objects-in-python)
from types import SimpleNamespace

# Configure file paths
paths = SimpleNamespace()
paths.data_dir = "data"
paths.output_dir = "out"
paths.models_dir = "data/models"

# convert all to absolute paths - consider the above relative to where this script lives, not where it's called from
for key, relative_path in paths.__dict__.items():
    # this would be relative to where config.py is imported from!
    # full_path = os.path.abspath(relative_path)

    # apply path relative to where config.py lives, not where it's imported from:
    dirname = os.path.dirname(__file__)
    # go one more level up
    dirname = os.path.dirname(dirname)
    paths.__dict__[key] = os.path.abspath(os.path.join(dirname, relative_path))


def make_dirs():
    """Create all necessary directories (except parquet directory), and necessary subdirectories in output folder, and all intermediate directories (like `mkdir -p`)"""
    dirs_to_make = paths.__dict__.values()
    for d in dirs_to_make:
        os.makedirs(d, exist_ok=True)
        print(d)
