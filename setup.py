from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''This function returns a list of requirements excluding '-e .' '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() != HYPEN_E_DOT]
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Monika',
    author_email='monikasekar9903@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
