from setuptools import find_packages, setup


setup(
    name='Risk Adjustment Scoring Engine',
    version='0.1', 
    packages=find_packages(),
    install_requires=[
    	#python, you should list python depdencies(pip installables, not python itself)
    	#flask, it's not being used for this project.
    ],
    #python_requires='>=3.6', # if you want to target specific python version
    include_package_data=True,
)
