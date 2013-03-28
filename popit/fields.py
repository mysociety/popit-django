import re

from django.db import models

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^popit\.fields\.ApiInstanceURLField"])

class ApiInstanceURLField(models.URLField):
    # Have a specific field for this because we might want to add some smarts at
    # some point, and we want to check it is actually a url to prevent odd errors
    # from happening when bad values are entered and then subsequently tried to be
    # used when fetching data. By default model validation only happens when
    # submitted through a form (which is silly, but there you go).
        
    description = "A url field that enforces validation"

    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        value = super(ApiInstanceURLField, self).to_python(value)

        # Want immediate validation on creation
        for validator in self.validators:
            validator(value)

        return value
