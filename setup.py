from setuptools import setup, find_namespace_packages
from io import open

with open("README.md", "r", encoding="utf-8") as fp:
    readme = fp.read()

setup(
    name="NitrotypePy",
    version="0.0.6",
    description="A way to access nitrotype's unofficial api.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="The Moon That Rises",
    url="https://www.github.com/RangerEmerald/NitrotypePy",
    license="MIT",
    packages=find_namespace_packages(include="NitrotypePy.*"),
    install_requires=[
        "cloudscraper >= 1.2.58",
    ],
)
