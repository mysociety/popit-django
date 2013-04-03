from django.core.management.base import BaseCommand
from popit.models import ApiInstance

class Command(BaseCommand):
    help = 'Retrieve all documents from all PopIt API instances'

    def handle(self, *args, **options):
        for instance in ApiInstance.objects.all():
            instance.fetch_all_from_api()
