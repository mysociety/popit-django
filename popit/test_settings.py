"""Settings that need to be set in order to run the tests."""

import os

DEBUG = True
USE_TZ = True
SITE_ID = 1

SECRET_KEY = '...something secure here...'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME":   "popit-django",
    }
}

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
