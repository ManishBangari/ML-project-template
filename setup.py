from setuptools import find_packages, setup
from typing import List

HYPEHN_DOT_E ='-e .' 

def get_requirements(file_path:str)->List[str]:
    '''
    This functions returns the list of all the requirements. 
    '''

    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]
    
    if HYPEHN_DOT_E in requirements:
        requirements.remove(HYPEHN_DOT_E)

    return requirements


setup(
    name="data-science project template",
    version='0.1',
    author="Manish Singh",
    author_email='manishbangari2108@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)