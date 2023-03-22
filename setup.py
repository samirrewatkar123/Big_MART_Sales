from setuptools import find_packages,setup
from typing import List

hypen_minus_e='-e .'
def get_requirements(file_path:str)-> List[str]:
    """ 
    this function returns the list of requirements
    
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace('\n', "") for req in requirements]
        
        if hypen_minus_e in requirements:
            requirements.remove(hypen_minus_e)
            
    return requirements
    

setup(
    name="Big Mart Sales Project",
    version='0.0.1',
    author="Sameer Rewatkar",
    author_email='samirrewatkar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)