#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="databridge",
    version="0",
    description="Data Bridge Schemas",
    packages=find_packages(),
    install_requires=["datajoint"],
)
