#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup
import os
from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='popit-django',
    version='0.0.0',
    description='Use PopIt stored data in your Django app',
    author='mySociety',
    author_email='modules@mysociety.org',
    url='https://github.com/mysociety/popit-django',
    long_description=open('README.md', 'r').read(),

    # Not convinced that this is correct - it skips the fixture which are .js files
    packages=find_packages(),

    requires=[],
    install_requires=required,
    tests_require=[],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    test_suite='runtests.runtests',
)
