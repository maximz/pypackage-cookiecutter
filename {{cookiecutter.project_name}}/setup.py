#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.md") as history_file:
    history = history_file.read()

requirements = ["Click>=7.0"]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="{{ cookiecutter.author.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.email }}",
    name="{{ cookiecutter.package_name }}",
    description="{{ cookiecutter.friendly_name }}",
    packages=find_packages(include=["{{ cookiecutter.package_name }}", "{{ cookiecutter.package_name }}.*"]),
    python_requires=">=3.8",
    version="{{ cookiecutter.version }}",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repo_name}}",
    zip_safe=False,
)
