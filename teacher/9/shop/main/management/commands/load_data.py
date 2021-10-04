from django.core.management.base import BaseCommand, CommandError

from main.models import Page


class Command(BaseCommand):
   
    def handle(self, *args, **options):
        print('Start loading....')
        Page.objects.all().delete()
        p = Page()
        p.title = 'Test'
        p.content = 'Content'
        p.save()