#!/usr/bin/env python

# This file mainly exists to allow python setup.py test to work.
#
# You can test all the variations of tests by running:
#
#   ./manage.py test && python runtests.py && ./setup.py test && echo OK
#

import os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'

import django
from django.core.management import call_command

def runtests():
    if django.VERSION[:2] >= (1, 7):
        django.setup()
    # use the call_command approach so that we are as similar to running
    # './manage.py test' as possible. Notably we need the South migrations to be
    # run.
    call_command('test', verbosity=2)
    sys.exit(0)

if __name__ == '__main__':
    runtests()
