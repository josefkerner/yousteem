from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    #posts = models.ManyToManyField(Post)
    name = models.CharField(max_length=200)

class Post(models.Model):
    categories = models.ManyToManyField(Category)

    url= models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    score = models.DecimalField(decimal_places=2,max_digits=5)