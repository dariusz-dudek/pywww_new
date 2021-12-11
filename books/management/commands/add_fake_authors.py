from django.core.management.base import BaseCommand
from books.utils import create_authors


class Command(BaseCommand):
    help = 'Create fake authors'

    def add_arguments(self, parser):
        parser.add_argument(
            '-n', '--number',
            type=int, default=10, dest='number', help='Amount of authors to genereate'
        )

    def handle(self, *args, **options):
        n = options.get('number', 10)
        create_authors(n)
        self.stdout.write(f'{n} authors was created')
