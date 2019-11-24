#!/usr/bin/env python

import io
import re
import os
from setuptools import setup, find_packages


def read(*filenames, **kwargs):
    encoding = kwargs.get("encoding", "utf-8")
    sep = kwargs.get("sep", os.linesep)
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


def read_requirements(req="base.txt"):
    content = read(os.path.join("requirements", req))
    return [line for line in content.split(os.linesep) if not line.strip().startswith("#")]


def read_version():
    content = read(os.path.join(os.path.dirname(__file__), "pcskcli", "__init__.py"))
    return re.search(r"__version__ = \"([^']+)\"", content).group(1)

setup(
    name="pcsk",
    version=read_version(),
    description="Python CLI Starter Kit",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="wingkwong",
    author_email="wingkwong.code@gmail.com",
    url="https://github.com/wingkwong/pcsk",
    license="MIT",
    packages=find_packages(exclude=["tests.*", "tests"]),
    keywords="pcsk",
    # Support Python 3.6 or greater
    python_requires=">=3.6, <=4.0, !=4.0",
    entry_points={"console_scripts": ["{}=pcskcli.cli.main:cli".format("pcskcli")]},
    install_requires=read_requirements("base.txt"),
    extras_require={"dev": read_requirements("dev.txt")},
    include_package_data=True,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: MIT",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Utilities",
    ],
)