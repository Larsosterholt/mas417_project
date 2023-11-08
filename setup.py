# setup.py
from setuptools import setup, find_packages

setup(
    name='nameTagLib',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'scipy',
        'cadquery',
    ],
)
# generere bibliotek:  i terminal: " python setup.py sdist ".
# ikke legg til standard bibliotek i install_requirements
