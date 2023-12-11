import io
from notifier.cli import entry
import os
import sys

from setuptools import Command, find_packages, setup

# import notifypy

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name="notifier.py",
    version="0.3.38",
    author="Juliandev02",
    description="A simple Python library that simplifies the sending of desktop notifications!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Strawberry-Foundations/notifier",
    python_requires=">=3.6.0",
    packages=find_packages(
        exclude=["testing", "*.testing", "*.testing.*", "testing.*", "tests"]
    ),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["notifier = notifier.cli:entry"]},
    include_package_data=True,
    install_requires=["loguru", "jeepney ; platform_system=='Linux'"],
)
