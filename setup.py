from setuptools import find_packages,setup # this will install packages and setup
from typing import List

HYPEN_E_DOT='-e .'  # this will trigger setup.py file this is not a package

## defining a function such that setup.py will install the packages from requirements.txt

def get_requirements(file_path:str)->List[str]: 
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]  # replacing 'new line' with 'space' 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  # removing HYPEN_E_DOT to install packages

        return requirements


setup(
    name='Diamond_Price_Prediction',
    version='0.0.1',
    author='vipul',
    author_email='vipul7905853921@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

)

## src will automatically get converted into packages
# __init__.py
# to run (python setup.py install)  --  1st way

# to run (pip install -r requirements.txt)     -- 2nd way through  HYPEN_E_DOT