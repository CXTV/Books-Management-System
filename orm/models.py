from django.db import models

# Create your models here.

class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    publishDate = models.DateField()
    publish = models.CharField(max_length=32)