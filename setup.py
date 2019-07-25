from setuptools import find_packages
from setuptools import setup

setup(
    name="pyfoo",
    version="0.1.0",
    license='Proprietary',
    packages=find_packages(exclude=('tests',))
)
