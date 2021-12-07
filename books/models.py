from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    available = models.BooleanField(default=False)
    publication_year = models.IntegerField()
    author = models.CharField(max_length=255)
