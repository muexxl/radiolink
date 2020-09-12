# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='radiolink',
    version='0.1.0',
    description='Radiolink package for communication with multiple RF24 modules',
    long_description=readme,
    author='Stephan Muekusch',
    author_email='stephan@1drone.de',
    url='https://github.com/muexxl',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

