# -*- coding: utf-8 -*-
# @Author: Rocks
# @Date:   2017-11-01 16:54:32
# @Last Modified by:   Rocks
# @Last Modified time: 2017-11-01 16:55:33
from django.db import models

# Create your models here.

class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publishDate = models.DateField()
    pubname = models.ForeignKey(to='Pubname',to_field ='nid') #一对多
    authors=models.ManyToManyField(to='Author')

class Pubname(models.Model):
    nid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    address=models.CharField(max_length=32)
    email=models.EmailField()

    def __str__(self):
        return self.name

class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    authorInfo=models.OneToOneField(to="AuthorInfo")

class AuthorInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    birthday = models.DateField()
    phone = models.IntegerField()
    addr = models.CharField(max_length=64)











