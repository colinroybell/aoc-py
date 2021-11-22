"""Minimal setup file for aoc project."""

from setuptools import setup, find_packages

setup(
    name="aoc-py",
    version="1.0.0",
    license="proprietary",
    description="Advent of Code",
    author="Colin Bell",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
