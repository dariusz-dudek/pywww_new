from faker import Faker
from .models import Book
from random import randint


def create_books(n=10):
    faker = Faker('pl_PL')
    for _ in range(n):
        book = Book(
            title=faker.text(randint(10, 30)),
            author=faker.name(),
            available=faker.boolean(),
            publication_year=randint(-1000, 2020),
            description=faker.text(randint(100, 400))
        )
        book.save()
