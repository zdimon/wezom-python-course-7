from django.db import models

class Page(models.Model):
    title=models.CharField(max_length = 300)
    content = models.CharField(max_length = 2500)
    alias = models.CharField(max_length = 300,
    null = True, blank = True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=300)       
    category= models.ForeignKey(Category,models.
    CASCADE)
    image = models.ImageField(upload_to= 'products', null = True,blank = True)

    def __str__(self):
        return self.name   

