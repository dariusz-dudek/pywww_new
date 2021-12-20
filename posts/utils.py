from django.contrib.auth.models import User
from faker import Faker
from .models import Post
from random import randint


def create_posts(n=10):
    faker = Faker('pl_PL')
    for _ in range(n):
        # c = faker.date_this_century()
        post = Post(
            title=faker.text(randint(10, 30)),
            content=faker.text(randint(100, 400)),
            published=faker.boolean(),
            sponsored=faker.boolean(),
            # created=c,
            # modified=c + faker.time_delta(10)
            author=User.objects.first()
        )
        post.save()
