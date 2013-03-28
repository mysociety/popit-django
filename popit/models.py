from django.db import models
from .fields import ApiInstanceURLField

class ApiInstance(models.Model):
    """A specific PopIt API instance"""
    url = ApiInstanceURLField(
        unique    = True,
        help_text = "The full URL to the root of the api - eg 'http://example.com/api"
    )

    ### future fields might include:
    # name
    # last_checked - for incremental updates


# Create your models here.
