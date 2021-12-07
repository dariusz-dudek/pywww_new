from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}: {self.title} '