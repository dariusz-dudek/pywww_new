from django.db import models
from common.models import Timestamped
from datetime import datetime


class Post(Timestamped):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    sponsored = models.BooleanField(default=False)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tags = models.ManyToManyField('tags.Tag', related_name='posts')
    example_file = models.FileField(upload_to='posts/examples/', blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True, editable=False)
    image = models.ImageField(upload_to=f'posts/images/%Y/%m/%d', null=True, width_field='image_width')

    def __str__(self):
        return f'{self.id}: {self.title} '
