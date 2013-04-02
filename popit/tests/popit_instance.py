from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from popit.models import ApiInstance, Person
from popit.tests import instance_helpers

class ApiInstanceTest(TestCase):
    def test_url_constraints(self):
        """
        Test that url is required and unique
        """
        # create a good one
        instance = ApiInstance(url="http://foo.com/api")
        instance.save()
        self.assertTrue(instance)
        
        # test that the url is required and must be a url - even when creating entries
        # from code.
        self.assertRaises(ValidationError, ApiInstance, url="not a url")
        self.assertRaises(ValidationError, ApiInstance) # url missing

        # test that we can't create a duplicate
        def save_duplicate():
            ApiInstance(url=instance.url).save()
        self.assertRaises(IntegrityError, save_duplicate)
        

    def test_retrieve_all_from_instance(self):
        """
        Test that it is possible to retrieve several people from the instance.
        """
    
        # create the instance, delete contents and load test fixture
        instance_helpers.delete_api_database()
        instance_helpers.load_test_data()
        instance = ApiInstance.objects.create(url=instance_helpers.get_api_url())
        self.assertTrue(instance)
    
        # Tell the instance to sync data
        instance.fetch_all_from_api()
    
        # check that the persons expected are loaded
        person = Person.objects.get(name='Joe Bloggs')
        self.assertTrue(person)

        # update the api to use a different fixture and check that the update is
        # applied
        instance_helpers.delete_api_database()
        instance_helpers.load_test_data('rename_joe_blogs')
        instance.fetch_all_from_api()
        renamed = Person.objects.get(pk=person.id)
        self.assertEqual(renamed.name, 'Josh Blaggs')


        