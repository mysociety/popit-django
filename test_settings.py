"""Settings that need to be set in order to run the tests."""

import os

DEBUG = True
USE_TZ = True
SITE_ID = 1

SECRET_KEY = '...something secure here...'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME":   "popit-django.sqlite3",
    }
}

MIDDLEWARE_CLASSES = []

ROOT_URLCONF = 'popit.tests.urls'

CURRENT_DIR = os.path.dirname(__file__)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(CURRENT_DIR, '../../static/')
STATICFILES_DIRS = (
    os.path.join(CURRENT_DIR, 'test_static'),
)

TEMPLATE_DIRS = (
    os.path.join(CURRENT_DIR, '../templates'),
)

INSTALLED_APPS = [
    'popit',
]

# Testing related
TEST_POPIT_API_HOST_IP   = '127.0.0.1'
TEST_POPIT_API_PORT      = '3000'
TEST_POPIT_API_SUBDOMAIN = 'popit-django-test'

# create the url to use for testing the database.
# See http://xip.io/ for details on the domain used.
TEST_POPIT_API_URL = "http://%s.%s.xip.io:%s/api" % ( TEST_POPIT_API_SUBDOMAIN,
                                                      TEST_POPIT_API_HOST_IP,
                                                      TEST_POPIT_API_PORT )

# If you want to create a test entry this is useful:
# curl                                           \
#     -v                                         \
#     -H "Content-type: application/json"        \
#     -X POST                                    \
#     -d ' {"name": "Joe Bloggs"}'               \
#     http://popit-django-test.127.0.0.1.xip.io:3000/api/persons/
