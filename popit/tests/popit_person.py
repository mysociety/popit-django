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
    

    def test_popit_url(self):
        """
        Test that the popit_url field is unique if it has a value and that it is
        possible to have several with no value.
        """
        
        # create instance
        instance = ApiInstance(url="http://foo.com/api")
        instance.save()
        self.assertTrue(instance)
        
        # create a person with no popit_url
        person_no_url_1 = Person(api_instance=instance, name="Bob")
        person_no_url_1.save()
        self.assertTrue(person_no_url_1)
        
        # create another
        person_no_url_2 = Person(api_instance=instance, name="Bob")
        person_no_url_2.save()
        self.assertTrue(person_no_url_2)
        
        # check that the empty popit_url is returned as empty string
        self.assertEqual(person_no_url_1.popit_url, '')
        
        # url to use when testing
        popit_url = popit_url=instance.url + '/person/123'

        # create one with a popit_url
        person_with_url = Person(api_instance=instance, name="Bob", popit_url=popit_url)
        person_with_url.save()
        self.assertTrue(person_no_url_1)
        
        # try to create a duplicate one
        self.assertRaises(IntegrityError, Person.objects.create, api_instance=instance, name="Bob", popit_url=popit_url)
