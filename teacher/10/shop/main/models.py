from django.db import models

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

    def __str__(self):
        return self.name