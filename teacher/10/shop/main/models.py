from django.db import models
from django.utils.html import mark_safe
from image_cropping import ImageRatioField, ImageCropField

class Page(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    alias = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category,models.CASCADE)
    image = ImageCropField(upload_to='products', null=True, blank=True)
    cropping = ImageRatioField('image', '200x200')

    def image_tag(self):
        return mark_safe(f'<img  height="100" src="{self.image.url}" />')

    def __str__(self):
        return self.name