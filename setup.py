from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

about = {}
exec(open(path.join(here, 'pyburstlib/__init__.py')).read(), about)

with open(path.join(here, 'README.md')) as file:
    long_description = file.read()

setup(
    name='pyburstlib',
    version=about['__version__'],
    description='A python library for working with Burstcoin',
    long_description=long_description,
    author='drownedcoast',
    url='https://github.com/beatsbears/pyburstlib',
    packages=find_packages(exclude=['tests*']),
    license='MIT License',
    install_requires=[
        "requests>=2.12.1"
    ],
    keywords='burst burstcoin pocc',
    python_requires='>=3.3'
)