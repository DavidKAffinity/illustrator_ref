# setup.py
from setuptools import setup, find_packages

setup(
    name="illustrator_ref",
    version="1.0",
    description="Illustrator 2026 COM Library Python Reference",
    author="David Kaufman",
    author_email="david.kaufman222@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.11",
    install_requires=[],
)