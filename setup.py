from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path :str) ->List[str]:
    '''
    This function takes file path for the file requirements text file and read the file
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements






setup(
    name = 'ML_Project',
    version = '0.0.1',
    author = 'Piyush Chaudhari',
    author_email = 'piyushpchaudhari@gmail.com',
    packages = find_packages(),
    install_require = get_requirements('requirements.txt')
    )