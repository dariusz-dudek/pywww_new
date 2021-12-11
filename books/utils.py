from faker import Faker
from .models import Book, Author
from random import randint, choice


def create_books(n=10):
    faker = Faker('pl_PL')
    authors = Author.objects.all()
    for _ in range(n):
        book = Book()
        book.title = faker.text(randint(10, 30))
        book.available = faker.boolean()
        book.publication_year = randint(-1000, 2020)
        book.description = faker.text(randint(100, 400))
        book.save()
        book.author.add(choice(authors))


def create_authors(n=10):
    faker = Faker('pl_PL')

    for _ in range(n):
        birth_year = randint(-500, 1980)
        author = Author(
            name=faker.name(),
            birth_year=birth_year,
            death_year=birth_year + randint(20, 90),
            biogram=faker.text(randint(100, 400))
        )
        author.save()
