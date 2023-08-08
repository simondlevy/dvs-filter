#!/usr/bin/env python3

'''
Python distutils setup file for dvs_filters module.

Copyright (C) 2023 Simon D. Levy

MIT License
'''

#from distutils.core import setup
from setuptools import setup

setup (name = 'dvs-filters',
    version = '0.1',
    install_requires = ['numpy'],
    description = 'Python class for DVS filtering',
    packages = ['dvsfilter'],
    author='Simon D. Levy',
    author_email='simon.d.levy@gmail.com',
    url='https://github.com/simondlevy/eDVS',
    license='MIT',
    platforms='Linux; Windows; OS X'
    )
