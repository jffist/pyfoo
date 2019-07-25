from setuptools import find_packages
from setuptools import setup

setup(
    name="pyfoo",
    version="0.3.1",
    license='Proprietary',
    packages=find_packages(exclude=('tests',)),
    install_requires=['numpy'],
    tests_require=['pytest','numpy.testing'],

    # scripts and entry points
    scripts=['scripts/foobar.py'],
    entry_points = {
        'console_scripts': ['barentry=pyfoo.foo:main']
    },
    # extended metadata
    url="https://github.com/jffist/pyfoo",
    author="Foo Man",
    author_email="foo@man.com",
    description="A minimalistic example of python package",
    long_description="Usually long description is stored in a Readme.rst",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.7',
    ],
)
