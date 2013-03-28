from django.test import TestCase
from django.db import IntegrityError

from popit.models import ApiInstance, Person

class PersonTest(TestCase):
    def test_instance_is_required(self):
        """
        Test that instance is required
        """
        # create instance
        instance = ApiInstance(url="http://foo.com/api")
        instance.save()
        self.assertTrue(instance)
        
        # create person
        person = Person(api_instance=instance, name="Bob")
        person.save()
        self.assertTrue(person)

        # try to create without instance
        self.assertRaises(IntegrityError, Person.objects.create, name="Bob") # instance missing
        