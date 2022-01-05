# -*- coding: utf-8 -*-

from __future__ import print_function

import sys

from setuptools import find_packages 

try:
    from skbuild import setup
except ImportError:
    print(
        "Please update pip, you need pip 10 or greater,\n"
        " or you need to install the PEP 518 requirements in pyproject.toml yourself",
        file=sys.stderr,
    )
    raise

setup(
    name="lora",
    version="0.0.1",
    description="a minimal example package to test cython in scikit-build",
    author="Jean-Mathieu Vermosen",
    license="MIT",
    packages=find_packages(where = 'lib'),
    package_dir={"": "lib"},
    cmake_install_dir="lib/lora",
    install_requires=['cython'],
    cmake_args=[],
    include_package_data = True,
    extras_require={"test": ["pytest"]},
)
