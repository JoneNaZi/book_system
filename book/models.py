from django.db import models

# Create your models here.


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, null=False, unique=True)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, null=False, unique=True)
    publisher = models.ForeignKey(to='Publisher', on_delete=models.CASCADE)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, null=False, unique=True)
    book = models.ManyToManyField(to="Book")