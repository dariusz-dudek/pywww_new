from django.db import models
from common.models import Timestamped


class Author(Timestamped):
    name = models.CharField(max_length=255)
    birth_year = models.IntegerField()
    death_year = models.IntegerField(blank=True, null=True)
    biogram = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Book(Timestamped):
    title = models.CharField(max_length=255)
    description = models.TextField()
    available = models.BooleanField(default=False)
    publication_year = models.IntegerField()
    authors = models.ManyToManyField('Author', related_name='author')
    tags = models.ManyToManyField('tags.Tag', related_name='books')
    cover = models.ImageField(upload_to='books/covers/%Y/%m/%d', null=True)

    def __str__(self):
        return f'{self.authors}: {self.title}'
