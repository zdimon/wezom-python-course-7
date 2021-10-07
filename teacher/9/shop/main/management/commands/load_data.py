from django.core.management.base import BaseCommand, CommandError

from main.models import Page, Category, Product

cats = ['cars', 'food', 'milk']

class Command(BaseCommand):
   
    def handle(self, *args, **options):
        print('Start loading....')
        Page.objects.all().delete()
        p = Page()
        p.title = 'Main page title'
        p.content = 'Main page Content Content Content Content Content Content'
        p.alias = 'mainpage'
        p.save()

        p = Page()
        p.title = 'About page title'
        p.content = 'About page Content Content Content Content Content Content'
        p.alias = 'about'
        p.save()

        Category.objects.all().delete()
        Product.objects.all().delete()
        for c in cats:
            nc = Category()
            nc.name = c
            nc.save()
            for i in range(1,5):
                p = Product()
                p.name = f'product {i}'
                p.category = nc
                p.save()



