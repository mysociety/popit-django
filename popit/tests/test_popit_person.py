# coding=utf-8
from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
import simplejson as json
import urllib
import re
from popit.tests import instance_helpers

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
        
        # check it is empty string when fetched from db
        self.assertEqual( Person.objects.get(pk=person_no_url_1.id).popit_url, '')
        
        # url to use when testing
        popit_url = popit_url=instance.url + '/person/123'

        # create one with a popit_url
        person_with_url = Person(api_instance=instance, name="Bob", popit_url=popit_url)
        person_with_url.save()
        self.assertTrue(person_no_url_1)
        
        # try to create a duplicate one
        self.assertRaises(IntegrityError, Person.objects.create, api_instance=instance, name="Bob", popit_url=popit_url)

        # try to create one with a bad URL
        self.assertRaises(ValidationError, Person.objects.create, api_instance=instance, name="Bob", popit_url='This is not a URL')

        # try to create one with a URL that does not start with the ApiInstance URL
        # (implying that it is from a different instance)
        self.assertRaises(ValidationError, Person.objects.create, api_instance=instance, name="Bob", popit_url='http://other.com/api/person/123')


    def test_post_a_person_to_the_api(self):
        instance = ApiInstance.objects.create(url=instance_helpers.get_api_url())
        person = Person.objects.create(api_instance=instance, name="Juan Perez")


        person.post_to_the_api()

        self.assertTrue(person.popit_url)
        my_re = re.compile(instance.url + "/persons/([^/]+)/{0,1}")
        self.assertTrue(my_re.match(person.popit_url))
        person_id = my_re.match(person.popit_url).groups()[0]


        #trying to get the person from the actual api
        response = urllib.urlopen(person.popit_url)
        self.assertEquals(response.code, 200)
        response_as_json = json.loads(response.read())
        
        # The popit-api responds something like this
        # {
        #   "result": {
        #     "name": "Juan Perez",
        #     "id": "522e2e23a68f91773a000001",
        #     "image": "http://url/to/the/image.png",
        #     "summary": "Juan Perez es un desarrollador de la fundación ciudadano inteligente que programa en ruby"
        # }

        self.assertEquals(response_as_json['result']['id'], person_id)
        self.assertEquals(response_as_json['result']['name'], person.name)
        #It should have image and summary empty
        self.assertIn('image',response_as_json['result'])
        self.assertIn('summary',response_as_json['result'])
        #yes it should be empty
        self.assertEquals(len(response_as_json['result']['image']), 0)
        self.assertEquals(len(response_as_json['result']['summary']), 0)