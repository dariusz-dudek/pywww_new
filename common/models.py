import random
import string
from django.utils.text import slugify
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


# class SlugMixin(models.Model):
#     slug = models.SlugField(max_length=100, unique=True)
#
#     @staticmethod
#     def get_random_text(n):
#         letters = string.ascii_letters
#         return ''.join(random.choice(letters) for i in range(n))
#
#     def save(self, *args, **kwargs):
#         if self._state.adding and not self.slug:
#             slug = slugify(self.slug)
#             slugs = self.__class__.objects.filter(slug=slug).values_list('slug', flat=True)
#             if slugs:
#                 while True:
#                     if slug in slugs:
#                         slug += SlugMixin.get_random_text(5)
#                     else:
#                         break
#             self.slug = slug
#         return super().save(*args, **kwargs)
