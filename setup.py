#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup

setup(
    name="utilities",
    version='0.3.1',
    description="Utilities for machine learning.",
    long_description="",
    classifiers=[],
    author="Martin Kozlovsky",
    packages=["own_utilities"],
    package_dir={"own_utilities": "."},
    setup_requires=["setuptools_scm"],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        "sklearn",
        "seaborn"
    ]
)
