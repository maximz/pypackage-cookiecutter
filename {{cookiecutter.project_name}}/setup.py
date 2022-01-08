#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

setup(
    author="{{ cookiecutter.author.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.email }}",
    name="{{ cookiecutter.package_name }}",
    description="{{ cookiecutter.friendly_name }}",
    packages=find_packages(include=["{{ cookiecutter.package_name }}", "{{ cookiecutter.package_name }}.*"]),
    python_requires=">=3.7",
    version="{{ cookiecutter.version }}",
)
