# Copyright (c) 2022 Wizart Animation.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Prodtrack
# Source Code License. By accessing, using, copying or modifying
# this work you indicate your agreement to the Prodtrack Source Code License.
# All rights not expressly granted therein are reserved by Wizart Animation.

import os

from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='lavka_prikolov',
    version="",
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
    license='',
    description='Lavka Prikolov',
    url='http://127.0.0.1:8000/',
    author='Marie Ardenn',
    author_email='',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 4.2',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
