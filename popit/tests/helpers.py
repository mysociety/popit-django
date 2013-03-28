
from django.conf import settings
import slumber
from subprocess import call

def get_api_client():
    return slumber.API(settings.TEST_POPIT_API_URL)

def get_api_database_name():
    api = get_api_client()
    # https://github.com/dstufft/slumber/issues/28
    return api.__getattr__('').get()['info']['databaseName']

def delete_api_database():
    name = get_api_database_name()
    call(["mongo", name, '--eval', 'db.dropDatabase()'])
    
