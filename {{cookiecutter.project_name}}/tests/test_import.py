#!/usr/bin/env python

import pytest


def test_importability():
    from {{cookiecutter.package_name}} import config

    assert config.paths is not None
