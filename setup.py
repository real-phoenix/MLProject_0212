## Why setup.py? 
## Build entire ML application as a package and deploy in PyPI (Python Package Index) for easy installation and distribution.

from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str)-> List[str]:
    '''
    This function will return the list of requirements mentioned in requirements.txt file
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n'", "") for req in requirements]
        if HYPHEN_E_DOT in requirements: 
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name='mlProject_0212', 
    version='0.0.1', 
    author='Shreya', 
    author_email='shreya.phoenix1.0@gmail.com', 
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)