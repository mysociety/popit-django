#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='popit-django',
    version='0.0.2',
    description='Use PopIt stored data in your Django app',
    license='GNU Affero General Public License v3',
    author='mySociety',
    author_email='modules@mysociety.org',
    url='https://github.com/mysociety/popit-django',
    long_description=open('README.rst', 'r').read(),

    # Not convinced that this is correct - it skips the fixture which are .js files
    packages=find_packages(),

    requires=[],
    install_requires=required,
    tests_require=[],
    classifiers=[
        # choose from https://pypi.python.org/pypi?:action=list_classifiers
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    test_suite='runtests.runtests',
)
