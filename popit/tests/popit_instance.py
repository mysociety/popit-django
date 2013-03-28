from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from popit.models import ApiInstance

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
        
