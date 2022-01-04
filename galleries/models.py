import random
import string

from django.db import models
from common.models import Timestamped
from django.utils.text import slugify
from sorl.thumbnail import ImageField


def get_random_text(n):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(n))


class Gallery(Timestamped):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if self._state.adding and not self.slug:
            slug = slugify(self.slug)
            slugs = self.__class__.objects.filter(slug=slug).values_list('slug', flat=True)
            if slugs:
                while True:
                    if slug in slugs:
                        slug += get_random_text(5)
                    else:
                        break
            self.slug = slug
        return super().save(*args, **kwargs)


def upload_to(instance, filename):
    return f'galleries/{instance.gallery.slug}/{filename}'


class Photo(Timestamped):
    title = models.TextField(max_length=255)
    slug = models.SlugField(unique=True, max_length=100)
    short_description = models.CharField(max_length=300, null=True, blank=True)
    image = ImageField(upload_to=upload_to)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='photos')
    source = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return f'{self.slug}'
