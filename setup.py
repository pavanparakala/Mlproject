<<<<<<< HEAD
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Krish',
author_email='krishnaik06@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)
=======
from setuptools import find_packages, setup
from typing import List


Hypen_Dot_E = "-e ."


def get_requirement(file_path: str) -> List[str]:
    """this function will return the list of requirements"""
    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        [req.replace("\n", "") for req in requirement]

        if Hypen_Dot_E in requirement:
            requirement.remove(Hypen_Dot_E)
    return requirement


setup(
    name="mlproject",
    version="0.0.1",
    author="pavan",
    author_email="pavanchandparakala@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement("requirements.txt")

)
>>>>>>> da750f084812d708d8dab492566b451a5b1021dd
