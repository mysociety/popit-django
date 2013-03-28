from django.db import models
from .fields import ApiInstanceURLField, PopItURLField

class ApiInstance(models.Model):
    """A specific PopIt API instance"""
    url = ApiInstanceURLField(
        unique    = True,
        help_text = "The full URL to the root of the api - eg 'http://example.com/api"
    )

    ### future fields might include:
    # name
    # last_checked - for incremental updates


class PopItDocument(models.Model):
    # The API instance is required
    api_instance = models.ForeignKey('ApiInstance')
    popit_url    = PopItURLField()

    name         = models.CharField(max_length=200)

    class Meta:
        abstract = True


class Person(PopItDocument):
    """A Person from a PopIt API instance"""
    pass
