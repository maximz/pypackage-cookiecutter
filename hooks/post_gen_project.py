# Cookiecutter doesn't support symlinks. We create docs symlinks ourselves as a post-generate hook.

import os

# Symlinks must be relative to the destination
os.symlink("../README.md", "docs/index.md")
os.symlink("../CHANGELOG.md", "docs/changelog.md")
