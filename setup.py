from setuptools import setup,find_packages
from typing import List

PROJECT_NAME="Machine Learning Project"
VERSION="0.0.1"
DESCRIPTION="This is our machine learning project"
AUTHOR_NAME="Rohit Nyati"
AUTHOR_EMAIL="rohitnyati5@gmail.com"
REQUIREMENTS="requirements.txt"

def get_requirement_list()-> List[str]:
    Hypen_e_dot="-e ."
    with open(REQUIREMENTS) as file:
        requirements_list=file.readlines()
        requirements_list=[requirement_name.replace("\n","") for requirement_name in requirements_list]

        if Hypen_e_dot in requirements_list:
            requirements_list.remove(Hypen_e_dot)
        return requirements_list


setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=get_requirement_list()

)