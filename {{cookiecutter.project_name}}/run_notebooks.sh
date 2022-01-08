#!/bin/bash
# Run a set of notebooks
# Optionally set kernel with --set-kernel "kernel-name"
jupytext --sync --pipe black --execute "$@";
