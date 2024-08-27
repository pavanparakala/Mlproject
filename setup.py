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
