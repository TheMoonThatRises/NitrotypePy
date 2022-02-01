from setuptools import setup, find_packages

setup(name='NitrotypePy',
    version='0.0.1',
    description='A way to access nitrotype\'s unoffical api',
    author='The Moon That Rises',
    url='https://www.github.com/RangerEmerald/NitrotypePy',
    packages = find_packages(),
    install_requires = [
        'cloudscraper >= 1.2.58',
    ],
)
