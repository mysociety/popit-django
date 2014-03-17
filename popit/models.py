import slumber

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

    def __unicode__(self):
        return 'PopIt instance <%s>' % self.url

    def api_client(self, collection_name):
        api = getattr(slumber.API(self.url), collection_name)
        return api

    def fetch_all_from_api(self):
        """
        Update all the local data from the API. This method actually delegates
        to the other models.
        """
        
        models = [Person]
        for model in models:
            model.fetch_all_from_api(instance=self)


class PopItDocument(models.Model):
    # The API instance is required
    api_instance = models.ForeignKey('ApiInstance')
    popit_url    = PopItURLField()
    popit_id     = models.CharField(max_length=200, null=True) # null for migration at least

    name         = models.CharField(max_length=200)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

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


    # This could possibly live on the manager and be called using Foo.objects.fetch_all_from_api(), perhaps ...
    @classmethod
    def fetch_all_from_api(cls, instance):
        """
        Get all the documents from the API and save them locally.
        """

        api_client = instance.api_client(cls.api_collection_name)

        # This is hacky, but I can't see a documented way to get to the url.
        # Liable to change if slumber changes their internals.
        collection_url = api_client._store['base_url']

        page = 1
        keep_fetching = True

        while keep_fetching:
            response = api_client.get(per_page=50, page=page)
            # In versions of popit-api before 0.0.14 there was no
            # pagination; in that case there will be no 'has_more' key
            # in the response, and all results will be returned.  In
            # versions 0.0.14 and later results are paginated by default
            # and there will always be a 'has_more' key indicating
            # whether further pages needed to be fetched or not.
            keep_fetching = response.get('has_more', False)
            page += 1

            for doc in response['result']:

                # Add url to the doc
                url = collection_url + '/' + doc['id']
                doc['popit_url'] = url
            
                cls.update_from_api_results(instance=instance, doc=doc)

    @classmethod
    def update_from_api_results(cls, instance, doc):

        # load the object from the db, or create it
        try:
            obj = cls.objects.get(popit_url=doc['popit_url'])
        except cls.DoesNotExist:
            # this is where generic fields (popit_url, popit_id) get set
            obj = cls(api_instance=instance, popit_url=doc['popit_url'], popit_id=doc['id'])

        # extract the dict of settable fields and update the obj
        settable = cls.extract_settable(doc)
        [setattr(obj, key, value) for (key, value) in settable.items()]

        obj.save()
        
        # TODO create/update related records here
        # obj.update_related_from_api_result(doc)

        return obj

    @classmethod
    def extract_settable(cls, doc):
        """
        You should override this method to extract the fields from the API
        result that should be set on the top level object. The response should
        be a dict of keys that are the field names, and values that are what
        should be set to them.

        This only applies to fields unique to the class - generic ones like
        popit_url are set elsewhere (in update_from_api_results).
        """
        raise NotImplementedError("Override extract_settable in '%s'" % cls)


class Person(PopItDocument):
    """A Person from a PopIt API instance"""

    api_collection_name = 'persons'

    image        = models.URLField(blank=True)
    summary      = models.TextField(blank=True)

    @classmethod
    def extract_settable(cls, doc):
        return {
            'name': doc['name'],
            'summary': doc.get('summary', ''),
            'image': doc.get('image', '')
        }

