#!/usr/bin/env python3

from distutils.core import setup

setup (name = 'dvs-filters',
       version = '0.1',
       install_requires = ['numpy'],
       description = 'Python class for DVS filtering',
       packages = ['dvs_filters'],
       author='Simon D. Levy',
       author_email='simon.d.levy@gmail.com',
       url='https://github.com/simondlevy/dvs-filters',
       license='MIT',
       platforms='Linux; Windows; OS X'
    )
