from django.db import models
from common.models import Timestamped


class Post(Timestamped):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    sponsored = models.BooleanField(default=False)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tags = models.ManyToManyField('tags.Tag', related_name='posts')

    def __str__(self):
        return f'{self.id}: {self.title} '
