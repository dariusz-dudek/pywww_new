from django.core.management.base import BaseCommand
from books.utils import create_books


class Command(BaseCommand):
    help = 'Create fake books'

    def add_arguments(self, parser):
        parser.add_argument(
            '-n', '--number',
            type=int, default=10, dest='number', help='Amount of books to generate'
        )

    def handle(self, *args, **options):
        n = options.get('number', 10)
        create_books(n)
        self.stdout.write(f'{n} books was create')
