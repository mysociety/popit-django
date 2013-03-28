from django.db import models
from django.core.exceptions import ValidationError

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

    def save(self, *args, **kwargs):
        """
        Add a check that the popit_url starts with the api_instance.url - so
        that we can be sure that the url is coming from the correct api.
        """
        if self.popit_url:
            try:
                self.popit_url.index(self.api_instance.url)
            except ValueError:
                raise ValidationError("popit_url does not start with its api_instance.url")

        super(PopItDocument, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Person(PopItDocument):
    """A Person from a PopIt API instance"""
    pass
