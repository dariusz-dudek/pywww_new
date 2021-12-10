from django.db import models
from django.utils.timezone import now, timedelta


class CheckAgeMixin:

    def is_older_than_n_days(self, n=1):
        """Check if created is older than now() - days"""
        delta = timedelta(days=n)
        return now() - self.created > delta


class Timestamped(models.Model, CheckAgeMixin):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(Timestamped):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    sponsored = models.BooleanField(default=False)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tags = models.ManyToManyField('tags.Tag', related_name='posts')

    def __str__(self):
        return f'{self.id}: {self.title} '
