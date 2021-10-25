from django.core.management.base import BaseCommand, CommandError
from django.core.files import File 
from main.models import Page, Category, Product, ProductImage
from shop.settings import BASE_DIR
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

                image_path = f'{BASE_DIR}/data/images/w{i}.jpg'
                print(image_path)
                p.image.save('test.jpg',File(open(image_path, 'rb')))

                for ip in range(1,5):
                    pi = ProductImage()
                    pi.title = f'image {ip}'
                    pi.product = p
                    pi.save()
                    image_path = f'{BASE_DIR}/data/images/w{ip}.jpg'                    
                    pi.image.save('test.jpg',File(open(image_path, 'rb')))


