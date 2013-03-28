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


add_introspection_rules([], ["^popit\.fields\.PopItURLField"])

class PopItURLField(models.URLField):
    # This field has some specific requirements - namely it is optional (locally
    # created docs won't have it) but if it has a value it should be unique. Should
    # also be a URL.
    #
    # This mean that it should store a NULL in the db when it is empty so that the
    # DB constraints act as expected (default Django behaviour would be to store an
    # empty string).
    #
    # Not implemented here would be a check that the url starts with the url of the
    # PopIt instance that the object is linked to.
    #
    # NOTE - this relies on the database behaviour regarding UNIQUE constraints, and
    # NULL fields. If your DB does not allow several NULLs in a UNIQUE index then
    # this won't work. Will work in Postgres and SQLite3, might work in mySQL
    # depending on table type, probably won't work in SQLServer.
        
    description = "A url field that enforces validation and uniqueness if not empty"
    
    __metaclass__ = models.SubfieldBase
    
    def __init__(self, *args, **kwargs):

        # enforce some of the options
        kwargs['unique']  = True
        kwargs['blank']   = True
        kwargs['null']    = True
        kwargs['default'] = ''

        super(PopItURLField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        value = super(PopItURLField, self).to_python(value)

        # Want immediate validation on creation (if there is a value)
        if value != '':
            for validator in self.validators:
                validator(value)

        return value

    def get_db_prep_value(self, value, **kwargs):
        # return None if empty string - so that null is stored in db
        # see http://stackoverflow.com/a/5114226/5349 for partial source
        if value == "":
            return None
        else:
            return value
