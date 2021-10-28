from django.db import models

# Create your models here.
class UserMessages(models.Model):
    username = models.CharField(max_length=250)
    text = models.TextField()