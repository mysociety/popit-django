#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='popit-django',
    version='0.0.0',
    description='Use PopIt stored data in your Django app',
    author='mySociety',
    author_email='modules@mysociety.org',
    url='https://github.com/mysociety/popit-django',
    long_description=open('README.md', 'r').read(),
    packages=[
        'FIXME'
    ],
    requires=[
    ],
    install_requires=[
    ],
    tests_require=[
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: AGPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)