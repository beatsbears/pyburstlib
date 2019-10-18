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
        'attrs==17.4.0',
        'certifi==2018.1.18',
        'cffi==1.11.5',
        'chardet==3.0.4',
        'idna==2.6',
        'pluggy==0.6.0',
        'py==1.5.2',
        'pycparser==2.18',
        'PyNaCl==1.2.1',
        'pytest==3.4.2',
        'requests>=2.20.0',
        'six==1.11.0',
        'urllib3==1.24.2'
    ],
    keywords='burst burstcoin pocc',
    python_requires='>=3.3'
)