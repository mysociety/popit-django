import slumber
import os
from subprocess import call

from django.conf import settings


def get_api_url():
    return settings.TEST_POPIT_API_URL
    
def get_api_client():
    return slumber.API(get_api_url())

def get_api_database_name():
    api = get_api_client()
    # https://github.com/dstufft/slumber/issues/28
    return api.__getattr__('').get()['info']['databaseName']

def delete_api_database():
    name = get_api_database_name()
    dev_null = open(os.devnull, 'w')
    call(["mongo", name, '--eval', 'db.dropDatabase()'], stdout=dev_null)
    
def load_test_data():
    """
    Use the mongofixtures CLI tool provided by the pow-mongodb-fixtures package
    used by popit-api to load some test data into db. Don't use the test fixture
    from popit-api though as we don't want changes to that to break our test
    suite.

        https://github.com/powmedia/pow-mongodb-fixtures#cli-usage

    """
    
    project_root = os.path.normpath(os.path.join(os.path.dirname(__file__), '../..'))
    
    # gather the args for the call
    mongofixtures_path = os.path.join( project_root, 'popit-api-for-testing/node_modules/.bin/mongofixtures' )
    database_name      = get_api_database_name()
    test_fixtures_path = os.path.join( project_root, 'popit/tests/fixtures.js' )

    # Hack to deal with bad handling of absolute paths in mongofixtures.
    # Fix: https://github.com/powmedia/pow-mongodb-fixtures/pull/14
    test_fixtures_path = os.path.relpath( test_fixtures_path )

    # Usage: mongofixtures db_name path/to/fixtures.js
    dev_null = open(os.devnull, 'w')
    call([mongofixtures_path, database_name, test_fixtures_path], stdout=dev_null)
