from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=48)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=128)
    site = models.URLField()


class Author(models.Model):
    first_name = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48)
    email = models.EmailField()


class Book(models.Model):
    title = models.CharField(max_length=512)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    publication_date = models.DateField()
