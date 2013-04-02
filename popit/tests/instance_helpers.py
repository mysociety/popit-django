import slumber
import os
import subprocess

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
    subprocess.call(["mongo", name, '--eval', 'db.dropDatabase()'], stdout=dev_null)
    
def load_test_data(fixture_name='default'):
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
    test_fixtures_path = os.path.join( project_root, 'popit/tests/fixtures/%s.js'%fixture_name )

    # Check that the fixture exists
    if not os.path.exists(test_fixtures_path):
        raise Exception("Could not find fixture for %s at %s" % (fixture_name, test_fixtures_path))

    # Hack to deal with bad handling of absolute paths in mongofixtures.
    # Fix: https://github.com/powmedia/pow-mongodb-fixtures/pull/14
    test_fixtures_path = os.path.relpath( test_fixtures_path )

    # Usage: mongofixtures db_name path/to/fixtures.js
    try:
        output = subprocess.check_output([mongofixtures_path, database_name, test_fixtures_path], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output)
