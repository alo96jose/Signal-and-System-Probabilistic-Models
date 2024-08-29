from setuptools import find_packages, setup

setup(
    name='proceso',
    packages=find_packages(include=['proceso']),
    version='0.0.1',
    description='Proyecto 4 de IE0405 - Modelos Probabilísticos de Señales y Sistemas',
    author='Denisse Ugalde Rivera, Isabel Sabater Aguilar, Alonso José Jiménez Anchía',
    license='MIT',
    install_requires=[
        'numpy',
        'scipy',
        'requests',
        'pandas'
    ],
)
