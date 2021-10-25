from django.db import models
from django.utils.html import mark_safe
from image_cropping import ImageRatioField, ImageCropField
from tinymce.models import HTMLField
from django.contrib.auth.models import User

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
    desc = HTMLField()
    category = models.ForeignKey(Category,models.CASCADE)
    image = ImageCropField(upload_to='products', null=True, blank=True)
    cropping = ImageRatioField('image', '200x200')

    def image_tag(self):
        return mark_safe(f'<img  height="100" src="{self.image.url}" />')

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    phone = models.CharField(max_length=250)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name



class Testimonial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.product.name


class ProductImage(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)



class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class CartOrder(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)